import xml.etree.ElementTree as ET

import pandas as pd

import SongtextAdjectives

import SongInformation


tree = ET.parse('D:/Data/Nextcloud/Documents/Uni/Advanced NLP with Python/AP Projekt/Data_songtexts_genius_complete.xml')

root = tree.getroot()


for child in root:

    songtitle = SongInformation.get_songtitle(child)
    artist = SongInformation.get_artist(child)
    songtext = SongInformation.get_songtext(child)
    
    # print(SongtextAdjectives.get_adjectives(songtext))
    # print("")
    # print(SongtextAdjectives.adjectives_sorted(songtext))
    # print("")
    # print(SongtextAdjectives.find_repeated_adjectives(songtext))
    # print("")
    # print(SongtextAdjectives.find_main_adjectives(songtext))
    # print("")
    print(SongtextAdjectives.find_similar_song(songtitle, artist, root))
    print("")