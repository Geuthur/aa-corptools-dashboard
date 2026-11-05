"""Generate Corptools CharacterAudit test objects."""

# Third Party
from corptools.models import CharacterAudit

# Alliance Auth
from allianceauth.eveonline.models import EveCharacter


def create_characteraudit(eve_character: EveCharacter, **kwargs) -> CharacterAudit:
    """Create a characteraudit object for the given character."""
    params = {"character": eve_character}
    params.update(kwargs)
    obj = CharacterAudit(**params)
    obj.save()
    return obj
