from django.test import TestCase

# Create your tests here.
class HomeTest(TestCase):
    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)


class AboutTest(TestCase):
    def test_about_status_code(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)   


class PostTest(TestCase):
    def test_post_status_code(self):
        response = self.client.get('/post/')
        self.assertEquals(response.status_code, 200)   

class PostDetailTest(TestCase):
    def test_post_detail_status_code(self):
        response = self.client.get('/post/1/')
        self.assertEquals(response.status_code, 200)                          