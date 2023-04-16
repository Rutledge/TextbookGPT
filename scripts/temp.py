import json

# Read JSON data from the file
with open('process_json/output.json', 'r') as file:
    data = json.load(file)

# Update the IDs to be incremental
for index, item in enumerate(data, start=1):
    item['id'] = str(index)

# Write the updated JSON data back to the file
with open('output.json', 'w') as file:
    json.dump(data, file, indent=2)
