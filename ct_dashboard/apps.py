"""App Configuration"""

# Django
from django.apps import AppConfig

# AA Corptools Dashboard
from ct_dashboard import __version__


class CTDashboardConfig(AppConfig):
    """App Config"""

    default_auto_field = "django.db.models.AutoField"
    name = "ct_dashboard"
    label = "ct_dashboard"
    verbose_name = f"Corptools Dashboard v{__version__}"
