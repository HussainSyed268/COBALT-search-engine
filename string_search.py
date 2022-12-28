import json
import mmap


def search_inverted_index(search_string, lexicon_file, index_file):
    # Memory-map the lexicon file
    with open(lexicon_file, 'r') as f:
        lexicon_mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        # Read the contents of the memory-mapped file into a string
        lexicon_data = lexicon_mm.read()
        # Parse the lexicon data as a dictionary
        lexicon = json.loads(lexicon_data)
    # Split the search string into individual words
    words = search_string.split(" ")
    # Initialize an array to store the sets of doc_ids for each word
    doc_ids_sets = []
    # Iterate over the words
    for word in words:
        # Check if the word is in the lexicon
        if word not in lexicon:
            # If the word is not in the lexicon, add an empty set to the array
            doc_ids_sets.append(set())
            continue
        # Memory-map the inverted index file
        with open(index_file, 'r') as f:
            index_mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        # Read the contents of the memory-mapped file into a string
        index_data = index_mm.read()
        # Parse the index data as a dictionary
        index = json.loads(index_data)
        # Get the doc_ids for the word from the index
        doc_ids = index[str(lexicon[word])]
        # Convert the doc_ids to a set and add it to the array
        doc_ids_sets.append(set(doc_ids))
    # Return the array of doc_ids sets
    return doc_ids_sets


# Example usage
docs_id=search_inverted_index('covid and same', 'lexicon.json', 'invert.json')
common_docs=docs_id[0]
for i in range(1,len(docs_id)):
    common_docs=common_docs.intersection(docs_id[i])
print(common_docs)
