import unittest
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
from hillel_automation__2026.lesson_12.homework_12 import sum_two_numbers, count_letter, replace_dots, clean_text


class MyTest(unittest.TestCase):

    def test_1(self):
        actual_result = sum_two_numbers(1, 3)
        expected_result = 4
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        actual_result = sum_two_numbers(1, 3)
        self.assertIsNotNone(actual_result)

    def test_3(self):
        actual_result = sum_two_numbers(1, 3)
        self.assertTrue(actual_result)

    def test_4(self):
        with self.assertRaises(TypeError):
            sum_two_numbers(None, None)

    def test_5(self):
        actual_result = count_letter("hello", "h")
        self.assertIsInstance(actual_result, int)

    def test_6(self):
        with self.assertRaises(TypeError):
            count_letter("hello", None)

    def test_7(self):
        actual_result = replace_dots("hello....world")
        expected_result = "hello world"
        self.assertEqual(expected_result, actual_result)

    def test_8(self):
        with self.assertRaises(AttributeError):
            replace_dots(123)

    def test_9(self):
        text = "test   test   test"
        actual_result = clean_text(text)
        expected_result = "test test test"
        self.assertEqual(expected_result, actual_result)

    def test_10(self):
        text = "test   test   test"
        actual_result = clean_text(text)
        self.assertIsInstance(actual_result, str)

    def test_11(self):
        with self.assertRaises(AttributeError):
            clean_text(123)

    def test_12(self):
        actual_result = clean_text("test")
        self.assertTrue(actual_result)
