import json
import mmap
import re
import os


def search_inverted_index(word, lexicon_file, index_file):
    # Memory-map the lexicon file
    with open(lexicon_file, 'r') as f:
        lexicon_mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        # Read the contents of the memory-mapped file into a string
        lexicon_data = lexicon_mm.read()
        # Parse the lexicon data as a dictionary
        lexicon = json.loads(lexicon_data)
    # Print the search word and the lexicon
    # print(f'Searching for word: {word}')
    # print(f'Lexicon: {lexicon}')
    # Check if the search word is in the lexicon
    if word not in lexicon:
        return []

    # Memory-map the inverted index file
    with open(index_file, 'r') as f:
        index_mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    # Read the contents of the memory-mapped file into a string
    index_data = index_mm.read()
    # Parse the index data as a dictionary
    index = json.loads(index_data)
    # Print the inverted index data
    id = lexicon[word]
    print(index[f'{id}'])
    # Check if the search word is in the index
    # If the word was not found in the index, return an empty list


search_inverted_index('covid', 'lexicon.json', 'invert.json')


def get_hits(word, inverted_index, lexicon_file):
    # Memory-map the lexicon file
    with open(lexicon_file, 'r') as f:
        lexicon_mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        # Read the contents of the memory-mapped file into a string
        lexicon_data = lexicon_mm.read()
        # Parse the lexicon data as a dictionary
        lexicon = json.loads(lexicon_data)
    # Check if the search word is in the lexicon
    if word not in lexicon:
        return {}
    # Get the word's ID from the lexicon
    word_id = lexicon[word]
    # Memory-map the inverted index file
    with open(inverted_index, 'r') as f:
        inverted_mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        # Read the contents of the memory-mapped file into a string
        inverted_data = inverted_mm.read()
        # Parse the inverted index data as a dictionary
        inverted = json.loads(inverted_data)
    # Look up the word's ID in the inverted index and retrieve the dictionary of files and locations
    file_info = inverted[f'{word_id}']
    # Initialize an empty dictionary to store the hits for each article
    hits = {}
    # Iterate over the files in the dictionary
    for file_number_article_id, locations in file_info.items():
        # Extract the article ID from the file number and article ID string
        article_id = re.search(r"\[(.*?)\]", file_number_article_id).group(1)
        print(file_info[file_number_article_id]["content"])
        # Calculate the total number of times the word appears in the article
        word_count = len(file_info[file_number_article_id]["content"]) +file_info[file_number_article_id]["title"]*5
        # Add an entry to the hits dictionary for the article
       
        hits[article_id] = word_count
    return hits
        
    # Return the hits dictionary
hits=get_hits("covid","invertnew.json","lexicon.json")
for id,num in hits.items():
    print(id , num)

# print(get_hits('hello', 'invert.json', 'lexicon.json'))


# folder_path = '/check'
# # Get a list of the file names in the folder
# files = os.listdir(folder_path)
# # Initialize an empty dictionary
# file_dict = {}
# # Loop through the list of file names
# for i, file in enumerate(files):
#     # Add the file name as a key to the dictionary, with the value equal to the index
#     file_dict[file] = i


# def get_article_by_index(json_file, index):
#     # Load the JSON file into a list of dictionaries
#     with open(json_file, 'r') as f:
#         articles = json.load(f)
#     # Check if the index is within the range of the list
#     if index >= 0 and index < len(articles):
#         # Return the name and URL of the article at the given index
#         return articles[index]['title'], articles[index]['url']
#     # If the index is out of range, return None
#     return None
