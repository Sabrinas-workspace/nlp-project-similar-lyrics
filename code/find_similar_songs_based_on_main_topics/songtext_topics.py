"""This module finds topics of songs and finds songtexts with similar topics.

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

from collections import Counter
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import song_information

nlp = spacy.load(("en_core_web_sm"))

# Adding words to STOP_WORDS that are not (useful) topics
to_add = ["anything", "arm", "ay", "bag", "believin", "bit", "breakin", "bunch",
            "bus", "cart", "case", "clock", "course", "cryin", "dashboard",
            "dawn", "day", "door", "dime", "ditch", "fightin", "floor", "form",
            "fragment", "frame", "gate", "gettin", "getting", "half", "head",
            "hee", "holdin", "hour", "hundredfold", "immor", "kind", "leg",
            "lil", "line", "location", "look", "lookin", "lot", "lovin'",
            "makin", "mark", "mercede", "mile", "million", "mixin", "morning",
            "na", "nobody", "note", "number", "ooh", "oop", "ounce", "pack",
            "page", "parking", "pause", "people", "person", "piece", "pipe",
            "place", "point", "porch", "pound", "pow", "text", "room", "round",
            "runnin", "screen", "seam", "season", "shape", "shell", "shirt",
            "sidewalk", "sink", "sippin", "sittin", "somethin'", "spending",
            "step", "stick", "stressin", "stuff", "swimmin", "t", "telling",
            "thing", "thinkin", "toast", "tomorrow", "tonight", "trippin",
            "tryna", "tryin", "waitin", "way", "wearin", "week", "whoa",
            "window", "woe", "word", "year"]
for word in to_add:
    STOP_WORDS.add(word)

def get_nouns(songtext):
    """Finds all nouns from the songtext.

    Args:
        songtext: A string containing the songtext of a song.

    Returns:
        A list of all nouns found in the songtext.
    """
    doc = nlp(songtext.lower())
    all_nouns = [token.lemma_ for token in doc if token.pos_ == "NOUN"
                    and token.lemma_ not in STOP_WORDS]
    return all_nouns

def nouns_sorted(songtext):
    """Creates a Counter of all nouns from the songtext.

    Args:
        songtext: A string containing the songtext of a song.

    Returns:
        A Counter of all nouns found in the songtext.
    """
    nouns = get_nouns(songtext)
    sorted_nouns = Counter(nouns)
    return sorted_nouns

def find_topics(songtext):
    """Creates a list of all repeating nouns from the songtext.

    Args:
        songtext: A string containing the songtext of a song.

    Returns:
        A list of all nouns found more than once in the songtext.
    """
    nouns = nouns_sorted(songtext)
    topics = [key for key, value  in nouns.most_common() if value > 1]
    return topics

def find_fewer_topics(songtext):
    """Creates a list of the most frequent nouns from the songtext.

    Args:
        songtext: A string containing the songtext of a song.

    Returns:
        A list of all nouns found more than twice in the songtext.
    """
    nouns = nouns_sorted(songtext)
    fewer_topics = [key for key, value  in nouns.most_common() if value > 2]
    return fewer_topics

def find_main_topics(songtext):
    """Creates a list of all main topics of the songtext.

    Args:
        songtext: A string containing the songtext of a song.

    Returns:
        Depending on the size of the list, either the return list of find_topics
        or the return list of find_fewer_topics.
    """
    sorted_topics = find_topics(songtext)
    if len(sorted_topics) <= 5:
        main_topics = sorted_topics
    else:
        main_topics = find_fewer_topics(songtext)
        if len(main_topics) < 2:
            main_topics = sorted_topics
    return main_topics

def get_duplicates(song_list):
    """Finds all duplicates in a list.

    Args:
        song_list: Usually a list of "song by artist" strings which is the
        return list of find_similar_songs.

    Returns:
        A list of all items found more than once in the input list.
    """
    duplicates = [key for key in Counter(song_list).keys()
                    if Counter(song_list)[key] > 1]
    return duplicates

def without_duplicates(duplicates, similar_songs):
    """Creates a list that only includes those strings which occur once in the
    similar_songs list.

    Args:
        duplicates: Usually the list that is the return list of get_duplicates.
        similar_songs: Usually the list that is the return list of
        find_similar_songs.

    Returns:
        A list of all items that are found in the similar_songs list but not in
        the duplicates list.
    """
    result = []
    for song in similar_songs:
        if song not in duplicates:
            result.append(song)
    return result

def find_similar_songs(song, root):
    """Finds all similar songs to a song which are stored as children of an XML
    corpora.

    Args:
        song: A child of an ElementTree.
        root: The root of the ElementTree which has the child song.

    Returns:
        A list of all songs that have similar main topics to the passed song.
    """
    songtext = song_information.get_songtext(song)
    main_topics = find_main_topics(songtext)
    similar_songs = []
    for child in root:
        if child != song:
            songtext_child = song_information.get_songtext(child)
            main_topics_child = find_main_topics(songtext_child)
            for topic in main_topics_child:
                if topic in main_topics:
                    song_artist = ("'" + song_information.get_songtitle(child)
                                + "' by " + song_information.get_artist(child))
                    similar_songs.append(song_artist)
    return similar_songs

def more_similar_songs(song, root):
    """Creates a list with only those songs which have more than one topic in
    common with the passed song.

    Args:
        song: A child of an ElementTree.
        root: The root of the ElementTree which has the child song.

    Returns:
        A list of all songs that have more than one similar main topics to the
        passed song.
    """
    similar_songs = find_similar_songs(song, root)
    result = []
    if len(similar_songs) > 1:
        duplicates = get_duplicates(similar_songs)
        if len(duplicates) > 0:
            result = duplicates
    return result

def less_similar_songs(song, root):
    """Creates a list with only those songs which have only one topic in
    common with the passed song.

    Args:
        song: A child of an ElementTree.
        root: The root of the ElementTree which has the child song.

    Returns:
        A list of all songs that have exactly one similar main topic to the
        passed song.
    """
    similar_songs = find_similar_songs(song, root)
    result = []
    if len(similar_songs) > 1:
        duplicates = get_duplicates(similar_songs)
        if len(duplicates) > 1:
            result = without_duplicates(duplicates, similar_songs)
        else:
            result = similar_songs
    else:
        result = similar_songs
    return result

def query_get_song_recommendation(songtitle, artist, root):
    """Tries to recommend similar songs to the requested song with an assessment
    of how likely the inquirer will like these songs.

    Args:
        songtitle: A string containing a song name.
        artist: A string containing the artist of the song.
        root: The root of the ElementTree.

    Returns:
        A string message including how much the inquirer could like the similar
        song(s) or an apology if either the song could not be found in the
        corpora or if a similar song could not be found.
    """
    for child in root:
        if (song_information.get_songtitle(child) == songtitle
                and song_information.get_artist(child) == artist):
            song = child
        else:
            answer = ("Sorry, '" + songtitle + "' by " + artist
                        + "could not be found in this corpora")
    similar_songs = find_similar_songs(song, root)
    if len(similar_songs) == 1:
        answer = ("If you like '" + songtitle + "' by" + artist
                        + ", you might like " + str(similar_songs[0]))
    elif len(similar_songs) > 1:
        duplicates = get_duplicates(similar_songs)
        if len(duplicates) > 0:
            really_like = ("If you like '" + songtitle + "' by " + artist +
                        ", you might really like " + ", ".join(duplicates))
            similar_songs_rest = without_duplicates(duplicates, similar_songs)
            might_like = ("If you like '" + songtitle + "' by " + artist
                        + ", you might like " + ", ".join(similar_songs_rest))
            answer = really_like + '\n' + might_like
        else:
            answer = ("If you like '" + songtitle + "' by " + artist +
                            ", you might like " + ", ".join(similar_songs))
    else:
        answer = ("Sorry, there is no similar song to '" + songtitle +
                        "' by" + artist + " in this corpora")
    return answer

def query_find_song_about(topic, root):
    """Tries to find songs about this topic in a corpora."

    Args:
        topic: A string containing a topic which has to be a single noun.
        root: The root of the ElementTree.

    Returns:
        A string including one or more songs about the requested topic or an
        apology if no song about that topic could be found in the corpora.
    """
    songs = []
    for child in root:
        songtext = song_information.get_songtext(child)
        main_topics = find_main_topics(songtext)
        if topic in main_topics:
            song_artist = ("'" + song_information.get_songtitle(child)
                        + "' by " + song_information.get_artist(child))
            songs.append(song_artist)
    if len(songs) == 1:
        answer = "A song about " + topic + " is " + str(songs[0])
    elif len(songs) > 1:
        answer = "Songs about " + topic + " are " + ", ".join(songs)
    else:
        answer = ("Sorry, there is no song about " + topic
                        + " in this corpora")
    return answer

def query_find_topics_of_artist(artist, root):
    """Tries to find common topics of the songtexts from an artist."

    Args:
        artist: A string containing a music artist.
        root: The root of the ElementTree.

    Returns:
        A string including the topics that are repeatetly dealt with in songs of
        the requested artist or an apology if the artist could not be found in
        the corpora.
    """
    topics = []
    repeating_topics = []
    for child in root:
        artist_child = song_information.get_artist(child)
        if artist_child == artist:
            songtext = song_information.get_songtext(child)
            song_topics = find_topics(songtext)
            for topic in song_topics:
                if topic in topics and topic not in repeating_topics:
                    repeating_topics.append(topic)
                else:
                    topics.append(topic)
            if artist[-1] == 's':
                answer = ("The topics of " + artist + "' songs are "
                            + ", ".join(repeating_topics))
            else:
                answer = ("The topics of " + artist + "'s songs are "
                            + ", ".join(repeating_topics))
        else:
            answer = "Sorry, the artist you requested is not in the corpora"
    return answer
