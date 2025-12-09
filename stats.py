def get_num_words(path:str):
    with open(path) as f:
        words = f.read()
        
        nb = len(words.split())
        return f"Found {nb} total words"
    
def get_nb_char(path:str):
    with open(path) as f:
        file = f.read()
        words = file.lower().split()
        
        value = {}
        for word in words:
            for char in word:
                if char not in value:
                    value[char] = 1
                else:
                    value[char] +=1
        return value
    
def sort_on(items):
    
    return items["num"]

    
def sort_list(characters:dict):
    
    value = []
    for character in characters:
        sorted = {}
        sorted["char"] = character
        sorted["num"] = characters[character]
        value.append(sorted)
    value.sort(reverse=True,key=sort_on)
    return value