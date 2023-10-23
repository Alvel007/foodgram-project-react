from django.contrib import admin

from .forms import TagForm
from foodgram.settings import EMPTY_VALUE_DISPLAY
from recipes.models import (Cart, Favorite, Ingredient,
                            IngredientRecipe, Recipe, Tag,
                            TagRecipe)


class TagRecipeInline(admin.TabularInline):
    model = TagRecipe
    extra = 1


class IngredientRecipeInline(admin.TabularInline):
    model = IngredientRecipe
    extra = 1


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit',)
    search_fields = ('name',)
    list_filter = ('measurement_unit',)
    empty_value_display = EMPTY_VALUE_DISPLAY
    inlines = (IngredientRecipeInline,)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug',)
    search_fields = ('name',)
    empty_value_display = EMPTY_VALUE_DISPLAY
    inlines = (TagRecipeInline,)
    form = TagForm


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'name',)
    list_filter = ('tags',)
    search_fields = ('name', 'author__username', 'author__email')
    empty_value_display = EMPTY_VALUE_DISPLAY
    filter_vertical = ('tags',)
    inlines = (TagRecipeInline, IngredientRecipeInline,)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user',)
    search_fields = ('recipe__name', 'user__username', 'user__email')
    empty_value_display = EMPTY_VALUE_DISPLAY


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user',)
    search_fields = ('user__username', 'user__email')
    empty_value_display = EMPTY_VALUE_DISPLAY
