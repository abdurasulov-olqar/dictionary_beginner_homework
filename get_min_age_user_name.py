def get_min_age_user_name(data:list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """
    l = []
    name = []
    for i in data:
        if type(i['age']) == int:
          l.append(i['age'])
          name.append(i['name'])
          
    return name[l.index(min(l))]