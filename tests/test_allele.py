import pytest
from str_locus_parser.allele import (
    Allele,
    AlleleValueError,
    UnnamedAlleleWasFound,
    OFF_LADDER_VALUES,
)


def allele_created_by_valid_value():
    values = ["11", "11.3", "X", "Y", "SRY"]
    for value in values:
        assert Allele(value).value == value

def test_allele_raised_by_invalid_value():
    invalid_values = ["11/3", " 11.3", " "]
    for value in invalid_values:
        with pytest.raises(AlleleValueError):
            Allele(value)


def test_type_validator():
    with pytest.raises(TypeError):
        Allele._type_validator(11)


def test_value_validator():
    with pytest.raises(AlleleValueError):
        Allele("11/3")


def test_off_ladder_validator():
    with pytest.raises(UnnamedAlleleWasFound):
        for OL in OFF_LADDER_VALUES:
            Allele._off_ladder_validator(OL)


def test_prepare_value():
    assert Allele("11,3").value == "11.3"


def test_replace_commas():
    assert Allele._replace_commas("11,3") == "11.3"

