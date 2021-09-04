"""This module tests the module lyrics_adjectives and exports the results.
"""

import xml.etree.ElementTree as ET
import pandas as pd
import lyrics_adjectives
import song_information

# Insert the path to your XML corpus and comment in the next line
# tree = ET.parse('PATH')
root = tree.getroot()

# Some example queries
print(lyrics_adjectives.query_get_song_recommendation("Demons", "Imagine Dragons", root))
print("")
print(lyrics_adjectives.query_get_song_recommendation("Time", "NF", root))
print("")
print(lyrics_adjectives.query_get_song_recommendation("Bad at love", "Halsey", root))
print("")


# Creates dataframe for results
songtitles = []
artists = []
similar_adjectives = []
for child in root:
    songtitle = song_information.get_songtitle(child)
    artist = song_information.get_artist(child)
    similar_songs = lyrics_adjectives.find_similar_songs(child, root)
    songtitles.append(songtitle)
    artists.append(artist)
    similar_adjectives.append(similar_songs)

songs = {'Songtitle': songtitles,
         'Artist': artists,
         'Songs with similar adjectives': similar_adjectives
        }

df = pd.DataFrame(songs, columns = ['Songtitle', 'Artist',
                    'Songs with similar adjectives'])

# Insert the path to the folder in which you want to save the results file
# and comment in the next line
# df.to_csv (r'PATH/adjectives_results.csv', sep= ';', index = False, header=True)
print(df)
