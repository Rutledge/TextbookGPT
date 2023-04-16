import json
import glob
import os
import boto3
from bs4 import BeautifulSoup

# Configure the S3 bucket and folder
bucket_name = "textbook-images-19283761293"
s3_folder = "neuroscience/"

# Initialize the S3 client
s3 = boto3.client("s3")

def upload_image_to_s3(image_path):
    with open(image_path, "rb") as file:
        s3_key = os.path.join(s3_folder, os.path.basename(image_path))
        s3.upload_fileobj(file, bucket_name, s3_key)
        s3_url = f"https://{bucket_name}.s3.amazonaws.com/{s3_key}"
    return s3_url

# Get all the HTML files in the folder
html_files = glob.glob("neuroscience/text/*.html")

for html_file in html_files:
    # Read the HTML file
    with open(html_file, "r") as file:
        html_content = file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all the image and caption pairs
    image_elements = soup.find_all("img", class_="calibre11")
    caption_elements = soup.find_all("figcaption", class_="figleg")

    # Extract image sources, upload them to S3, and store the S3 URLs and captions as JSON objects
    output_data = []
    for img, caption in zip(image_elements, caption_elements):
        local_image_src = img["src"]
        s3_image_src = upload_image_to_s3(os.path.join("neuroscience", local_image_src))
        caption_html = str(caption)
        output_data.append({"image_source": s3_image_src, "image_caption": caption_html})

    # Save the JSON objects to a file
    chapter = html_file.split("/")[-1].split(".")[0]  # Extract the chapter name
    output_file = f"neuroscience/text/images_in_chapter_{chapter}.json"
    with open(output_file, "w") as outfile:
        json.dump(output_data, outfile)

