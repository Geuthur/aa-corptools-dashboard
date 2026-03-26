"""Generate AllianceAuth test objects from allianceauth.json."""

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


def load_characteraudit():
    CharacterAudit.objects.all().delete()
    create_characteraudit(EveCharacter.objects.get(character_id=1001))
    create_characteraudit(EveCharacter.objects.get(character_id=1002))
    create_characteraudit(EveCharacter.objects.get(character_id=1003))
