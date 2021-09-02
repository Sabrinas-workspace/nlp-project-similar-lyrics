import spacy
from collections import Counter
import SongInformation

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
        if SongInformation.get_songtitle(child) == songtitle and SongInformation.get_artist(child) == artist:
            songtext = SongInformation.get_songtext(child)
            main_topics = find_main_adjectives(songtext)
            song = child
    similar_songs = []
    for child in root:
        if song != child:
            songtext_child = SongInformation.get_songtext(child)
            main_topics_child = find_main_adjectives(songtext_child)
            for topic in main_topics_child:
                if topic in main_topics:
                    song_artist = "'" + SongInformation.get_songtitle(child) + "' by " + SongInformation.get_artist(child)
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
