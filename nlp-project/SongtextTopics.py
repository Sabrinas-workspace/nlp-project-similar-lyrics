# Python Module SongtextTopics

import spacy
from collections import Counter

nlp = spacy.load(("en_core_web_sm"))

def get_nouns(songtext):
    doc = nlp(songtext.lower())
    all_nouns = [token.lemma_ for token in doc if token.pos_ == "NOUN"]
    return all_nouns

def nouns_sorted(songtext):
    nouns = get_nouns(songtext)
    sorted_nouns = Counter(nouns)
    return sorted_nouns
    
def find_topics(songtext):
    nouns = nouns_sorted(songtext)
    topics = [key for key, value  in nouns.most_common() if value > 1]
    return topics

def find_fewer_topics(songtext):
    nouns = nouns_sorted(songtext)
    fewer_topics = [key for key, value  in nouns.most_common() if value > 2]
    return fewer_topics

def find_main_topics(songtext):
    sorted_topics = find_topics(songtext)
    if len(sorted_topics) <= 5:
        main_topics = sorted_topics
    else:
        main_topics = find_fewer_topics(songtext)
    return main_topics


# adjectives

def get_adjectives(songtext):
    doc = nlp(songtext.lower())
    all_adjectives = [token.lemma_ for token in doc if token.pos_ == "ADJ"]
    return all_adjectives

def adjectives_sorted(songtext):
    adjectives = get_adjectives(songtext)
    sorted_adjectives = Counter(adjectives)
    return sorted_adjectives
    
def find_repeated_adjectives(songtext):
    adjectives = adjectives_sorted(songtext)
    repeated_adjectives = [key for key, value  in adjectives.most_common() if value > 1]
    return repeated_adjectives

def find_most_used_adjectives(songtext):
    adjectives = adjectives_sorted(songtext)
    most_used_adjectives = [key for key, value  in adjectives.most_common() if value > 2]
    return most_used_adjectives

def find_main_adjectives(songtext):
    sorted_repeated_adjectives = find_repeated_adjectives(songtext)
    if len(sorted_repeated_adjectives) <= 5:
        main_adjectives = sorted_repeated_adjectives
    else:
        main_adjectives = find_most_used_adjectives(songtext)
    return main_adjectives