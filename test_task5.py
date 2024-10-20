"""Test code for task1.py
"""
import pytest
from task5 import tier_water_bill

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
    # Test case 1: 29370 gallons
    year_usage = [800, 900, 1500, 2000, 2050, 3000, 
                  3500, 4000, 4500, 5020, 1500, 600]
    testing = True
    tier_water_bill(year_usage)
    captured = capsys.readouterr()
    assert captured.out == expected_output


    