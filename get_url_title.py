import json
import mmap
jsonFiles={0:"committeeconstructivetomorrowcfactorg.json",1:"crikey.json",2:"covertgeopolitics.json"}
def get_article_by_index(json_file, index):
    # Load the JSON file into a list of dictionaries
    with open(json_file, 'r') as f:
        articles = json.load(f)
    # Check if the index is within the range of the list
    if index >= 0 and index < len(articles):
        # Return the name and URL of the article at the given index
        return articles[index]['title'], articles[index]['url']
    # If the index is out of range, return None
    return None



def get_url_title(dict1, dict2):
    # Extract the keys of dict1
    keys = dict1.keys()
   
    # Split the keys on the '[' character and extract the first element of each key
    ids = [key.split('[')[0] for key in keys]
    indices = [int(key.split('[')[1].split(']')[0]) for key in keys]
    print(indices)

    print(ids)
    # Initialize an empty list to store the retrieved data
    data = []
    # Iterate through the IDs
    for i in range(len(ids)):
        # Check if the ID is in dict2
        # if id in keys2:
            # Use the ID to retrieve data from dict2
           print(ids[i])
           Jname= jsonFiles[int(ids[i])]
          

           name,url=get_article_by_index(Jname,indices[i])
           print(name,url)

            
    # Return the retrieved data
   




get_url_title(result,jsonFiles)


