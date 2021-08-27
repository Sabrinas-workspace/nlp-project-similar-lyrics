from typing import Text
import spacy

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
    return polarity_analysis

def song_subjectivity(songtext):
    subjectivity_analysis = TextBlob(songtext).subjectivity
    return subjectivity_analysis

def pos_neg_neutral_polarity(songtext, root):
    polarity = song_polarity_lines(songtext)
    if polarity < 0:
        result = "The polarity of '" + SongInformation.get_songtitle(songtext, root) + "' by " + SongInformation.get_artist(songtext, root) + " is negative"
    elif polarity > 0:
        result = "The polarity of '" + SongInformation.get_songtitle(songtext, root) + "' by " + SongInformation.get_artist(songtext, root) + " is positive"
    else:
        result = "The polarity of '" + SongInformation.get_songtitle(songtext, root) + "' by " + SongInformation.get_artist(songtext, root) + " is neutral"
    return result