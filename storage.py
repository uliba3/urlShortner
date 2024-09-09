import json

# Input: None
# Output: data dictionary
def get_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data

# Input: original_url, hash
# Output: True if the data is saved successfully, False otherwise
def save_data(original_url, hash):
    data = get_data()
    data[hash] = original_url
    with open('data.json', 'w') as file:
        json.dump(data, file)
    return True

# Input: hash
# Output: original_url if the hash exists, None otherwise
def get_original_url(hash):
    data = get_data()
    return data.get(hash, None)

