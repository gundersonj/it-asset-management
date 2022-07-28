from django.test import TestCase, tag
from django.urls import reverse, resolve
from setup.views import LocationListView, LocationCreateView
from setup.models import Location


@tag("location", "model")
class LocationModelTests(TestCase):
    def setUp(self):
        self.location = Location.objects.create(
            location_id="001",
            location_name="Test Location",
        )

    def test_create_location_id(self):
        self.assertEqual(self.location.location_id, "001")

    def test_create_location_name(self):
        self.assertEqual(self.location.location_name, "Test Location")

    def test_location_model_str(self):
        self.assertEqual(str(self.location.location_name), "Test Location")


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


@tag("location", "createview")
class LocationCreateViewTests(TestCase):
    def setUp(self):
        url = reverse("setup:location_add")
        self.response = self.client.get(url)

        self.client.post(
            reverse("setup:location_add"),
            {"location_id": "002", "location_name": "Second Loc"},
        )
        self.location = Location.objects.last()

    def test_location_creation(self):
        self.assertEqual(self.location.location_id, "002")
        self.assertEqual(self.location.location_name, "Second Loc")

    def test_location_create_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_location_create_template(self):
        self.assertTemplateUsed(self.response, "setup/locations/location_add.html")

    def test_location_create_view_contains_correct_html_code(self):
        self.assertContains(self.response, "Save Location")

    def test_location_create_view_does_not_contain_incorrect_html_code(self):
        self.assertNotContains(self.response, "Homepage")

    def test_location_create_view_url_resolves_location_create_view(self):
        view = resolve("/setup/locations/add/")
        self.assertEqual(
            view.func.__name__,
            LocationCreateView.as_view().__name__,
        )
