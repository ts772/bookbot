def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main(filepath):
    return get_book_text(filepath)

def word_count(filepath):
    text = main(filepath)
    words = text.split()
    return len(words)
    
def character_count(filepath):
    characters = {}
    text = main(filepath)
    words = text.split()
    for word in words:
        for letter in word:
            i = letter.lower()
            if i not in characters:
                characters[i] = 1
            elif i in characters:
                characters[i] += 1
    return characters

def report(filepath):
    characters = character_count(filepath)
    def sort_on(characters):
        for letter in characters:
            num = characters[letter]
        return num
    list = [{key: value} for key, value in characters.items()]
    list.sort(reverse = True, key = sort_on)
    return list
    





