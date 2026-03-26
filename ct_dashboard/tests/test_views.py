# Django
from django.http import HttpResponse
from django.test import RequestFactory, TestCase

# Alliance Auth
from allianceauth.eveonline.models import EveCharacter

# AA Corptools Dashboard
from ct_dashboard.tests.testdata.load_allianceauth import load_allianceauth
from ct_dashboard.tests.testdata.load_characteraudit import load_characteraudit
from ct_dashboard.tests.testdata.utils import (
    add_character_to_user,
    create_user_from_evecharacter,
)
from ct_dashboard.views import dashboard_corptools_check


class DashboardCorptoolsCheckTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        load_allianceauth()
        load_characteraudit()
        cls.factory = RequestFactory()
        cls.user_without_permission, cls.character_ownership = (
            create_user_from_evecharacter(character_id=1002)
        )
        cls.user_with_ma_permission, cls.character_ownership = (
            create_user_from_evecharacter(
                character_id=1001,
                permissions=["corptools.view_characteraudit"],
            )
        )

    def test_dashboard_corptools_check_user_with_ct_permission(self):
        # given
        request = self.factory.get("/")
        request.user = self.user_with_ma_permission
        # when
        response = dashboard_corptools_check(request)
        # Convert SafeString to HttpResponse for testing
        response = HttpResponse(response)
        # then
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            '<div id="corptools-check-dashboard-widget" class="col-12 mb-3">',
            response.content.decode("utf-8"),
        )

    def test_dashboard_corptools_check_user_without_permission(self):
        # given
        request = self.factory.get("/")
        request.user = self.user_without_permission
        # when
        response = dashboard_corptools_check(request)
        # Convert SafeString to HttpResponse for testing
        response = HttpResponse(response)
        # then
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(
            '<div id="corptools-check-dashboard-widget" class="col-12 mb-3">',
            response.content.decode("utf-8"),
        )

    def test_dashboard_corptools_check_many(self):
        # given
        add_character_to_user(
            self.user_with_ma_permission, EveCharacter.objects.get(character_id=1006)
        )
        add_character_to_user(
            self.user_with_ma_permission, EveCharacter.objects.get(character_id=1007)
        )
        request = self.factory.get("/")
        request.user = self.user_with_ma_permission
        # when
        response = dashboard_corptools_check(request)
        # Convert SafeString to HttpResponse for testing
        response = HttpResponse(response)
        # then
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            '<div id="corptools-check-dashboard-widget" class="col-12 mb-3">',
            response.content.decode("utf-8"),
        )

    def test_dashboard_corptools_check_character_update_issues(self):
        # given
        request = self.factory.get("/")
        request.user = self.user_with_ma_permission
        # when
        response = dashboard_corptools_check(request)
        # Convert SafeString to HttpResponse for testing
        response = HttpResponse(response)
        # then
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            '<div id="corptools-check-dashboard-widget" class="col-12 mb-3">',
            response.content.decode("utf-8"),
        )
        # Check that the character update issue icon is present
        self.assertIn(
            "<i class='fas fa-triangle-exclamation'",
            response.content.decode("utf-8"),
        )
        # Check that the issue message is present
        self.assertIn(
            "Please re-register this character, as there was an issue with the last update.",
            response.content.decode("utf-8"),
        )

    def test_dashboard_corptools_check_character_both_unregistered_and_issues(self):
        # given
        # Add an unregistered character (character without corptools record)
        add_character_to_user(
            self.user_with_ma_permission, EveCharacter.objects.get(character_id=1006)
        )

        request = self.factory.get("/")
        request.user = self.user_with_ma_permission
        # when
        response = dashboard_corptools_check(request)
        # Convert SafeString to HttpResponse for testing
        response = HttpResponse(response)
        # then
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            '<div id="corptools-check-dashboard-widget" class="col-12 mb-3">',
            response.content.decode("utf-8"),
        )
        # Check that both icons are present (registration issue and update issue)
        self.assertIn(
            "<i class='fas fa-times-circle'",
            response.content.decode("utf-8"),
        )
        self.assertIn(
            "<i class='fas fa-triangle-exclamation'",
            response.content.decode("utf-8"),
        )
