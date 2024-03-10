from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm
from .models import Recipe
import random
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


def home(request):
    recipes = list(Recipe.objects.all())
    random_recipes = random.sample(recipes, 5) if len(recipes) > 5 else recipes
    return render(request, 'home.html', {'recipes': random_recipes})


def recipe_detail(request, user_id):
    recipe = get_object_or_404(Recipe, id=user_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            new_recipe = Recipe(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                steps=form.cleaned_data['steps'],
                cooking_time=form.cleaned_data['cooking_time'],
                author=request.user,
            )
            if 'image' in request.FILES:
                new_recipe.image = form.cleaned_data['image']
            new_recipe.save()
            categories = form.cleaned_data.get('categories')
            if categories:
                new_recipe.categories.set(categories)
            return redirect('recipe_detail', id=new_recipe.id)
    else:
        form = RecipeForm()
    return render(request, 'add_edit_recipe.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Неверный логин или пароль')
    else:
        return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return render(request, 'logout.html')
