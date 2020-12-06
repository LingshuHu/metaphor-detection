from nltk.corpus import wordnet as wn
from GetDependencyParse import dependency_parse
import math

def detect_metaphor(sentence):
    """ Accepts a sentence and outputs similarity of noun-noun pairs related by nsubj
    """

    dep_parse_output, noun_list = dependency_parse(sentence.lower())

    nsubj_pairs = []
    for dp in dep_parse_output:
        if(len(dp) >= 3):
            if (dp[0] == "nsubj" and dp[1] in noun_list and dp[2] in noun_list):
                nsubj_pairs.append(dp[1:])

    #nsubj_pairs = [ns_parse[1:] for ns_parse in list(filter(lambda dp: dp[0] == "nsubj" and dp[1] in noun_list and dp[2] in noun_list, dep_parse_output))]

    for pair in nsubj_pairs:
        print("\nInvestigating metaphor for pair {0}".format(pair))

        syn_pair = []

        for word in pair:

            synsets = wn.synsets(word)
            print("What sense of '{0}' would you like to use?".format(word))
            for i, synset in enumerate(synsets):
                print("{0}: {1}".format(i, synset.definition))
            chosen_id = int(input("Enter number corresponding to sense: "))

            syn_pair.append(synsets[chosen_id])

        similarity_measure = similarity(syn_pair[0], syn_pair[1])

        if similarity_measure is None or similarity_measure >= 0.1:
            print("{0} does NOT constitute a Noun-Noun metaphor, similarity {1}".format(pair, similarity_measure))
        else:
            print("{0} constitutes a Noun-Noun metaphor, similarity {1}".format(pair, similarity_measure))

    if len(nsubj_pairs) == 0:
        print("No Noun-Noun pairs detected. Thus the sentence is not a Noun-Noun metaphor")

def similarity(synset1, synset2):
    """ Accepts 2 synsets and returns the similarity
    """

    return(synset1.path_similarity(synset2))

def square_rooted(x):
    return(round(math.sqrt(sum([a*a for a in x])),3))
  
def cosine_similarity(x,y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return(round(numerator/float(denominator),3))


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")

    detect_metaphor(sentence)
