def get_max_age_user_name(data:list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """
    l = []
    for i in data:
        if type(i['age']) == int:
          l.append(i['age'])
    return max(l)
