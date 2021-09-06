"""This module analyses a song's sentiment and based on that finds similar songs.

   Functions:
   The following function can be used without an XML tree:
   song_polarity(string) -> float

   The following functions can only be used with an XML tree:
   query_sentiment(string, string, xml.etree.ElementTree.Element) -> string
   pos_minimum_difference(xml.etree.ElementTree.Element, float,
                xml.etree.ElementTree.Element) -> xml.etree.ElementTree.Element
   neg_minimum_difference(xml.etree.ElementTree.Element, float,
                xml.etree.ElementTree.Element) -> xml.etree.ElementTree.Element
   similar_sentiment(xml.etree.ElementTree.Element,
                                xml.etree.ElementTree.Element) -> string
   query_get_song_recommendation(string, string, xml.etree.ElementTree.Element)
        -> string
"""

from textblob import TextBlob
import song_information

def song_polarity(lyrics):
    """Calculates the polarity of the lyrics.

    Args:
        lyrics: A string containing the lyrics of a song.

    Returns:
        A float representing the polarity value of the lyrics.
    """
    lines = lyrics.split('\n')
    polarity_analysis = 0
    count = 0
    for line in lines:
        polarity_analysis += TextBlob(line).polarity
        count += 1
    result = polarity_analysis/count
    return result

def query_sentiment(songtitle, artist, root):
    """Evaluates the requested songs sentiment.

    Args:
        songtitle: A string containing a song name.
        artist: A string containing the artist of the song.
        root: The root of the ElementTree.

    Returns:
        A string message including whether the requested song has a negative,
        positive or neutral sentiment.
    """
    for child in root:
        if (song_information.get_songtitle(child) == songtitle
                and song_information.get_artist(child) == artist):
            song = child
    lyrics = song_information.get_lyrics(song)
    polarity = song_polarity(lyrics)
    songtitle = song_information.get_songtitle(root, lyrics)
    artist = song_information.get_artist(root, lyrics)
    if polarity < 0:
        result = ("The sentiment of '" + songtitle + "' by " + artist +
                    " is negative")
    elif polarity > 0:
        result = ("The sentiment of '" + songtitle + "' by " + artist +
                    " is positive")
    else:
        result = ("The sentiment of '" + songtitle + "' by " + artist +
                    " is neutral")
    return result

def pos_minimum_difference(song, polarity, root):
    """Calculates which song has the most similar polarity to the passed
    polarity.

    Args:
        song: A child of an ElementTree.
        polarity: A positive float which represents the polarity of the song to
        which the song with the most similar polarity is wanted.
        root: The root of the ElementTree which has the child song.

    Returns:
        The child of the XML tree in which the song with the most similar
        polarity to the passed polarity is stored.
    """
    minimum = 10.0 # A number which is higher than the polarity values
    for child in root:
        if child != song:
            lyrics_child = song_information.get_lyrics(child)
            polarity_child = song_polarity(lyrics_child)
            if polarity_child > 0:
                difference = polarity - polarity_child
                if abs(difference) < minimum:
                    minimum = abs(difference)
                    minimum_song = child
    return minimum_song

def neg_minimum_difference(song, polarity, root):
    """Calculates which song has the most similar polarity to the passed
    polarity.

    Args:
        song: A child of an ElementTree.
        polarity: A negative float which represents the polarity of the song to
        which the song with the most similar polarity is wanted.
        root: The root of the ElementTree which has the child song.

    Returns:
        The child of the XML tree in which the song with the most similar
        polarity to the passed polarity is stored.
    """
    minimum = 10.0 # A number which is higher than the polarity values
    for child in root:
        if child != song:
            lyrics_child = song_information.get_lyrics(child)
            polarity_child = song_polarity(lyrics_child)
            if polarity_child < 0:
                difference = abs(polarity - polarity_child)
                if abs(difference) < minimum:
                    minimum = abs(difference)
                    minimum_song = child
    return minimum_song

def similar_sentiment(song, root):
    """Finds the song with the most similar polarity to the requested song from
    all songs stored in an XML corpus.

    Args:
        song: A child of an ElementTree.
        root: The root of the ElementTree which has the child song.

    Returns:
        A string containing the song with the most similar polarity to the
        passed song.
    """
    lyrics = song_information.get_lyrics(song)
    polarity = song_polarity(lyrics)
    if polarity > 0:
        similar_song = pos_minimum_difference(song, polarity, root)
        result = ("'" + song_information.get_songtitle(similar_song) + "' by "
                        + song_information.get_artist(similar_song))
    elif polarity < 0:
        similar_song = neg_minimum_difference(song, polarity, root)
        result = ("'" + song_information.get_songtitle(similar_song) + "' by "
                        + song_information.get_artist(similar_song))
    return result

def query_get_song_recommendation(songtitle, artist, root):
    """Recommends the song with the most similar sentiment to the requested song.
    Args:
        songtitle: A string containing a song name.
        artist: A string containing the artist of the song.
        root: The root of the ElementTree.

    Returns:
        A string message including which song has a similar mood to the
        requested song.
    """
    for child in root:
        if (song_information.get_songtitle(child) == songtitle
                and song_information.get_artist(child) == artist):
            song = child
    lyrics = song_information.get_lyrics(song)
    polarity = song_polarity(lyrics)
    if polarity > 0:
        similar_song = pos_minimum_difference(song, polarity, root)
        result = ("'" + song_information.get_songtitle(similar_song) + "' by "
                    + song_information.get_artist(similar_song)
                    + " has a similiar mood to '" + songtitle + "' by " + artist)
    elif polarity < 0:
        similar_song = neg_minimum_difference(song, polarity, root)
        result = ("'" + song_information.get_songtitle(similar_song) + "' by "
                    + song_information.get_artist(similar_song)
                    + " has a similiar mood to '" + songtitle + "' by " + artist)
    return result
