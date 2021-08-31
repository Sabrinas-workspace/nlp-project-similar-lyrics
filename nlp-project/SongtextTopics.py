# Python Module SongtextTopics

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from collections import Counter
import xml.etree.ElementTree as ET
import SongInformation

to_add = ["anything", "believin", "bunch", "case", "day", "head", "hundredfold", "kind", "lot", "million", "people", "person", "pow", "t", "thing", "thinkin", "somethin'", "stressin", "tryna", "way", "wearin"]
for word in to_add:
    STOP_WORDS.add(word)
#print(sorted(STOP_WORDS))

nlp = spacy.load(("en_core_web_sm"))

def get_nouns(songtext):
    doc = nlp(songtext.lower())
    all_nouns = [token.lemma_ for token in doc if token.pos_ == "NOUN" and token.lemma_ not in STOP_WORDS]
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
        if len(main_topics) < 2:
            main_topics = sorted_topics
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



# other functions, only work with XML

def find_song_about(topic, root):
    songs = []
    result_string = ""
    for child in root:
        songtext = SongInformation.get_songtext(child)
        main_topics = find_main_topics(songtext)

        if topic in main_topics:
            song_artist = "'" + SongInformation.get_songtitle(child) + "' by " + SongInformation.get_artist(child)
            songs.append(song_artist)
    if len(songs) == 1:
        result_string = "A song about " + topic + " is " + str(songs[0]) 
    elif len(songs) > 1:
        result_string = "Songs about " + topic + " are " + ", ".join(songs)
    else:
        result_string = "I'm sorry, there is no song about " + topic + " in this database"
        
    return result_string

def find_topics_of_artist(artist, root):
    topics = []
    repeating_topics = []
    for child in root:
        artist_child = SongInformation.get_artist(child)
        if artist_child == artist:
            songtext = SongInformation.get_songtext(child)
            song_topics = find_topics(songtext)
            for topic in song_topics:
                if topic in topics and topic not in repeating_topics:
                    repeating_topics.append(topic)
                else:
                    topics.append(topic)
    result = ""
    if artist[-1] == 's':
        result = "The topics of " + artist + "' songs are " + ", ".join(repeating_topics)
    else:
        result = "The topics of " + artist + "'s songs are " + ", ".join(repeating_topics)

    return result

# find similar functions, only XML

def find_similar_song(songtitle, artist, root):
    for child in root:
        if SongInformation.get_songtitle(child) == songtitle and SongInformation.get_artist(child) == artist:
            songtext = SongInformation.get_songtext(child)
            main_topics = find_main_topics(songtext)
            song = child
    similar_songs = []
    for child in root:
        if song != child:
            songtext_child = SongInformation.get_songtext(child)
            main_topics_child = find_main_topics(songtext_child)
            for topic in main_topics_child:
                if topic in main_topics:
                    song_artist = "'" + SongInformation.get_songtitle(child) + "' by " + SongInformation.get_artist(child)
                    similar_songs.append(song_artist)
        
    result_string = ""
    if len(similar_songs) == 1:
        result_string = "If you like '" + songtitle + "' by" + artist + ", you might like " + str(similar_songs[0]) 
    elif len(similar_songs) > 1:
        duplicates = get_duplicates(similar_songs)
        if len(duplicates) > 1:
            duplicates_string = "If you like '" + songtitle + "' by " + artist + ", you might really like " + ", ".join(duplicates)
            other_similar_songs = get_similar_songs_without_duplicates(duplicates, similar_songs)
            other_similar_songs_string = "If you like '" + songtitle + "' by " + artist + ", you might like " + ", ".join(other_similar_songs)

            result_string = duplicates_string + '\n' + other_similar_songs_string
        else:
            result_string = "If you like '" + songtitle + "' by " + artist + ", you might like " + ", ".join(similar_songs)
    else:
        result_string = "I'm sorry, there is no song similar song to '" + songtitle + "' by" + artist + " in this database"
        
    return result_string

def find_similar_songs(songtitle, artist, root):
    for child in root:
        if SongInformation.get_songtitle(child) == songtitle and SongInformation.get_artist(child) == artist:
            songtext = SongInformation.get_songtext(child)
            main_topics = find_main_topics(songtext)
            song = child
    similar_songs = []
    for child in root:
        if song != child:
            songtext_child = child.find("songtext").text
            main_topics_child = find_main_topics(songtext_child)
            for topic in main_topics_child:
                if topic in main_topics:
                    song_artist = "'" + SongInformation.get_songtitle(child) + "' by " + SongInformation.get_artist(child)
                    similar_songs.append(song_artist)
    return similar_songs

def more_similar_songs(songtitle, artist, root):
    similar_songs = find_similar_songs(songtitle, artist, root)
    result = []
   
    if len(similar_songs) > 1:
        duplicates = get_duplicates(similar_songs)
        if len(duplicates) > 1:
            result = duplicates
            
    return result

def less_similar_songs(songtitle, artist, root):
    similar_songs = find_similar_songs(songtitle, artist, root)
    
    result = []
   
    if len(similar_songs) > 1:
        duplicates = get_duplicates(similar_songs)
        if len(duplicates) > 1:
            result = get_similar_songs_without_duplicates(duplicates, similar_songs)
        else:
            result = similar_songs
    else:
        result = similar_songs
            
    return result    
    





