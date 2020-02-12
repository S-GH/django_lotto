from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.
class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name='Test numbers', text='selected numbers')
        g.generate()
        print(g.update_date)
        print(g.lottos)

        # test case, 로또의 길이가 20이상이여야 한다.
        self.assertTrue(len(g.lottos)>20)
