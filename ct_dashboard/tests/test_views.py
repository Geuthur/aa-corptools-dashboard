# Third Party
from evesde_factory.allianceauth import EveCharacterFactory
from evesde_factory.utils import add_character_to_user

# Django
from django.http import HttpResponse

# AA Corptools Dashboard
from ct_dashboard.tests import AuthTestCase
from ct_dashboard.tests.testdata.factory import UserMainFactory
from ct_dashboard.tests.testdata.load_characteraudit import create_characteraudit
from ct_dashboard.views import dashboard_corptools_check


class DashboardCorptoolsCheckTest(AuthTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user_without_permission = UserMainFactory(permissions=[])
        cls.user_with_ma_permission = UserMainFactory()
        for user in (cls.user_without_permission, cls.user_with_ma_permission):
            create_characteraudit(user.profile.main_character)

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
        add_character_to_user(self.user_with_ma_permission, EveCharacterFactory())
        add_character_to_user(self.user_with_ma_permission, EveCharacterFactory())
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
        add_character_to_user(self.user_with_ma_permission, EveCharacterFactory())

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
