from . import rownania
import pytest


def test_dodaj():
    assert rownania.dodaj(5, 4) == 9


def test_dodaj_jeden_arg():
    assert rownania.dodaj(5) == 5


def test_dodaj_none():
    assert rownania.dodaj() == None


def test_dodaj_zero():
    assert rownania.dodaj(-5, 5) == 0


@pytest.mark.parametrize("liczba1, liczba2, wynik", [(5, 4, 9), (-5, 5, 0)])
def test_dodaj_kilka(liczba1, liczba2, wynik):
    assert rownania.dodaj(liczba1, liczba2) == wynik