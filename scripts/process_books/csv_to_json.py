import csv
import json

# Constants
CHAPTER = "Chapter 4 - Numerical Computation"
SOURCE = "Deep Learning Book, Goodfellow et Al. 2016"
SOURCE_ID = "Goodfellow-et-al-2016"
AUTHOR = "Ian Goodfellow and Yoshua Bengio and Aaron Courville"

CHAPTER_MAPPING = {
    "main-4.xhtml": "Introduction",
    "main-5.xhtml": "Linear Algebra",
    "main-6.xhtml": "Probability and Information Theory",
    "main-7.xhtml": "Numerical Computation",
    "main-8.xhtml": "Machine Learning Basics",
    "main-9.xhtml": "Feedforward Deep Networks",
    "main-10.xhtml": "Regularization for Deep Learning",
    "main-11.xhtml": "Optimization for Training Deep Models",
    "main-12.xhtml": "Convolutional Networks",
    "main-13.xhtml": "Sequence Modeling: Recurrent and Recursive Nets",
    "main-14.xhtml": "Practical Methodology",
    "main-15.xhtml": "Applications",
    "main-16.xhtml": "Linear Factor Models",
    "main-17.xhtml": "Autoencoders",
    "main-18.xhtml": "Representation Learning",
    "main-19.xhtml": "Structured Probabilistic Models for Deep Learning",
    "main-20.xhtml": "Monte Carlo Methods",
    "main-21.xhtml": "Confronting the Partition Function",
    "main-22.xhtml": "Approximate Inference",
    "main-23.xhtml": "Deep Generative Models",
}


# Read the CSV file
with open('deeplearning.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = []

    for row in reader:
        rows.append({
            "id": row["universal_book_id"],
            "text": row["text_paragraph"],
            "chapter": CHAPTER_MAPPING.get(row["paragraph_id"], ""),
            "chapter_id": row["paragraph_id"],
            "source": SOURCE,
            "source_id": SOURCE_ID,
            "author": AUTHOR
        })

# Write the JSON output file
with open('deeplearning.json', 'w') as jsonfile:
    json.dump(rows, jsonfile, indent=2)
