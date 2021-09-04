"""This module tests the module songtext_topics and exports the results.
"""

import xml.etree.ElementTree as ET
import pandas as pd
import songtext_topics
import song_information

# Insert the path to your XML corpus and comment in the next line
# tree = ET.parse('PATH')
root = tree.getroot()

# Some example queries
print(songtext_topics.query_get_song_recommendation("Billie Jean", "Michael Jackson", root))
print("")
print(songtext_topics.query_get_song_recommendation("My Stress", "NF", root))
print("")

print(songtext_topics.query_find_song_about("love", root))
print("")
print(songtext_topics.query_find_song_about("hate", root))
print("")
print(songtext_topics.query_find_song_about("pain", root))
print("")

print(songtext_topics.query_find_topics_of_artist("NF", root))
print("")
print(songtext_topics.query_find_topics_of_artist("Troye Sivan", root))
print("")
print(songtext_topics.query_find_topics_of_artist("Tina Turner", root))
print("")


# Creates dataframe for results
songtitles = []
artists = []
similar_topics = []
might_have_similar_topics = []
for child in root:
    songtitle = song_information.get_songtitle(child)
    artist = song_information.get_artist(child)
    more_similar_songs = songtext_topics.more_similar_songs(child, root)
    less_similar_songs = songtext_topics.less_similar_songs(child, root)
    songtitles.append(songtitle)
    artists.append(artist)
    similar_topics.append(more_similar_songs)
    might_have_similar_topics.append(less_similar_songs)

songs = {'Songtitle': songtitles,
         'Artist': artists,
         'Songs with similar topics': similar_topics,
         'Songs that might have similar topics': might_have_similar_topics
        }

df = pd.DataFrame(songs, columns = ['Songtitle', 'Artist',
                    'Songs with similar topics',
                    'Songs that might have similar topics'])

# Insert the path to the folder in which you want to save the results file
# and comment in the next line
# df.to_csv (r'PATH/topics_results.csv', sep= ';', index = False, header=True)
print(df)
