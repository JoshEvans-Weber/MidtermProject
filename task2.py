"""
Calculate your water bill based on usage
"""

def simple_water_bill():
    """
    SIMPLE WATER BILL WITH BASE PRICE AND OVERUSE PRICES
    """
    BASEPRICE = 30.00
    PRICE = 0.08
    # Task 1: Basic Water Usage
    # Take user input for the number of gallons of water used in a household
    gallons_usage = int(input('How many gallons you used this month? '))

    # TODO: Calculate final charge
    # First 2000 gallons, basic rate: $30.00
    # Additional gallons after 2000 at $0.08 per gallon
    final_charge = 0
    overuse = 0
    '''Set working variables to zero'''
    if gallons_usage > 2000:
        overuse = gallons_usage - 2000
        '''Calculate over used water'''
    final_charge = BASEPRICE + (overuse * PRICE)
    '''calculate final price'''

    print(f'You used {gallons_usage} gallons, your bill is ${final_charge:.2f}')


if __name__ == '__main__':
    simple_water_bill()
