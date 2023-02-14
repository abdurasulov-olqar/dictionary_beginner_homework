def sum_even_values(data: dict) -> int:
    '''
    Return the sum of all even values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all even values in the dictionary
    '''
    d = (data.values())
    s = 0
    for i in d:
        if i%2 == 0:
            s += i
    return s
