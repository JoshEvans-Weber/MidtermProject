"""Test code for task1.py
"""
import pytest
from task1 import simple_water_bill

# Test cases for simple_water_bill()
# Use pytest.mark.parametrize decorator to pass multiple test cases
# https://docs.pytest.org/en/stable/parametrize.html
# First element in the tuple is the input, second element is the
#  expected output
@pytest.mark.parametrize("gallons_usage, expected_output", [
    (100, "You used 100 gallons, your bill is $8.00\n"),
    (200, "You used 200 gallons, your bill is $16.00\n"),
    (2500, "You used 2500 gallons, your bill is $200.00\n"),
    (3214, "You used 3214 gallons, your bill is $257.12\n"),
])


def test_simple_water_bill(monkeypatch, capsys, gallons_usage, expected_output):
    monkeypatch.setattr('builtins.input', lambda _: str(gallons_usage))
    simple_water_bill()
    captured = capsys.readouterr()
    assert captured.out == expected_output
