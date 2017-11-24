import numpy as np
import scipy as sc
from scipy import sparse
from Parser import *
from Parser import prev_tags


# Building f(x,y) for a specific tag y and history x.
# history means a dict, which contains: {prev1: , prev2: , words_line: , idx}
def build_f(tag:str, history:dict, dicts:dict):
    f_slots = []
    idx = history['idx']
    curr_word = history['words_line'][idx]
    # f100:
    if curr_word in dicts['w_t']:
        if tag in dicts['w_t'][curr_word]:
            f_slots.append(dicts['w_t'][curr_word][tag])

    # f104:
    if tag in dicts['t_bigram']:
        if history['prev1'] in dicts['t_bigram'][tag]:
            f_slots.append(dicts['t_bigram'][tag][history['prev1']])

    # f103:
    if tag in dicts['t_trigram']:
        if prev_tags(history['prev1'], history['prev2']) in dicts['t_trigram'][tag]:
            f_slots.append(dicts['t_trigram'][tag][prev_tags(history['prev1'], history['prev2'])])

    return f_slots


# building a sparse matrix for sum(f(x(i), y(i))
def build_f_tot(words_data, tags_data, dicts, f_slot_assigned):
    rows_count = 0
    rows_for_f_tot = []
    columns_count = 0
    columns_for_f_tot = []
    data_for_f_tot = []

    for line_idx, line in enumerate(words_data):
        for idx, word in enumerate(line[2:]):
            idx += 2  # in order to not iterate over '**', '*'
            tag = tags_data[line_idx][idx]
            prev1 = tags_data[line_idx][idx-1]
            prev2 = tags_data[line_idx][idx-2]
            history = {'prev1': prev1, 'prev2': prev2, 'words_line': line, 'idx': idx}
            curr_f = build_f(tag=tag, history=history, dicts=dicts)
            curr_f_len = len(curr_f)

            # update f_tot data:
            rows_for_f_tot += curr_f
            columns_for_f_tot += np.full((curr_f_len), columns_count, dtype=int).tolist()
            columns_count += 1
            data_for_f_tot += np.ones(curr_f_len, dtype=int).tolist()
            rows_count += curr_f_len

    f_tot = sparse.coo_matrix((data_for_f_tot, (rows_for_f_tot, columns_for_f_tot)), shape=(f_slot_assigned, columns_count+1), dtype=int)
    return f_tot
