import json
import mmap


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
    # print(index[lexicon[word]])
    # If the word was not found in the index, return an empty list


# Example usage
search_inverted_index('covid', 'lexicon.json', 'invert.json')
