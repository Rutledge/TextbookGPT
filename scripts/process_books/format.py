import json
import os

input_file_pattern = "images_in_chapter_part"
output_file_name = "output.json"

def process_file(file_name):
    with open(file_name, 'r') as file:
        input_data = json.load(file)

    output_data = []
    for index, item in enumerate(input_data, start=1):
        output_data.append({
            "id": str(index),
            "text": item["image_caption"],
            "metadata": {
                "image_url": item["image_source"],
                "source": "Neuroscience"
            }
        })
    return output_data

all_output_data = []

for i in range(23):
    file_name = f"{input_file_pattern}{str(i).zfill(4)}.json"
    if os.path.exists(file_name):
        all_output_data.extend(process_file(file_name))

with open(output_file_name, 'w') as output_file:
    json.dump(all_output_data, output_file, indent=2)

