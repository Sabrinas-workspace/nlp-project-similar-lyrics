"""This module finds similar songs based on common adjectives.

   Note: This module is based on the module songtext_topics but is not included
   in or combined with songtext_topics to avoid confusion and to allow the
   possibility of working with only one method to find similar songtext since
   they do not lead to equally good or bad results.

   Functions:
   The following functions can be used without a XML tree:
   get_adjectives(string) -> list
   adjectives_sorted(string) -> Counter
   find_repeated_adjectives(string) -> list
   get_duplicates(list) -> list

   The following functions can only be used with a XML tree:
   find_similar_songs(xml.etree.ElementTree.Element,
                        xml.etree.ElementTree.Element) -> list
   query_get_song_recommendation(string, string, xml.etree.ElementTree.Element)
        -> string
"""

from collections import Counter
import spacy
import song_information

nlp = spacy.load(("en_core_web_sm"))

def get_adjectives(songtext):
    """Finds all adjectives from the songtext.

    Args:
        songtext: A string containing the songtext of a song.

    Returns:
        A list of all adjectives found in the songtext.
    """
    doc = nlp(songtext.lower())
    all_adjectives = [token.lemma_ for token in doc if token.pos_ == "ADJ"]
    return all_adjectives

def adjectives_sorted(songtext):
    """Creates a Counter of all adjectives from the songtext.

    Args:
        songtext: A string containing the songtext of a song.

    Returns:
        A Counter of all adjectives found in the songtext.
    """
    adjectives = get_adjectives(songtext)
    sorted_adjectives = Counter(adjectives)
    return sorted_adjectives

def find_repeated_adjectives(songtext):
    """Creates a list of all repeating adjectives from the songtext.

    Args:
        songtext: A string containing the songtext of a song.

    Returns:
        A list of all adjectives found more than once in the songtext.
    """
    adjectives = adjectives_sorted(songtext)
    repeated_adjectives = [key for key, value  in adjectives.most_common()
                            if value > 1]
    return repeated_adjectives

def get_duplicates(song_list):
    """Finds all duplicates in a list.

    Args:
        song_list: A list of "song by artist" strings with which this
        function is called from find_similar_songs.

    Returns:
        A list of all strings found more than once in the input list.
    """
    duplicates = [key for key in Counter(song_list).keys()
                    if Counter(song_list)[key] > 1]
    return duplicates

def find_similar_songs(song, root):
    """Finds all similar songs to a song which are stored as children of an XML
    corpus.

    Args:
        song: A child of an ElementTree.
        root: The root of the ElementTree which has the child song.

    Returns:
        A list of all songs that have at least two common adjectives to the
        passed song.
    """
    songtext = song_information.get_songtext(song)
    adjectives = find_repeated_adjectives(songtext)
    similar_songs = []
    for child in root:
        if child != song:
            songtext_child = song_information.get_songtext(child)
            adjectives_child = find_repeated_adjectives(songtext_child)
            for topic in adjectives_child:
                if topic in adjectives:
                    song_artist = ("'" + song_information.get_songtitle(child)
                                + "' by " + song_information.get_artist(child))
                    similar_songs.append(song_artist)
    result = get_duplicates(similar_songs)
    return result

def query_get_song_recommendation(songtitle, artist, root):
    """Tries to recommend similar songs to the requested song.
    Args:
        songtitle: A string containing a song name.
        artist: A string containing the artist of the song.
        root: The root of the ElementTree.

    Returns:
        A string message including which similar song(s) to the requested song
        the inquirer could like or an apology if either the song could not be
        found in the corpus or if a similar song could not be found.
    """
    for child in root:
        if (song_information.get_songtitle(child) == songtitle
                and song_information.get_artist(child) == artist):
            song = child
        else:
            answer = ("Sorry, '" + songtitle + "' by " + artist
                        + "could not be found in this corpus")
    similar_songs = find_similar_songs(song, root)
    if len(similar_songs) > 0:
        answer = ("If you like '" + songtitle + "' by " + artist
                    + ", you might like " + ", ".join(similar_songs))
    else:
        answer = ("Sorry, there is no similar song to '" + songtitle + "' by "
                    + artist + " in this corpus")
    return answer
