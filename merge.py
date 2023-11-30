# import os
# import json

# if not os.path.exists('json'):
#    os.makedirs('json')

# def merge_json_files(directory, output_file, year=2023):
#     merged_data = {}

#     for filename in os.listdir(directory):
#         if filename.endswith('.json'):
#             month_day = filename.split('.')[0]
#             print(month_day)
#             month, day = map(int, month_day.split('_'))
#             date_str = f"{year}-{month:02d}-{day:02d}"

#             with open(os.path.join(directory, filename), 'r') as file:
#                 data = json.load(file)

#             # Instead of adding 'date' to each entry, use the date as a key
#             # and assign all data from the file to this key
#             merged_data[date_str] = data

#     with open(output_file, 'w') as file:
#         json.dump(merged_data, file, indent=4)

# # Example usage
# # Assuming the current directory is the desired location for the output file
# current_directory = os.getcwd()
# output_file_path = os.path.join(current_directory, 'json', 'merged.json')
# merge_json_files(current_directory, output_file_path)

import os
import json

if not os.path.exists('json'):
   os.makedirs('json')

def merge_json_files(directory, output_file, year=2023):
    merged_data = {}

    # Load existing data from merged.json if it exists
    if os.path.exists(output_file):
        with open(output_file, 'r') as file:
            merged_data = json.load(file)
        # print(merged_data)
        # print('2023-11-01' in merged_data)
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            month_day = filename.split('.')[0]
            # print(month_day)
            month, day = map(int, month_day.split('_'))
            date_str = f"{year}-{month:02d}-{day:02d}"
            # print(date_str)
            with open(os.path.join(directory, filename), 'r') as file:
                data = json.load(file)

            # Update or add the entry for date_str
            if date_str not in merged_data or not merged_data[date_str]:
                merged_data[date_str] = data

    with open(output_file, 'w') as file:
        json.dump(merged_data, file, indent=4)

# Example usage
# Assuming the current directory is the desired location for the output file
current_directory = os.getcwd()
output_file_path = os.path.join(current_directory, 'json', 'merged.json')
merge_json_files(current_directory, output_file_path)

