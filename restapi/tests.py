# from django.test import TestCase
from unittest import TestCase

# Create your tests here.


def add_two(a, b):
    return a + b


class TestSum(TestCase):
    def test_addition(self):
        self.assertEqual(add_two(1, 2), 3)
