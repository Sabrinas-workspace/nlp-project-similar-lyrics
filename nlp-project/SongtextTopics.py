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