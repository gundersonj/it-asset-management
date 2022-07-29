from django.test import TestCase, tag
from django.urls import reverse, resolve
from setup.views import LocationListView, LocationCreateView, LocationUpdateView
from setup.models import Location


@tag("model")
class LocationModelTests(TestCase):
    def setUp(self):
        self.location = Location.objects.create(
            location_id="001", location_name="Test Location",
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
    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    @tag("template")
    def test_template(self):
        self.assertTemplateUsed(self.response, "setup/locations/location_list.html")

    @tag("correct_html")
    def test_contains_correct_html_code(self):
        self.assertContains(self.response, "Locations", status_code=200, html=False)

    @tag("incorrect_html")
    def test_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Homepage")

    @tag("resolve", "url")
    def test_url_resolves_view(self):
        view = resolve("/setup/locations/")
        self.assertEqual(
            view.func.__name__, LocationListView.as_view().__name__,
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

    @tag("status_code")
    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    @tag("template")
    def test_template(self):
        self.assertTemplateUsed(self.response, "setup/locations/location_add.html")

    @tag("correct_html")
    def test_contains_correct_html_code(self):
        self.assertContains(self.response, "Save Location")

    @tag("incorrect_html")
    def test_does_not_contain_incorrect_html_code(self):
        self.assertNotContains(self.response, "Homepage")

    @tag("resolve", "url")
    def test_url_resolves_location_create_view(self):
        view = resolve("/setup/locations/add/")
        self.assertEqual(
            view.func.__name__, LocationCreateView.as_view().__name__,
        )


@tag("updateview")
class LocationUpdateViewTests(TestCase):
    def setUp(self):
        self.new_location = Location.objects.create(
            location_id="002", location_name="2nd Location",
        )
        self.response = self.client.post(
            reverse(
                "setup:location_edit", kwargs={"pk": self.new_location.location_id}
            ),
            {"location_id": "002", "location_name": "2nd Test Location",},
        )

    @tag("status_code")
    def test_status_code(self):
        self.assertEqual(self.response.status_code, 302)

    @tag("resolve", "url")
    def test_url_resolves_view(self):
        view = resolve("/setup/locations/002/edit/")
        self.assertEqual(
            view.func.__name__, LocationUpdateView.as_view().__name__,
        )
