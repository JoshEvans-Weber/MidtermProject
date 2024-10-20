"""
Calculate your water bill based on tier pricing
"""
def gal_tier1(gallons_usage):
    '''TIER 1 USAGE: upto 2000'''
    gallons_tier1 = 0
    TIER1UPPER = 2000
    gallons_tier1 = gallons_usage

    if gallons_tier1 > TIER1UPPER:
        gallons_tier1 = TIER1UPPER
    
    return gallons_tier1

def gal_tier2(gallons_usage):
    '''TIER 2 USAGE: between 2001 and 5000 gallons'''
    TIER2UPPER = 5000
    TIER2LOW = 2000
    gallons_tier2 = 0

    if gallons_usage == 5000:
        gallons_tier2 = 3000
    
    if gallons_usage != 5000:
        
        if gallons_usage > TIER2UPPER:
            gallons_tier2 = (TIER2UPPER - TIER2LOW)

        if gallons_usage > TIER2LOW and gallons_usage < TIER2UPPER:
            gallons_tier2 = (gallons_usage - TIER2LOW)
        
    return gallons_tier2

def gal_tier3(gallons_usage):
    ''''TIER 3 USAGE: anything over 5000'''
    gallons_tier3 = 0
    if gallons_usage > 5000:
        gallons_tier3 = gallons_usage - 5000
    
    return gallons_tier3


def tier1(gallons_usage):
    ''' TIER 1: upto 2000 gallons; PRICE for this tier is 30$ flat rate'''
    BASE_PRICE = 30.00
    if gallons_usage >= 1:
        charge_tier1 = BASE_PRICE
        return charge_tier1
    
def tier2(gallons_tier2):
    ''' TIER 2: PRICE for this range is $0.08 per gallon'''

    PRICE = 0.08
    charge_tier2 = gallons_tier2 * PRICE
    return charge_tier2

def tier3(gallons_tier3):
    ''' TIER 3: more than 5000 gallons; PRICE for this range is $0.20 per gallon'''
    MAX_PRICE = 0.20

    charge_tier3 = gallons_tier3 * MAX_PRICE
    return charge_tier3

def final(cost_tier1, cost_tier2, cost_tier3):
    final_charge = cost_tier1 + cost_tier2 + cost_tier3
    return final_charge



def tier_water_bill():
    """
    Tier system to calculate the final bill
    """
    year_usage = [800, 900, 1500, 2000, 2050, 3000, 
                  3500, 4000, 4500, 5020, 1500, 600]
    charges = {'tier1': 0.0, 'tier2': 0.0, 'tier3': 0.0}
    gallons = {'tier1': 0, 'tier2': 0, 'tier3': 0}
    gallons_usage = 0
    for num in year_usage:
        gallons_usage = num
        gallons_tier1 = gal_tier1(gallons_usage)
        gallons_tier2 = gal_tier2(gallons_usage)
        gallons_tier3 = gal_tier3(gallons_usage)
        cost_tier1 = tier1(gallons_usage)
        cost_tier2 = tier2(gallons_tier2)
        cost_tier3 = tier3(gallons_tier3)
        
        gallons['tier1'] += gallons_tier1
        charges['tier1'] += cost_tier1
        
        gallons['tier2'] += gallons_tier2
        charges['tier2'] += cost_tier2
        
        gallons['tier3'] += gallons_tier3
        charges['tier3'] += cost_tier3



    charges['final'] = final(charges['tier1'], charges['tier2'], charges['tier3'])
    gallons['final'] = final(gallons['tier1'], gallons['tier2'], gallons['tier3'])

    print(f"You used {gallons['final']} gallons, your bill is ${charges['final']:.2f}")
    print(f"Tier1 (0-2000): {gallons['tier1']} gallons,  ${charges['tier1']:.2f}")
    print(f"Tier2 (2001-5000): {gallons['tier2']} gallons,  ${charges['tier2']:.2f}")
    print(f"Tier3 (more than 5001): {gallons['tier3']} gallons,  ${charges['tier3']:.2f}")



if __name__ == '__main__':
    tier_water_bill()
