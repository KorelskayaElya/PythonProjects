from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
def recipe(request,recipe_name):
    # параметр количества порций, по умолчанию 1 порция
    servings = int(request.GET.get('servings', '1'))
    if recipe_name in DATA:
        # достаем нужный рецепт
        recipe = DATA[recipe_name]
        # создаем новый словарь с изменениями количества
        scaled_recipe = {}
        for ingredient, quantity in recipe.items():
            # расчитываем кол-во порций
            scaled_quantity = quantity*servings
            # кладем в словарь новое значение количества
            scaled_recipe[ingredient] = scaled_quantity
        # создаем контекст, передав в html два параметра recipe_name и recipe
        context = {
            'recipe_name': recipe_name,
            'recipe': scaled_recipe,
        }
        # передаем визуальную часть страницы
        return render(request,'calculator/index.html',context)
    else:
        # при вводе неправильного названия рецепта - выводим сообщение
        return HttpResponse('Рецепт не найден')
