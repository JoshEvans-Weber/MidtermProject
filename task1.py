"""
Calculate your water bill based on usage
"""


def simple_water_bill():
    """
    Simple water bill function
    """

    PRICE = 0.08
    # Task 1: Basic Water Usage
    # Take user input for the number of gallons of water used in a household at $0.08 per gallon
    gallons_usage = int(input('How many gallons you used this month? '))

    # TODO: Calculate final charge
    final_charge = 0
    final_charge = gallons_usage * PRICE
    
    print(f'You used {gallons_usage} gallons, your bill is ${final_charge:.2f}')


if __name__ == '__main__':
    simple_water_bill()
