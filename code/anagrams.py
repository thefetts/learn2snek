def grams(anagram, nag_a_ram):
    gram_1 = list(anagram.replace(' ', ''))
    gram_2 = list(nag_a_ram.replace(' ',''))
    gram_1.sort()
    gram_2.sort()
    if gram_1 == gram_2:
        return "is anagram!"
    else:
        return "bropen!!"




        # for a, b in zip(gram_1, gram_2):
        #     if a != b:
        #         print (a, "is different from", b)
        #         break
        #     else:
        #         print ("is anagram!")
        #         break
