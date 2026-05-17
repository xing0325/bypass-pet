from __future__ import annotations

import pytest

from bypass_pet.state import SentinelState


@pytest.fixture
def sentinel(tmp_path):
    return SentinelState(tmp_path / "subdir" / ".bypass-on")


def test_initial_state_is_accept_when_file_missing(sentinel):
    assert sentinel.current() == "accept"
    assert not sentinel.path.exists()


def test_toggle_creates_file_and_returns_bypass(sentinel):
    assert sentinel.toggle() == "bypass"
    assert sentinel.path.exists()
    assert sentinel.current() == "bypass"


def test_toggle_round_trip(sentinel):
    assert sentinel.toggle() == "bypass"
    assert sentinel.toggle() == "accept"
    assert not sentinel.path.exists()
    assert sentinel.current() == "accept"


def test_set_to_bypass_is_idempotent(sentinel):
    sentinel.set("bypass")
    sentinel.set("bypass")
    assert sentinel.current() == "bypass"


def test_set_to_accept_is_idempotent_even_if_file_missing(sentinel):
    sentinel.set("accept")
    sentinel.set("accept")
    assert sentinel.current() == "accept"
    assert not sentinel.path.exists()


def test_set_creates_parent_directories(sentinel):
    assert not sentinel.path.parent.exists()
    sentinel.set("bypass")
    assert sentinel.path.parent.is_dir()
    assert sentinel.path.is_file()


def test_set_rejects_unknown_state(sentinel):
    with pytest.raises(ValueError):
        sentinel.set("wat")  # type: ignore[arg-type]
