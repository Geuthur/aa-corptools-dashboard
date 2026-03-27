# Third Party
from corptools.app_settings import CORPTOOLS_APP_NAME
from corptools.models import CharacterAudit

# Django
from django.template.loader import render_to_string
from django.utils.html import format_html
from django.utils.translation import gettext as _

# Alliance Auth
from allianceauth.authentication.models import CharacterOwnership
from allianceauth.services.hooks import get_extension_logger

logger = get_extension_logger(__name__)


def dashboard_corptools_check(request):
    known_characters = CharacterOwnership.objects.filter(user=request.user)
    known_character_ids = known_characters.values_list(
        "character__character_id", flat=True
    )
    characters = CharacterAudit.objects.filter(
        character__character_id__in=known_character_ids
    )
    character_ids = characters.values_list("character__character_id", flat=True)

    characters_with_issues: list[CharacterAudit] = []
    # Check if characters are active this will trigger the is_active function which will check if the character is active and update the last_active field in the database, if there is an issue with the character it will be marked as inactive and show a warning in the dashboard
    for character in characters:
        if not character.is_active():
            characters_with_issues.append(character)

    unregistered_characters = known_characters.exclude(
        character__character_id__in=character_ids
    )

    chars = {}

    if characters:
        for char in unregistered_characters:
            title = _("Character Registration Issue")
            msg = f"<span class='text-danger'><i class='fas fa-times-circle' data-bs-tooltip='aa-corptools-dashboard' title='{title}'></i></span>"
            chars[char.character.character_id] = {
                "id": char.character.character_id,
                "name": char.character.character_name,
                "issues": _(
                    "Character is not registered in {corptools_app_name}."
                ).format(corptools_app_name=CORPTOOLS_APP_NAME),
                "icon": format_html(msg),
            }

    if characters_with_issues:
        for issue in characters_with_issues:
            title = _("Character Update Issue")
            msg = f"<span class='text-warning'><i class='fas fa-triangle-exclamation' data-bs-tooltip='aa-corptools-dashboard' title='{title}'></i></span>"
            chars[issue.character.character_id] = {
                "id": issue.character.character_id,
                "name": issue.character.character_name,
                "issues": _(
                    "Please re-register this character, as there was an issue with the last update."
                ),
                "icon": format_html(msg),
            }

    context = {
        "chars": chars if chars else None,
        "corptools_app_name": CORPTOOLS_APP_NAME,
    }
    return render_to_string(
        template_name="ct_dashboard/dashboard.html", context=context, request=request
    )
