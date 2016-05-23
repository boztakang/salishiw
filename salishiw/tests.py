from django.test import TestCase
from django.core.urlresolvers import reverse

class HomeViewTests(TestCase):

    def test_home_view_title(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Salish Irish Wolfhounds")
        