from album.models import Category
from django.test import TestCase

# Create your tests here.

#Test Category:
class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category(name='food')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0) 
