"""
Sample tests
"""

# docker-compose run --rm app sh -c "python manage.py test" -> to run the test case 

from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc modules"""

    def test_add_numbers(self):
        """test adding numbers together"""
        res = calc.add(5, 6)
        """To check if the result is equal or not, if this has the same result it will return True"""
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Subtracting the numbers"""
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)