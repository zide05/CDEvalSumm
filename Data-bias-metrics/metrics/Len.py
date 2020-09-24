from nltk import word_tokenize


def getlen(sample_list):
    lengths = []
    for sample in sample_list:
        lengths.append(sum([len(word_tokenize(sent)) for sent in sample]))
    return lengths
