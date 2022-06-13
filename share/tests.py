from django.test import TestCase

# Create your tests here.
class HomeTest(TestCase):
    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)