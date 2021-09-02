"""This module finds similar songs based on common adjectives.

   Note: This module is based on the module songtext_topics but is not included
   in or combined with songtext_topics to avoid confusion and to allow the
   possibility of working with only one method to find similar songtext since
   they do not lead to equally good or bad results.

   Functions:
   The following functions can be used without a XML tree:
   get_nouns(string) -> list
   nouns_sorted(string) -> Counter
   find_topics(string) -> list
   find_fewer_topics(string) -> list
   find_main_topics(string) -> list
   get_duplicates(list) -> list
   without_duplicates(list, list) -> list

   The following functions can only be used with a XML tree:
   find_similar_songs(xml.etree.ElementTree.Element,
                       xml.etree.ElementTree.Element) -> list
   more_similar_songs(xml.etree.ElementTree.Element,
                       xml.etree.ElementTree.Element) -> list
   less_similar_songs(xml.etree.ElementTree.Element,
                       xml.etree.ElementTree.Element) -> list
   query_get_song_recommendation(string, string, xml.etree.ElementTree.Element)
               -> string
   query_find_song_about(string, xml.etree.ElementTree.Element) -> string
   query_find_topics_of_artist(string, xml.etree.ElementTree.Element) -> string
"""

import spacy
from collections import Counter
import song_information

nlp = spacy.load(("en_core_web_sm"))

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

# little functions, only for XML

def get_duplicates(song_list):
    duplicates = [key for key in Counter(song_list).keys() if Counter(song_list)[key] > 1]
    return duplicates

def get_similar_songs_without_duplicates(duplicates, similar_songs):
    result = []
    for song in similar_songs:
        if song not in duplicates:
            result.append(song)
    return result

def find_similar_song(songtitle, artist, root):
    for child in root:
        if song_information.get_songtitle(child) == songtitle and song_information.get_artist(child) == artist:
            songtext = song_information.get_songtext(child)
            main_topics = find_main_adjectives(songtext)
            song = child
    similar_songs = []
    for child in root:
        if song != child:
            songtext_child = song_information.get_songtext(child)
            main_topics_child = find_main_adjectives(songtext_child)
            for topic in main_topics_child:
                if topic in main_topics:
                    song_artist = "'" + song_information.get_songtitle(child) + "' by " + song_information.get_artist(child)
                    similar_songs.append(song_artist)
        
    result_string = ""
    if len(similar_songs) == 1:
        result_string = "If you like '" + songtitle + "' by " + artist + ", you might like " + str(similar_songs[0]) 
    elif len(similar_songs) > 1:
        duplicates = get_duplicates(similar_songs)
        if len(duplicates) > 0:
            duplicates_string = "If you like '" + songtitle + "' by " + artist + ", you might really like " + ", ".join(duplicates)
            other_similar_songs = get_similar_songs_without_duplicates(duplicates, similar_songs)
            other_similar_songs_string = "If you like '" + songtitle + "' by " + artist + ", you might like " + ", ".join(other_similar_songs)

            result_string = duplicates_string + '\n' + other_similar_songs_string
        else:
            result_string = "If you like '" + songtitle + "' by " + artist + ", you might like " + ", ".join(similar_songs)
    else:
        result_string = "I'm sorry, there is no similar song to '" + songtitle + "' by " + artist + " in this database"
        
    return result_string
