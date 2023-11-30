import json
import datetime

def read_json_file(file_path, meal='lunch'):
    """
    Reads a JSON file and returns today's menu for lunch or dinner 
    based on the current time.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: Today's menu for the specified meal time.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Get today's date in YYYY-MM-DD format
        today = datetime.date.today().strftime("%Y-%m-%d")

        # Check if today's date is in the JSON data
        if today in data:
            current_time = datetime.datetime.now().time()

            # Check if the current time is before or after 2 PM
            if current_time.hour < 14:  # Before 2 PM
                meal = 'Lunch'
            else:
                meal = 'Dinner'

            # Return today's menu for the specified meal
            return data[today].get(meal, {})

        else:
            print("No menu available for today.")
            return {}

    except Exception as e:
        print(f"Error reading the JSON file: {e}")
        return None

# Usage
file_path = 'json/merged.json'
json_content = read_json_file(file_path)
print(json_content)
