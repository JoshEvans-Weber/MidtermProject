"""Test code for task1.py
"""
import pytest
from task4 import tier_water_bill

# Test cases for simple_water_bill()
# Use pytest.mark.parametrize decorator to pass multiple test cases
# https://docs.pytest.org/en/stable/parametrize.html
# First element in the tuple is the input, second element is the
#  expected output
@pytest.mark.parametrize("expected_output", [
    ('''You used 29370 gallons, your bill is $1168.00
Tier1 (0-2000): 19300 gallons,  $360.00
Tier2 (2001-5000): 10050 gallons,  $804.00
Tier3 (more than 5001): 20 gallons,  $4.00\n'''),
])


def test_simple_water_bill(monkeypatch, capsys, expected_output):
    tier_water_bill()
    captured = capsys.readouterr()
    assert captured.out == expected_output
