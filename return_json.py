import json

def read_json_file(file_path):
    """
    Reads a JSON file and returns its contents.

    Args:
    file_path (str): The path to the JSON file.

    Returns:
    dict: The contents of the JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading the JSON file: {e}")
        return None
file_path = 'json/merged.json'
json_content = read_json_file(file_path)
print(json_content)