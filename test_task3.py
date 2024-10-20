"""Test code for task1.py
"""
import pytest
from task3 import tier_water_bill

# Test cases for simple_water_bill()
# Use pytest.mark.parametrize decorator to pass multiple test cases
# https://docs.pytest.org/en/stable/parametrize.html
# First element in the tuple is the input, second element is the
#  expected output
@pytest.mark.parametrize("gallons_usage, expected_output", [
    (100, "You used 100 gallons, your bill is $30.00\nTier1 (0-2000): 100 gallons,  $30.00\nTier2 (2001-5000): 0 gallons,  $0.00\nTier3 (more than 5000): 0 gallons,  $0.00\n"),
    (2000, "You used 2000 gallons, your bill is $30.00\nTier1 (0-2000): 2000 gallons,  $30.00\nTier2 (2001-5000): 0 gallons,  $0.00\nTier3 (more than 5000): 0 gallons,  $0.00\n"),
    (2001, "You used 2001 gallons, your bill is $30.08\nTier1 (0-2000): 2000 gallons,  $30.00\nTier2 (2001-5000): 1 gallons,  $0.08\nTier3 (more than 5000): 0 gallons,  $0.00\n"),
    (4520, "You used 4520 gallons, your bill is $231.60\nTier1 (0-2000): 2000 gallons,  $30.00\nTier2 (2001-5000): 2520 gallons,  $201.60\nTier3 (more than 5000): 0 gallons,  $0.00\n"),
    (5000, "You used 5000 gallons, your bill is $270.00\nTier1 (0-2000): 2000 gallons,  $30.00\nTier2 (2001-5000): 3000 gallons,  $240.00\nTier3 (more than 5000): 0 gallons,  $0.00\n"),
    (5020, "You used 5020 gallons, your bill is $274.00\nTier1 (0-2000): 2000 gallons,  $30.00\nTier2 (2001-5000): 3000 gallons,  $240.00\nTier3 (more than 5000): 20 gallons,  $4.00\n"),
])


def test_simple_water_bill(monkeypatch, capsys, gallons_usage, expected_output):
    monkeypatch.setattr('builtins.input', lambda _: str(gallons_usage))
    tier_water_bill()
    captured = capsys.readouterr()
    assert captured.out == expected_output
