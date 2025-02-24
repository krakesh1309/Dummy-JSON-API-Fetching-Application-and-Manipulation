from django.shortcuts import render, get_object_or_404
import json
import os

# Existing recipes_view
def recipes_view(request):
    json_file_path = os.path.join('E:\\Django\\Project_template', 'recipes.json')
    with open(json_file_path, 'r') as json_file:
        recipes = json.load(json_file)
    
    context = {
        'recipes': recipes['recipes']
    }
    return render(request, 'recipes.html', context)

# New recipe_detail_view
def recipe_detail_view(request, recipe_id):
    json_file_path = os.path.join('E:\\Django\\Project_template', 'recipes.json')
    with open(json_file_path, 'r') as json_file:
        recipes = json.load(json_file)['recipes']
    
    # Find the specific recipe by ID
    recipe = next((item for item in recipes if item["id"] == recipe_id), None)
    
    if recipe is None:
        return render(request, '404.html', status=404)
    
    context = {
        'recipe': recipe
    }
    return render(request, 'recipe_details.html', context)
