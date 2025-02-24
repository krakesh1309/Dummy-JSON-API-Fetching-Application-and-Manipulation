from django.shortcuts import render
import json
# Create your views here.
file = open(r'E:\Django\Dummy\recipes.json', 'r')
json_data = file.read()
data = json.loads(json_data)
recipes = data['recipes']

def allrecipes(request):
    context = {
        'recipes':recipes
    }
    return render(request, 'recipes.html', context)

def recipeview(request, id):
    context= {
        'recipe': recipes[id-1]
    }
    return render(request, 'recipe.html', context)