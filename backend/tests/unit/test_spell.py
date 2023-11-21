import pytest
from domain.spell import Spell
from domain.SPELLS import SPELLS


def test_init():
    spell = Spell("Magic No1")
    assert spell.name == "Magic No1"


def test_get_method_name():
    spell = Spell("Magic 1")
    method_name = spell._Spell__get_method_name()
    assert method_name == "cast_magic_1"


@pytest.mark.parametrize("spell_name,expected_value", SPELLS.items())
def test_get_value(spell_name, expected_value):
    spell = Spell(spell_name)
    value = spell.get_value()
    assert value == expected_value


def test_valid_spell_name():
    spell = Spell("Magic 1")
    assert spell.valid_spell_name() is True

    spell = Spell("unknown")
    assert spell.valid_spell_name() is False
