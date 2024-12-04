from typing import Any

import pytest

from datura.flatten_dict import flatten_dict


@pytest.mark.parametrize("data", [None, 1, "a", []])
def test_flatten_dict_invalid(data: Any) -> None:
    with pytest.raises(ValueError):
        flatten_dict(data)


@pytest.mark.parametrize(
    "value, expected",
    [
        ({}, {}),  # Empty value
        ({"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 2, "c": 3}),  # Simple example
        (  # Provided test case
            {"a": 1, "b": {"c": 2, "d": {"e": 3, "f": 4}}, "g": {"h": 5}},
            {"a": 1, "b.c": 2, "b.d.e": 3, "b.d.f": 4, "g.h": 5},
        ),
    ],
)
def test_flatten_dict_valid(value: dict, expected: dict) -> None:
    assert flatten_dict(value) == expected
