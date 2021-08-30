import xml.etree.ElementTree as ET

from textblob import TextBlob

import SongInformation

def song_polarity(songtext):
    polarity_analysis = TextBlob(songtext).polarity
    return polarity_analysis

def song_polarity_lines(songtext):
    lines = songtext.split('\n')
    polarity_analysis = 0
    count = 0
    for line in lines:
        polarity_analysis += TextBlob(line).polarity
        count += 1
    result = polarity_analysis/count
    return result

def pos_neg_neutral_polarity(songtext, root):
    polarity = song_polarity_lines(songtext)
    if polarity < 0:
        result = "The polarity of '" + SongInformation.get_songtitle(songtext, root) + "' by " + SongInformation.get_artist(songtext, root) + " is negative"
    elif polarity > 0:
        result = "The polarity of '" + SongInformation.get_songtitle(songtext, root) + "' by " + SongInformation.get_artist(songtext, root) + " is positive"
    else:
        result = "The polarity of '" + SongInformation.get_songtitle(songtext, root) + "' by " + SongInformation.get_artist(songtext, root) + " is neutral"
    return result

def similar_mood_polarity(songtitle, artist, root):
    for child in root:
        if SongInformation.get_songtitle_child(child) == songtitle and SongInformation.get_artist_child(child) == artist:
            songtext = child.find("songtext").text
            song_child = child
    polarity = song_polarity_lines(songtext)

    minimum = 10.0
    result = ""

    for child in root:
        if child != song_child:
            songtext_child = SongInformation.get_songtext_child(child)
            polarity_child = song_polarity_lines(songtext_child)
    
            
            if polarity > 0 and polarity_child > 0:
                difference = polarity - polarity_child
                if abs(difference) < minimum:
                    minimum = abs(difference)
                    minimum_song = child
                    result = "'" + SongInformation.get_songtitle_child(minimum_song) + "' by " + SongInformation.get_artist_child(minimum_song) + " has a similiar mood to '" + songtitle + "' by " + artist

            if polarity < 0 and polarity_child < 0:
                difference = abs(polarity - polarity_child)
                if abs(difference) < minimum:
                    minimum = abs(difference)
                    minimum_song = child
                    result = "'" + SongInformation.get_songtitle_child(minimum_song) + "' by " + SongInformation.get_artist_child(minimum_song) + " has a similiar mood to '" + songtitle + "' by " + artist
                    
            

    return result

    

def similar_mood_polarity_title(songtitle, artist, root):
    for child in root:
        if SongInformation.get_songtitle_child(child) == songtitle and SongInformation.get_artist_child(child) == artist:
            songtext = child.find("songtext").text
            song_child = child
    polarity = song_polarity_lines(songtext)

    minimum = 10.0
    result = ""

    for child in root:
        if child != song_child:
            songtext_child = SongInformation.get_songtext_child(child)
            polarity_child = song_polarity_lines(songtext_child)
    
            
            if polarity > 0 and polarity_child > 0:
                difference = polarity - polarity_child
                if abs(difference) < minimum:
                    minimum = abs(difference)
                    minimum_song = child
                    result = "'" + SongInformation.get_songtitle_child(minimum_song) + "' by " + SongInformation.get_artist_child(minimum_song)

            if polarity < 0 and polarity_child < 0:
                difference = abs(polarity - polarity_child)
                if abs(difference) < minimum:
                    minimum = abs(difference)
                    minimum_song = child
                    result = "'" + SongInformation.get_songtitle_child(minimum_song) + "' by " + SongInformation.get_artist_child(minimum_song) 
            

    return result
        

