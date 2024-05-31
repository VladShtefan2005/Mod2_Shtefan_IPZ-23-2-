from django.test import TestCase
from .models import Category, Recipe


class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Desserts")
        self.assertEqual(category.name, "Desserts")
        self.assertEqual(str(category), "Desserts")


class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")

    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            title="Chocolate Cake",
            description="Delicious chocolate cake",
            instructions="Mix ingredients and bake",
            ingredients="Flour, Sugar, Cocoa, Baking Powder, Eggs, Milk",
            category=self.category
        )
        self.assertEqual(recipe.title, "Chocolate Cake")
        self.assertEqual(recipe.description, "Delicious chocolate cake")
        self.assertEqual(recipe.instructions, "Mix ingredients and bake")
        self.assertEqual(recipe.ingredients, "Flour, Sugar, Cocoa, Baking Powder, Eggs, Milk")
        self.assertEqual(recipe.category.name, "Desserts")
        self.assertIsNotNone(recipe.created_at)
        self.assertIsNotNone(recipe.updated_at)
        self.assertEqual(str(recipe), "Chocolate Cake")

