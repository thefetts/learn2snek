def grams(anagram, nag_a_ram):
     gram_1 = list(anagram.replace(' ', ''))
     gram_2 = list(nag_a_ram.replace(' ',''))
     gram_1.sort()
     gram_2.sort()
     if gram_1 == gram_2:
         return "is anagram!"
     else:
         return "bropen!!"


def sort_anagram(word):
    return sorted(word.replace(' ',''))

def refactor_grams(anagram, nag_a_ram):
    if sort_anagram(anagram) == sort_anagram(nag_a_ram):
        return True
    else:
        return False

def add_ten(list_num):
    list_add_10 = []
    for num in list_num:
        list_add_10.append(num + 10)
    return list_add_10

def len_words(list_words):
    list_len_words = []
    for word in list_words:
        list_len_words.append(len(word))
    return list_len_words

def letter_counter(path_to_file, letters_to_count):
    dict_vowel_count = dict.fromkeys(letters_to_count, 0)
    for x in path_to_file:
        if x in dict_vowel_count:
            dict_vowel_count[x] += 1
    return dict_vowel_count

def remove_item(list_items, item_to_remove):
    if item_to_remove not in list_items:
        return "The item is not in the list."
    else:
        new_list_items = list(filter(lambda x: x != item_to_remove, list_items))
        return new_list_items

def cipher(text, cipher_alphabet, option):
    encipher_text = list(text)
    if option == "encipher":
        for index,x in enumerate(encipher_text):
            if x != ' ':
                encipher_text[index] = cipher_alphabet[x]
        return ''.join(encipher_text)

def count_isograms(text):
    count = 0
    for x in text:
        if len(x) == len(set(x)):
            count += 1
    return count

def matching_pairs(data):
    matches = []
    for index1, pair1 in enumerate(data):
        for index2, pair2 in enumerate(data[index1+1::]):
            if is_vowel(pair1[0]) == is_vowel(pair2[0]):
                if divisible_by_3(pair1[1]) == divisible_by_3(pair2[1]):
                    matches.append((index1, index2+index1+1))
    return matches

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u']

def divisible_by_3(number):
    return True if number % 3 == 0 else False



