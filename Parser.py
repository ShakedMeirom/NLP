import numpy as np
import scipy as sc
from collections import namedtuple
import re

# named tuples for trigrams:
prev_tags = namedtuple("prev_tags", ["prev1", "prev2"])


# words: array of sentences nums, each slot contains array of words of the sentence
# tags: array of sentences nums, each slot contains array of the tags of the sentence
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


# Creates a set of the unique tags of the data:
def gen_unique_tags(tags_arr):
    unique_tags = set().union(*tags_arr)
    return unique_tags


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

    return {'w_t': word_to_tag_dict, 't_bigram': tag_bigram_dict, 't_trigram': tag_trigram_dict}, f_slots_assigned


def test_parser(filePath):
    words_arr, tags_arr = parse_wtag_with_tags(filePath)
    for i, w_line in enumerate(words_arr):
        if len(tags_arr[i]) != len(w_line):
            print(i)

    print(words_arr[0], len(words_arr[0]))
    print(tags_arr[0], len(tags_arr[0]))





