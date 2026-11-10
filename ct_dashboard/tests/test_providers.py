# AA Corptools Dashboard
from ct_dashboard import __title__
from ct_dashboard.providers import AppLogger, logger
from ct_dashboard.tests import NoSocketsTestCase


class TestAppLogger(NoSocketsTestCase):
    def test_logger_is_app_logger(self):
        """
        Test should provide the shared AppLogger with the app title as prefix.
        """
        self.assertIsInstance(logger, AppLogger)
        self.assertEqual(logger.prefix, __title__)
        self.assertEqual(logger.logger.name, "ct_dashboard.providers")

    def test_process_adds_prefix(self):
        """
        Test should prefix log messages with the app title.
        """
        msg, kwargs = logger.process("Hello World", {"extra": {"a": 1}})

        self.assertEqual(msg, f"[{__title__}] Hello World")
        self.assertEqual(kwargs, {"extra": {"a": 1}})
