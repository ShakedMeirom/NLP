from v_calculator import *


# calculates q(v/t,u,w[1:n],k) in the viterbi algorithm:
def calculate_tag_probability(tag:str, history:dict, unique_tags:list, dicts:dict, v):
    raise NotImplemented


# calculates the most probable tagging for a sentence:
# Returns a list of the most probable tags:
def viterbi_algorith(sentence:list, unique_tags:list, dicts:dict, v):
    raise NotImplemented


# Generate Inference:
# Calculates the most probable tagging for all the sentences of the data.
# Returns a list of lists, which has the same size of the data, so each word has its most probable tag.
def gen_inference(data:list, unique_tags:list, dicts:dict, v):
    raise NotImplemented


