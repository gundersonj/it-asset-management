from django.test import TestCase, tag
from django.urls import reverse, resolve
from setup.views import LocationListView


@tag("listview")
class LocationListViewTests(TestCase):
    def setUp(self):
        url = reverse("setup:location_list")
        self.response = self.client.get(url)

    @tag("status_code")
    def test_location_list_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    @tag("template")
    def test_location_list_template(self):
        self.assertTemplateUsed(self.response, "setup/locations/location_list.html")

    @tag("contains_correct", "html")
    def test_location_list_contains_correct_html_code(self):
        self.assertContains(self.response, "Locations", status_code=200, html=False)

    @tag("contains_incorrect", "html")
    def test_location_list_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Homepage")

    @tag("resolve", "url")
    def test_location_list_url_resolves_location_list_view(self):
        view = resolve("/setup/locations/")
        self.assertEqual(
            view.func.__name__,
            LocationListView.as_view().__name__,
        )
