def get_user_names(data:list, country:str) -> list:
    """
    Return a list of users with a given country

    Args:
        data (dict): A dictionary of values
        country (str): The country to search for
    Returns:
        list: A list of users with the given country
    """
    l = []
    for i in data:
        if i['country'] == country:
            l.append(i['name'])
    return l
data = [
  {
    'name': 'John', 
    'country': 'USA'
  }, 
  {
    'name': 'Mary', 
    'country': 'UK'
  },
  {
    'name': 'Henry', 
    'country': 'UK'
  },
  {
    'name': 'Sam', 
    'country': 'MEX'
  },
  {
    'name': 'Kevin', 
    'country': 'RUS'
  },
  {
    'name': 'Dustin', 
    'country': 'GER'
  }
]
print(get_user_names(data, 'UK'))