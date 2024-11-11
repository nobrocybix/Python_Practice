
def two_die_multiply(die_1, die_2, roll_nums=1000):                                                
    # Make some rolls, and store results in a list.
    results = []
    for roll_num in range(roll_nums):
        result = die_1.roll() * die_2.roll()
        results.append(result)
        
    num_result = two_die_num_result(die_1, die_2)
            
    # Analyze the results.
    frequencies = []
    for value in num_result:
        frequency = results.count(value)
        frequencies.append(frequency)
    
    return frequencies

def two_die_num_result(die_1, die_2):
    ''' Look for possible results'''
    num_result = set()
    for n_die_1 in range(1, die_1.num_sides + 1):
        for n_die_2 in range(1, die_2.num_sides + 1):
            num_result.add(n_die_1 * n_die_2)
    num_result = sorted(num_result)

    return num_result