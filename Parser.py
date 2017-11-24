import numpy as np
import scipy as sc
#import pandas as pd
from collections import namedtuple
import re

# TODO: parsing:
# words: array of sentences nums, each slot contains array of words of the sentence
# tags: array of sentences nums, each slot contains array of the tags of the sentence
# array of unique words
# array of unique tags

prev_tags = namedtuple("prev_tags", ["prev1", "prev2"])

def parse_wtag_with_tags(filePath):
    words_arr = []
    tags_arr = []
    with open(filePath) as test_file:
        for line in test_file:
            line = line.strip('\n')
            #words_arr.append(re.split("_\w*\$?,? ", line))
            words_arr.append(['**', '*'] + (re.split(" |_", line))[::2])
            tags_arr.append(['**', '*'] + (re.split(" |_", line))[1::2])
    return words_arr, tags_arr


'''Creates the following  dicts:
    1) words to tags
    2) tags to prev tags (bigrams)
    3) tags to prev1 and prev2 tags (trigrams)
'''
def gen_dicts(words_arr, tags_arr):
    f_slots_assigned = 0
    word_to_tag_dict = {}
    tag_bigram_dict = {}
    tag_trigram_dict = {}

    # words to tags dict creation:
    for j, line in enumerate(words_arr):
        for i, word in enumerate(line):
            tag = tags_arr[j][i]
            if word in word_to_tag_dict:
                if tag not in word_to_tag_dict[word]:
                    word_to_tag_dict[word][tag] = f_slots_assigned
                    f_slots_assigned += 1
            else:
                word_to_tag_dict[word] = {tag: f_slots_assigned}
                f_slots_assigned += 1

    # bigrams tags dict creation:
    for tag_line in tags_arr:
        for i, tag in enumerate(tag_line[2:]):
            prev = tag_line[i-1]
            if tag in tag_bigram_dict:
                if prev not in tag_bigram_dict[tag]:
                    tag_bigram_dict[tag][prev] = f_slots_assigned
                    f_slots_assigned += 1
            else:
                tag_bigram_dict[tag] = {prev: f_slots_assigned}
                f_slots_assigned += 1

    # trigrams tags dict creation:
    for tag_line in tags_arr:
        for i, tag in enumerate(tag_line[2:]):
            prev = prev_tags(prev1=tag_line[i-1], prev2=tag_line[i-2])
            if tag in tag_trigram_dict:
                if prev not in tag_trigram_dict[tag]:
                    tag_trigram_dict[tag][prev] = f_slots_assigned
                    f_slots_assigned += 1
            else:
                tag_trigram_dict[tag] = {prev: f_slots_assigned}
                f_slots_assigned += 1

    return {'w_t': word_to_tag_dict, 't_bigram': tag_bigram_dict, 't_trigram': tag_trigram_dict}





test_words, test_tags = parse_wtag_with_tags('./test.wtag')
dicts = gen_dicts(test_words, test_tags)

print(len(dicts['t_bigram']['NNS']))
print(len(dicts['t_trigram']['CD']))

#print(test_words[0], len(test_words[0]))
#print(test_tags[0], len(test_tags[0]))

# for i, w_line in enumerate(test_words):
#     if len(test_tags[i]) != len(w_line):
#         print(i)
#
# print(test_words[0], len(test_words[0]))
# print(test_tags[0], len(test_tags[0]))

# test_data = np.loadtxt(, delimiter=' ', dtype='str')
# print(test_data[0])


# TODO: building f(x,y) functions:
# array of functions


# v*f = obj
#
# f100:
# for word in train
#
#     take real tag
#     find slots to lot
#     vf
#
#     for tag in word
#         find slots to lit
#         vf += sum(v(slots))
#
# f103:
#
# f104:
#
# v_sum_total





