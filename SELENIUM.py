import json
import time
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from pathlib import Path

# Start timer
start = time.perf_counter()

# Initialize variables
forward_index = {}
inverted_index = {}
lexicon = {}

# Initialize lemmatizer and stop words
wordnet = WordNetLemmatizer()
stop = stopwords.words('english')
stop.extend(['@','a','the','an',";","of",r"\u2014",r".", ",", "!", "?", ":", ";", "-", "--", "(", ")", "[", "]", "{", "}", "'", "\""])

# Function to add a word to the lexicon
def add_word_to_lexicon(word):
    if word not in lexicon:
        lexicon[word] = len(lexicon)

# Function to build a forward index for a given list of documents
def build_forward_index(documents, doc_number_prefix):
    global forward_index
    temp_forward_index = {}
    for i, doc in enumerate(documents):
        # Split document into words
        words = doc['content'].split()
        # Remove stop words and lemmatize remaining words
        words = [wordnet.lemmatize(word.lower()) for word in words if word not in stop]
        # Add words to lexicon and store their indices in the forward index
        doc_id = f"{doc_number_prefix}[{i}]"
        temp_forward_index[doc_id] = []
        for word in words:
            add_word_to_lexicon(word)
            temp_forward_index[doc_id].append(lexicon[word])
    # Merge the temporary forward index into the global forward index
    forward_index.update(temp_forward_index)
# Function to build an inverted index from a forward index
def build_inverted_index(forward_index):
    global inverted_index
    temp_inverted_index = {}
    # Iterate over the forward index
    for doc_id, words in forward_index.items():
        # Iterate over the words in the document
        for i, word in enumerate(words): 
            # If the word is not yet in the inverted index, add it with the current document as its first occurrence
            if word not in temp_inverted_index:
                temp_inverted_index[word] = {doc_id: [i]}
            # If the word is already in the inverted index, add the current document to the list of occurrences
            else:
                # If the current document is not yet in the list of occurrences for the word, add it with the current word's index as its first occurrence
                if doc_id not in temp_inverted_index[word]:
                    temp_inverted_index[word][doc_id] = [i]
                # If the current document is already in the list of occurrences for the word, add the current word's index to the list of occurrences
                else:
                    temp_inverted_index[word][doc_id].append(i)
    # Merge the temporary inverted index into the global inverted index
    inverted_index.update(temp_inverted_index)

# Get list of files in the 'check' directory
root = Path('./check')
files = [str(p) for p in root.iterdir()]

# Process each file
for i, file in enumerate(files):
    # Open the file and load the JSON data
    with open(file) as f:
        data = json.load(f)
    # Build the forward index and inverted index for the data
    doc_number = i  # Get the document number as the index of the file in the list of files
    build_forward_index(data, doc_number)
    build_inverted_index(forward_index)
# Stop timer and print elapsed time
end = time.perf_counter()
print(end - start)

# Save the inverted index, forward index, and lexicon to JSON files
with open("invert.json", "w") as f:
    json.dump(inverted_index, f, indent=1)
with open("forward.json", "w") as f:
    json.dump(forward_index, f, indent=1)
with open("lexicon.json", "w") as f:
    json.dump(lexicon, f, indent=1)
