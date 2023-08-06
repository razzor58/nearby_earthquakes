import pytest

from app.models import Coordinates, MaxInputAttemptsExceeded, ValidationError


def test_create_coordinates():
    coordinates = Coordinates(latitude=80, longitude=120)
    assert isinstance(coordinates, Coordinates)


def test_coordinates_point():
    coordinates = Coordinates(latitude=80, longitude=120)
    assert isinstance(coordinates.point, tuple)


@pytest.mark.parametrize(
    "latitude,longitude",
    [
        (-91, 120),
        (91, 120),
        (80, 200),
        (80, -200),
        (-100, -200),
    ],
)
def test_error_create_coordinates(latitude, longitude):
    with pytest.raises(ValidationError) as excinfo:
        _ = Coordinates(latitude=latitude, longitude=longitude)
    assert excinfo.value.title == "Coordinates"


@pytest.mark.parametrize("user_input", ["200"])
def test_too_many_inputs(monkeypatch, user_input):
    with pytest.raises(MaxInputAttemptsExceeded) as excinfo:
        monkeypatch.setattr("builtins.input", lambda _: user_input)
        _ = Coordinates.read_from_input()
    assert str(excinfo.value) == "Too many wrong inputs"


@pytest.mark.parametrize("user_input", ["80"])
def test_create_from_input(monkeypatch, user_input):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    coordinates = Coordinates.read_from_input()
    assert isinstance(coordinates, Coordinates)
