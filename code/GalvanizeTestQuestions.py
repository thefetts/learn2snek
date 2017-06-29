import math
import scipy.stats as st



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

def four_decimals(number):
    return float("{0:.4f}".format(number))

def nCr(number_of_x,limiter):
    return math.factorial (number_of_x) /\
           (math.factorial (number_of_x - limiter) * math.factorial(limiter))

def binomial_dist(number_of_x, limiter, p_of_success_in_1):
    return four_decimals( nCr(number_of_x, limiter) * (p_of_success_in_1 ** limiter)
           * ((1 - p_of_success_in_1) ** (number_of_x - limiter)))

def geometric_dist(p_of_success, bernoulli_step):
    return four_decimals(((1 - p_of_success) ** (bernoulli_step - 1)) * p_of_success)

def geometric_dist_sum(p_of_success, up_to_benoulli_step):
    total = 0
    for step in range(up_to_benoulli_step):
        total += geometric_dist(p_of_success, step)
    return four_decimals(total)

def poisson_dist(num_of_succ, mean):
    return four_decimals( ((math.e ** -mean) * (mean ** num_of_succ)) /
                         math.factorial(num_of_succ))

def sample_mean(total_positives, sample_size):
    return four_decimals( (1 * total_positives + 0 * (sample_size - total_positives)) / sample_size )

def sample_variance (total_positives, sample_size):
    return four_decimals(((total_positives * (1 - sample_mean(total_positives, sample_size)) ** 2) \
           + ((sample_size - total_positives) * (0 - sample_mean(total_positives, sample_size)) ** 2)) / \
             (sample_size - 1))

def sample_sd (total_positives, sample_size):
    return four_decimals(math.sqrt(sample_variance(total_positives, sample_size)))

def sd_of_sample_mean(total_positives, sample_size):
    return four_decimals(sample_sd(total_positives, sample_size) / math.sqrt(sample_size))

def confidence_interval(total_positives, sample_size, confidence):
    z_score = st.norm.ppf(confidence)
    interval = four_decimals(z_score * sd_of_sample_mean(total_positives, sample_size))
    print ("We are " + str(confidence*100)
           + "% confident that the true percentage of what we are measuring"
           + ", that the positives are "
           + str(sample_mean(total_positives, sample_size)*100) + "% + or - "
           + str(interval))

/Users/jerryfallon/workspace/learn2snek/code/GalvanizeTestQuestions.py





