import random

def get_titles(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents.strip().split('\n')
    
def pick_a_word(list_of_words):
    word = random.choice(list_of_words)
    return word



