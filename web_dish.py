import requests
from bs4 import BeautifulSoup
import json
import datetime
import calendar


def update_dict(dicts, key, value):
    if key in dicts:
        # Append value if key exists
        if isinstance(dicts[key], list):
            dicts[key].append(value)
        else:
            dicts[key] = [dicts[key], value]
    else:
        # Create the key with the value
        dicts[key] = value


def fetch_menu(url, section_dish):
    response = requests.get(url)
    if response.status_code != 200:
        print('Failed to retrieve the webpage')
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tr elements that could contain sections or dishes
    tr_elements = soup.find_all('tr')

    current_section = None
    for tr in tr_elements:
        # Check if the tr element is a section
        if tr.div and 'shortmenucats' in tr.div.get('class', []):
            current_section = tr.div.text.strip().strip('-').strip()

        # Check if the tr element is a dish
        dish = tr.find('a', attrs={'name': 'Recipe_Desc'})
        if dish:
            print('Section:', current_section, 'Dish:', dish.text.strip())
            update_dict(section_dish, current_section, dish.text.strip())


def update_dict(dicts, key, value):
    if key in dicts:
        # Append value if key exists
        if isinstance(dicts[key], list):
            dicts[key].append(value)
        else:
            dicts[key] = [dicts[key], value]
    else:
        # Create the key with the value
        dicts[key] = value

def fetch_menu1(url, meal_section):
    response = requests.get(url)
    if response.status_code != 200:
        print('Failed to retrieve the webpage')
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    current_meal = None
    current_section = None

    # Find all meals and sections
    meals_and_sections = soup.find_all('div', class_=['shortmenumeals', 'shortmenucats'])

    print(meals_and_sections)
    # Process meals and sections
    for element in meals_and_sections:
        # print(element)
        if 'shortmenumeals' in element.get('class', []):
            current_meal = element.text.strip()
            # print('Meal:', current_meal)

        elif 'shortmenucats' in element.get('class', []):
            current_section = element.text.strip().strip('-').strip()
            # print('  Section:', current_section)
            update_dict(meal_section, current_meal, current_section)

def create_meal_structure(meal_to_sections, section_to_dishes, month = 11, day = 1):
    structured_data = {}

    for meal, sections in meal_to_sections.items():
        structured_data[meal] = {}
        for section in sections:
            # Get dishes for each section from section_to_dishes dict, use set to avoid duplicates
            dishes = set(section_to_dishes.get(section, []))
            structured_data[meal][section] = list(dishes)

    # Writing to a JSON file
    file_name = str(month) + '_' + str(day) + '.' + 'json'
    with open(file_name, 'w') as file:
        json.dump(structured_data, file, indent=4)

    print("Meal structure written to 'meal_structure.json'")



def generate_ucr_dining_urls(month, year=2023):
    """
    Generates URLs for the UCR dining services menu for each day in the specified month.

    Args:
    month (int): The month for which URLs are to be generated.
    year (int, optional): The year for which URLs are to be generated. Defaults to 2023.

    Returns:
    list: A list of URLs for each day of the specified month.
    """
    base_url = "https://foodpro.ucr.edu/foodpro/shortmenu.asp?sName=University+of+California%2C+Riverside+Dining+Services&locationNum=03&locationName=Glasgow&naFlag=1&WeeksMenus=This+Week%27s+Menus&myaction=read&dtdate="
    urls = []

    # Calculate the number of days in the specified month
    _, num_days = calendar.monthrange(year, month)

    # Generate URLs for each day of the month
    for day in range(1, num_days + 1):
        date_str = f"{month}/{day}/{year}"
        full_url = base_url + date_str
        urls.append(full_url)

    return urls

# Example usage
urls_november = generate_ucr_dining_urls(11)  # URLs for November
urls_december = generate_ucr_dining_urls(12)  # URLs for December

date_str = []
for i in range(len(urls_november)):
    url = urls_november[i]
    section_dish = {}
    meal_section = {}
    # urls_november[:5], urls_december[:5]  # Display the first 5 URLs for each month
    fetch_menu(url, section_dish)
    fetch_menu1(url, meal_section)
    create_meal_structure(meal_section, section_dish, 11, i + 1)
 

