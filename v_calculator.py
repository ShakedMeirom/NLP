import numpy as np
import scipy as sc
from scipy import sparse
from Parser import *
from Parser import prev_tags
from f_calculators import *


# Target Function calculator:
# uses v, build_f_tot and build_f in order to create the target function (with regularization)
def target_func(words_data, tags_data, unique_tags, dicts, f_slot_assigned, v):
    raise NotImplemented


# Gradient Function calculator:
# uses v, build_f_tot and build_f in order to create the gradient function (with regularization)
def gradient_func(words_data, tags_data, unique_tags, dicts, f_slot_assigned, v):
    raise NotImplemented


# Finds the optimal v from the train data
# uses the target and gradient functions in order to optimize v by the lbfgs algorithm
def optimize_v(target_func, gradient_func):
    raise NotImplemented
