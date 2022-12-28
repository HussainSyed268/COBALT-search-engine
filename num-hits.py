def get_hits(word, inverted_index, lexicon_file):
    # Initialize an empty dictionary to store the hits for each article
    hits = {}
    with open(lexicon_file, 'r') as f:
        lexicon_mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        # Read the contents of the memory-mapped file into a string
        lexicon_data = lexicon_mm.read()
        # Parse the lexicon data as a dictionary
        lexicon = json.loads(lexicon_data)
    word_id = lexicon[f'{word}']
    print(word_id)
    with open(inverted_index, 'r') as f:
        inverted_mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        # Read the contents of the memory-mapped file into a string
        inverted_data = inverted_mm.read()
        # Parse the lexicon data as a dictionary
        inverted = json.loads(inverted_data)
    # Look up the word's ID in the inverted index and retrieve the dictionary of files and locations
    file_info = inverted[f'{word_id}']
    # Iterate over the files in the dictionary
    for file_number_article_id, locations in file_info.items():
        print(file_number_article_id)
        # Extract the article ID from the file number and article ID string
        # article_id = file_number_article_id.split(' [')[1][:-1]
        article_id = re.search(r"\[(.*?)\]", file_number_article_id).group(1)
        print(article_id)
        # Calculate the total number of times the word appears in the article
        word_count = len(locations)
        # Add an entry to the hits dictionary for the article
        hits[article_id] = word_count
    # Return the hits dictionary
    return hits