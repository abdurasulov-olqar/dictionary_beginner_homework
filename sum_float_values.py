def sum_float_values(data: dict) -> float:
    '''
    Return the sum of all float values in dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        float: The sum of all float values in the dictionary.
    '''
    d = (data.values())
    s = 0
    for i in d:
        if type(i) == float:
            s += i
    return s
