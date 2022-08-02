from django.test import TestCase, tag
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from setup.views import LocationListView, LocationCreateView, LocationUpdateView
from setup.models import Location


@tag("model")
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
        self.user = get_user_model().objects.create_user(
            username="TestUser",
            email="test@email.com",
            password="testpass123",
        )
        self.login = self.client.login(
            username="TestUser",
            password="testpass123",
        )
        url = reverse("setup:location_list")
        self.response = self.client.get(url)

    @tag("status_code", "logged_in")
    def test_status_code_for_logged_in_user(self):
        self.assertEqual(self.response.status_code, 200)

    @tag("template", "logged_in")
    def test_template_for_logged_in_user(self):
        self.assertTemplateUsed(self.response, "setup/locations/location_list.html")

    @tag("correct_html", "logged_in")
    def test_contains_correct_html_code_for_logged_in_user(self):
        self.assertContains(self.response, "Locations", status_code=200, html=False)

    @tag("incorrect_html", "logged_in")
    def test_does_not_contain_incorrect_html_for_logged_in_user(self):
        self.assertNotContains(self.response, "Homepage")

    @tag("resolve", "url", "logged_in")
    def test_url_resolves_view_for_logged_in_user(self):
        view = resolve("/setup/locations/")
        self.assertEqual(
            view.func.__name__,
            LocationListView.as_view().__name__,
        )


@tag("location", "createview")
class LocationCreateViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="TestUser",
            email="test@email.com",
            password="testpass123",
        )
        self.login = self.client.login(
            username="TestUser",
            password="testpass123",
        )
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

    @tag("status_code", "logged_in")
    def test_status_code_for_logged_in_user(self):
        self.assertEqual(self.response.status_code, 200)

    @tag("template", "logged_in")
    def test_template_for_logged_in_user(self):
        self.assertTemplateUsed(self.response, "setup/locations/location_add.html")

    @tag("correct_html", "logged_in")
    def test_contains_correct_html_code_for_logged_in_user(self):
        self.assertContains(self.response, "Save Location")

    @tag("incorrect_html", "logged_in")
    def test_does_not_contain_incorrect_html_code_for_logged_in_user(self):
        self.assertNotContains(self.response, "Homepage")

    @tag("resolve", "url", "logged_in")
    def test_url_resolves_location_create_view_for_logged_in_user(self):
        view = resolve("/setup/locations/add/")
        self.assertEqual(
            view.func.__name__,
            LocationCreateView.as_view().__name__,
        )


@tag("updateview")
class LocationUpdateViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="TestUser",
            email="test@email.com",
            password="testpass123",
        )
        self.login = self.client.login(
            username="TestUser",
            password="testpass123",
        )
        self.new_location = Location.objects.create(
            location_id="002",
            location_name="2nd Location",
        )
        self.response = self.client.post(
            reverse(
                "setup:location_edit", kwargs={"pk": self.new_location.location_id}
            ),
            {
                "location_id": "002",
                "location_name": "2nd Test Location",
            },
        )

    @tag("status_code", "logged_in")
    def test_status_code_for_logged_in_user(self):
        self.assertEqual(self.response.status_code, 302)

    @tag("resolve", "url", "logged_in")
    def test_url_resolves_view_for_logged_in_user(self):
        view = resolve("/setup/locations/002/edit/")
        self.assertEqual(
            view.func.__name__,
            LocationUpdateView.as_view().__name__,
        )


@tag("deleteview")
class LocationDeleteViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="TestUser",
            email="test@email.com",
            password="testpass123",
        )
        self.login = self.client.login(
            username="TestUser",
            password="testpass123",
        )
        self.new_location = Location.objects.create(
            location_id="003",
            location_name="3rd Location",
        )
        self.location = Location.objects.create(
            location_id="002",
            location_name="2nd Location",
        )
        self.response = self.client.get(
            reverse("setup:location_delete", kwargs={"pk": self.location.location_id})
        )
        self.post_response = self.client.post(
            reverse("setup:location_delete", kwargs={"pk": self.location.location_id})
        )

    def test_contains_correct_html_for_logged_in_user(self):
        self.assertContains(self.response, "Are you sure you want to delete")

    def test_delete_confirmation_status_code_for_logged_in_user(self):
        self.assertEqual(self.response.status_code, 200)

    def test_delete_redirect_for_logged_in_user(self):
        self.assertRedirects(
            self.post_response, reverse("setup:location_list"), status_code=302
        )

    def test_template_used(self):
        self.assertTemplateUsed(
            self.response, "setup/locations/location_delete.html"
        )
