from django.test import TestCase, tag
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from setup.views import (
    EmailLicenseListView,
    EmailLicenseCreateView,
)
from setup.models import EmailLicense


@tag("listview")
class EmailLicenseListViewTests(TestCase):
    def setUp(self):
        url = reverse("setup:email_license_list")
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(
            self.response, "setup/email_licenses/email_license_list.html"
        )

    def test_contains_correct_html(self):
        self.assertContains(self.response, "Add License")

    def test_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Homepage")

    def test_url_resolves_correct_view(self):
        view = resolve("/setup/licenses/")
        self.assertEqual(
            view.func.__name__,
            EmailLicenseListView.as_view().__name__,
        )


@tag("createview")
class EmailLicenseCreateView(TestCase):
    def setUp(self):
        self.post_response = self.client.post(
            reverse("setup:email_license_add"),
            {"license_id": "A1", "license_price": 10},
        )
        self.response = self.client.get(reverse("setup:email_license_add"))

    def test_email_license_creation(self):
        self.assertEqual(EmailLicense.objects.last().license_id, "A1")
        self.assertEqual(EmailLicense.objects.last().license_price, 10)

    def test_template_used(self):
        self.assertTemplateUsed(
            self.response, "setup/email_licenses/email_license_add.html"
        )
