def get_tiers(tier_range_data, test):
    """
    Get tier limits from user input
    """
    tier1 = False
    tier2 = False

    while test == False: 
        #First Tier max limit
        try:
            while tier1 == False:
                tier_range_data['tier1'] = float(input('''Please input the value for the first tier's limit:  '''))
                tier1 = True
                if float(tier_range_data['tier1']) < 0:
                    tier1 = False
                    print('Invalid input: input must be non-negative')

        except ValueError:
            print('invalid input: expecting a number')
            tier1 = False
        #Second Tier max limit
        try:
            test = False
            while tier2 == False:
                tier_range_data['tier2'] = float(input('''Please input the value for the second tier's limit:   '''))
                tier_range_data['tier2bottom'] = tier_range_data['tier1'] + 1
                tier2 = True
                if float(tier_range_data['tier2']) < 0:
                    tier2 = False
                    print('Invalid input: input must be non-negative')
                if float(tier_range_data['tier2']) <= float(tier_range_data['tier1']):
                         print("Tier's cannot be smaller than the next, please try again")
                         tier2 = False

        except ValueError:
            print('invalid input: expecting a number')
        #Third tier working number

        tier_range_data['tier3'] = float(tier_range_data['tier2']) + 1
        test = True
        print(f'''By selecting {tier_range_data['tier2']} for tier two, tier three is : {tier_range_data['tier3']} and above  ''')
        if tier_range_data['tier1'] == 0 or tier_range_data['tier2'] == 0:
            test = False
    return tier_range_data

def get_costs(tier_price_structure, test):
    '''
    Get user input for tier costs
    '''
    
    tier1 = False
    tier2 = False
    tier3 = False
    negative_error = ValueError('numbers need to be non negative. try again.')
    while test == False: 
        #Base rate costs
        while tier1 == False:
            try:
                tier_price_structure['tier1'] = float(input('''Please input the first tier's flat rate price:    '''))
                tier1 = True
            except ValueError:
                print('invalid input: expecting a number')
            
        #First per gallon cost
        while tier2 == False:
            try:
                tier_price_structure['tier2'] = float(input('''Please input the second tier's price per gallon:    '''))
                tier2 = True
            except ValueError:
                print('invalid input: expecting a number')
        #Second cost for excessive gallon use
        while tier3 == False:
            try:
                tier_price_structure['tier3'] = float(input('''Please input the third tier's price per gallon:    '''))
                tier3 = True
            except ValueError:
                print('invalid input: expecting a number')
        if tier_price_structure['tier1'] < 0 or tier_price_structure['tier2'] < 0 or tier_price_structure['tier3'] < 0 :
            print(negative_error)
            tier1 = False
            tier2 = False
            tier3 = False
            test = False

        else:
            test = True

    return tier_price_structure

def gal_tier1(gallons_usage, tier_range_data):
    '''TIER 1 USAGE: Define the max value for tier1 usage'''
    gallons_tier1 = gallons_usage

    if gallons_tier1 > int(tier_range_data['tier1']):
        gallons_tier1 = int(tier_range_data['tier1'])
    
    return gallons_tier1

def gal_tier2(gallons_usage, tier_range_data):
    '''TIER 2 USAGE: between tier1 max + 1 and tier 2 max gallons'''

    gallons_tier2 = 0

    if gallons_usage == tier_range_data['tier3']:
        gallons_tier2 = int(tier_range_data['tier3']) - int(tier_range_data['tier1'])
    
    if gallons_usage != int(tier_range_data['tier3']):
        
        if gallons_usage > int(tier_range_data['tier3'] - 1):
            gallons_tier2 = (int(tier_range_data['tier3'] - 1) - int(tier_range_data['tier1']))

        if gallons_usage > int(tier_range_data['tier1']) and gallons_usage < int(tier_range_data['tier3'] - 1):
            gallons_tier2 = (gallons_usage - int(tier_range_data['tier1']))
        
    return gallons_tier2

def gal_tier3(gallons_usage, tier_range_data):
    ''''TIER 3 USAGE: anything higher than tier 2 max'''
    gallons_tier3 = 0
    if gallons_usage > int(tier_range_data['tier3']):
        gallons_tier3 = gallons_usage - (int(tier_range_data['tier3']-1))
    
    return gallons_tier3

def tier1(gallons_usage, tier_price_structure):
    ''' TIER 1: PRICE for this tier is USER SPECIFIED flat rate'''
    if gallons_usage >= 1:
        charge_tier1 = float(tier_price_structure['tier1'])
        return charge_tier1
    
def tier2(gallons_tier2, tier_price_structure):
    ''' TIER 2: PRICE for this range is USER SPECIFIED per gallon'''

    charge_tier2 = gallons_tier2 * float(tier_price_structure['tier2'])
    return charge_tier2

def tier3(gallons_tier3, tier_price_structure):
    ''' TIER 3: PRICE for this range is USER SPECIFIED per gallon'''

    charge_tier3 = gallons_tier3 * float(tier_price_structure['tier3'])
    return charge_tier3

def final(a,b,c):
    '''Calculate the final cost by adding the 3 tier's costs together'''
    
    final_charge = a + b + c
    return final_charge

def calculate_bill(tier_price_structure, tier_range_data, year_usage):
    '''Calculate the bill and launch print_statement'''
    
    charges = {'tier1': 0.0, 'tier2': 0.0, 'tier3': 0.0}
    gallons = {'tier1': 0, 'tier2': 0, 'tier3': 0}
    gallons_usage = 0
    for num in year_usage:
        gallons_usage = num
        gallons_tier1 = gal_tier1(gallons_usage, tier_range_data)
        gallons_tier2 = gal_tier2(gallons_usage, tier_range_data)
        gallons_tier3 = gal_tier3(gallons_usage, tier_range_data)
        cost_tier1 = tier1(gallons_usage, tier_price_structure)
        cost_tier2 = tier2(gallons_tier2, tier_price_structure)
        cost_tier3 = tier3(gallons_tier3, tier_price_structure)
        
        gallons['tier1'] += gallons_tier1
        charges['tier1'] += cost_tier1
        
        gallons['tier2'] += gallons_tier2
        charges['tier2'] += cost_tier2
        
        gallons['tier3'] += gallons_tier3
        charges['tier3'] += cost_tier3

    charges['final'] = final(charges['tier1'], charges['tier2'], charges['tier3'])
    gallons['final'] = final(gallons['tier1'], gallons['tier2'], gallons['tier3'])

    print_statement(gallons, charges, tier_range_data)
    contCheck()

def print_statement(gallons, charges, tier_range_data):
    '''Structured statement for final output to program before loop repeats'''

    print(f"You used {gallons['final']} gallons, your bill is ${charges['final']:.2f}")
    print(f"Tier1 (0-{tier_range_data['tier1']}): {gallons['tier1']} gallons,  ${charges['tier1']:.2f}")
    print(f"Tier2 ({int(tier_range_data['tier1'])+1}-{tier_range_data['tier2']}): {gallons['tier2']} gallons,  ${charges['tier2']:.2f}")
    print(f"Tier3 (more than {int(tier_range_data['tier2']) + 1}): {gallons['tier3']} gallons,  ${charges['tier3']:.2f}")
    
def menu(tier_range_data, tier_price_structure, year_usage):
    '''Interactive menu to custom user experience'''
    
    test = False
    while test == False:
        the_menu = f'''      
Current Tier Structure
Tier 1: 0 to {tier_range_data['tier1']}
Tier 2  {tier_range_data['tier2bottom']} to {tier_range_data['tier2']}
Tier 3  {tier_range_data['tier3']} and higher

Prices Per Tier
Tier1: ${tier_price_structure['tier1']:.2f} flat rate
Tier2: ${tier_price_structure['tier2']:.2f} per gallon
Tier3: ${tier_price_structure['tier3']:.2f} per gallon

What would you like to do?

1: Adjust prices
2: Adjust Tier limits
3: View water usage for the year

C: Continue to calculate the water bill
Q: Exit program'''

        print(the_menu)
        menu_nav = str(input())
        if menu_nav == 'q' or menu_nav == 'Q':
            goto_quit()
        if menu_nav == 'c' or menu_nav == 'C':
            calculate_bill(tier_price_structure, tier_range_data, year_usage)
        if menu_nav == '1':
            tier_price_structure = get_costs(tier_price_structure, test)
        if menu_nav == '2':
            tier_range_data = get_tiers(tier_range_data, test)
        if menu_nav == '3':
            printUsage(year_usage)
        else:
            test = False

def contCheck():
    '''Continue function'''
    cont = False
    while cont == False:
        choice = input('(C)ontinue or (E)xit ')
        if choice == 'c' or choice == 'C':
            cont = True
            break
        if choice == 'e' or choice == 'E':
            goto_quit()
        else:
            cont = False
            
def goto_quit():
    '''function to initiate quitting the program'''
    print('Exiting Program')
    exit()
     
def tier_water_bill(year_usage):
    """
    Welcome to program, initiate dictionaries and launch menu
    """
    print('Welcome to the Water Bill Calculator.')
    
    tier_price_structure = {'tier1': 0, 'tier2': 0, 'tier3' : 0}
    tier_range_data = {'tier1': 0, 'tier2': 0, 'tier2bottom': 0, 'tier3' : 0}

    menu(tier_range_data, tier_price_structure, year_usage)
    
def printUsage(year_usage):
    print(f'''
          Usage for the year was:
            Jan: {year_usage[0]} gallons.
            Feb: {year_usage[1]} gallons.
            Mar: {year_usage[2]} gallons.
            Apr: {year_usage[3]} gallons.
            May: {year_usage[4]} gallons.
            Jun: {year_usage[5]} gallons.
            Jul: {year_usage[6]} gallons.
            Aug: {year_usage[7]} gallons.
            Sep: {year_usage[8]} gallons.
            Oct: {year_usage[9]} gallons.
            Nov: {year_usage[10]} gallons.
            Dec: {year_usage[11]} gallons.
            ''')
    contCheck()

if __name__ == '__main__':
    # Test case 1: 29370 gallons
    year_usage = [800, 900, 1500, 2000, 2050, 3000, 
                  3500, 4000, 4500, 5020, 1500, 600]
    tier_water_bill(year_usage)