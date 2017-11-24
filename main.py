import numpy as np
import scipy as sc
from scipy import sparse
from Parser import *
from Parser import prev_tags
from f_calculators import *

#train_words, train_tags = parse_wtag_with_tags('./train.wtag')
test_words, test_tags = parse_wtag_with_tags('./test.wtag')
dicts, f_slot_assigned = gen_dicts(test_words, test_tags)
unique_tags = gen_unique_tags(tags_arr=test_tags)

#print(len(dicts['t_bigram']))
#print(len(dicts['t_trigram']))
#print(f_slot_assigned)

coo = build_f_tot(test_words, test_tags, dicts, f_slot_assigned)
print(coo.shape)

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