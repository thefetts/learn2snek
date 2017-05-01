def word_count(sentence):
    return "Total word count: " + str(len(sentence.split()))

def unique_word(sentence):
    list_of_words = []
    sentence = sentence.replace(".","")
    sentence = sentence.replace(";","")
    sentence = sentence.replace("?","")
    sentence = sentence.replace("!","")
    for x in sentence.split():
        if x not in list_of_words:
            list_of_words.append(x)
    return "Unique words: " + str(len(list_of_words))

def sentence_count(sentence):
    number_of_ends = sentence.count(".") + sentence.count("!") + sentence.count("?") + sentence.count(";")
    return "Sentences: " + str(number_of_ends)