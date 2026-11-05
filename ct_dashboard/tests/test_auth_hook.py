# Standard Library
from unittest.mock import MagicMock

# Django
from django.http import HttpResponse
from django.test import RequestFactory, TestCase

# AA Corptools Dashboard
from ct_dashboard.auth_hooks import CorptoolsDashboardHook, register_corptools_hook
from ct_dashboard.tests.testdata.factory import UserMainFactory
from ct_dashboard.tests.testdata.load_characteraudit import create_characteraudit


class TestCorptoolsDashboardAuthHooks(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.factory = RequestFactory()
        cls.user_without_permission = UserMainFactory(permissions=[])
        cls.user_with_ct_permission = UserMainFactory()
        for user in (cls.user_without_permission, cls.user_with_ct_permission):
            create_characteraudit(user.profile.main_character)

    def test_render_returns_empty_string_for_user_without_permission(self):
        # given
        request = self.factory.get("/")
        request.user = self.user_without_permission
        rendered_item = CorptoolsDashboardHook()

        # when
        response = rendered_item.render(request)
        # Convert SafeString to HttpResponse for testing
        response = HttpResponse(response)
        # then
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(
            '<div id="corptools-check-dashboard-widget" class="col-12 mb-3">',
            response.content.decode("utf-8"),
        )

    def test_render_returns_widget_for_user_with_permission(self):
        # given
        request = self.factory.get("/")
        request.user = self.user_with_ct_permission
        rendered_item = CorptoolsDashboardHook()

        # when
        response = rendered_item.render(request)
        # Convert SafeString to HttpResponse for testing
        response = HttpResponse(response)
        # then
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            '<div id="corptools-check-dashboard-widget" class="col-12 mb-3">',
            response.content.decode("utf-8"),
        )

    def test_register_corptools_hook(self):
        # given
        hooks = register_corptools_hook()

        # then
        self.assertIsInstance(hooks, CorptoolsDashboardHook)
