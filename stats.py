def word_count(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def char_count(text):
    char = {}
    ltext = text.lower()
    words = ltext.split()
    for word in words:
        for letter in word:
            if letter not in char:
                char[letter] = 1
            else:
                char[letter] += 1
    return char

def sort_on(items):
    return items["num"]

def sorter(dict):
    count = []
    for char in dict:
        entry = {}
        value = dict[char]
        entry["name"] = char
        entry["num"] = value
        count.append(entry)
    count.sort(reverse=True, key=sort_on)
    return count