"""Hook into Alliance Auth"""

# Django
from django.utils.translation import gettext_lazy as _

# Alliance Auth
from allianceauth import hooks

from .views import dashboard_corptools_check


class CorptoolsDashboardHook(hooks.DashboardItemHook):
    def __init__(self):
        super().__init__(view_function=dashboard_corptools_check, order=5)


@hooks.register("dashboard_hook")
def register_corptools_hook():
    return CorptoolsDashboardHook()
