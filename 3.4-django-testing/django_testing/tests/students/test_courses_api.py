import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(**kwargs):
        return baker.make("students.Course", **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(**kwargs):
        return baker.make("students.Student", **kwargs)

    return factory


@pytest.mark.django_db
def test_retrieve_course(api_client, course_factory):
    course = course_factory()
    url = f"/api/v1/courses/{course.id}/"
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.json()["id"] == course.id
    assert response.json()["name"] == course.name


@pytest.mark.django_db
def test_list_courses(api_client, course_factory):
    courses = course_factory(_quantity=3)
    url = "/api/v1/courses/"
    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.json()) == 3


@pytest.mark.django_db
def test_filter_courses_by_id(api_client, course_factory):
    courses = course_factory(_quantity=3)
    course_id_to_filter = courses[1].id
    url = f"/api/v1/courses/?id={course_id_to_filter}"
    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["id"] == course_id_to_filter


@pytest.mark.django_db
def test_filter_courses_by_name(api_client, course_factory):
    course = course_factory(name="Math")
    url = f"/api/v1/courses/?name={course.name}"
    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == course.name


@pytest.mark.django_db
def test_create_course(api_client):
    data = {
        "name": "History",
        "students": []
    }
    url = "/api/v1/courses/"
    response = api_client.post(url, data, format="json")

    assert response.status_code == 201
    assert Course.objects.filter(name=data["name"]).exists()


@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    course = course_factory()
    data = {
        "name": "Updated Course",
        "students": []
    }
    url = f"/api/v1/courses/{course.id}/"
    response = api_client.put(url, data, format="json")

    assert response.status_code == 200
    course.refresh_from_db()
    assert course.name == data["name"]


@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    course = course_factory()
    url = f"/api/v1/courses/{course.id}/"
    response = api_client.delete(url)

    assert response.status_code == 204
    assert not Course.objects.filter(id=course.id).exists()


