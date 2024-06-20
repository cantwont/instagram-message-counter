import os
import json

def count_content_key(directory):
    content_count = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as json_file:
                        data = json.load(json_file)
                        print(f"Loaded message data from {file_path}")

                        if isinstance(data, list):
                            for item in data:
                                if isinstance(item, dict):
                                    if 'content' in item:
                                        content_count += 1
                                    #print(f"Item in list: {item}")
                        elif isinstance(data, dict):
                            def find_content(d):
                                nonlocal content_count
                                for key, value in d.items():
                                    if key == 'content':
                                        content_count += 1
                                    elif isinstance(value, dict):
                                        find_content(value)
                                    elif isinstance(value, list):
                                        for elem in value:
                                            if isinstance(elem, dict):
                                                find_content(elem)
                            find_content(data)

                except (json.JSONDecodeError, IOError) as e:
                    print(f"Error reading {file_path}: {e}")

    return content_count

directory = input("Enter the directory path: ")
count = count_content_key(directory)
print(f"You have {count} messages with this person")
