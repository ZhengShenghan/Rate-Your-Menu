import requests
from bs4 import BeautifulSoup
import json

section_dish = {}
meal_section = {}

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


def fetch_menu(url):
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

def fetch_menu1(url):
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

def create_meal_structure(meal_to_sections, section_to_dishes):
    structured_data = {}

    for meal, sections in meal_to_sections.items():
        structured_data[meal] = {}
        for section in sections:
            # Get dishes for each section from section_to_dishes dict, use set to avoid duplicates
            dishes = set(section_to_dishes.get(section, []))
            structured_data[meal][section] = list(dishes)

    # Writing to a JSON file
    with open('meal_structure.json', 'w') as file:
        json.dump(structured_data, file, indent=4)

    print("Meal structure written to 'meal_structure.json'")

url = 'https://foodpro.ucr.edu/foodpro/shortmenu.asp?sName=University%20of%20California%2C%20Riverside%20Dining%20Services&locationNum=03&locationName=Glasgow&naFlag=1'
fetch_menu(url)

# print(section_dish)

fetch_menu1(url)

# print(meal_section)

create_meal_structure(meal_section, section_dish)
