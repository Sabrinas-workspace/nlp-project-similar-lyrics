"""This module tests the module lyrics_sentiments and exports the results.
"""

import xml.etree.ElementTree as ET
import pandas as pd
import lyrics_sentiment
import song_information

# Insert the path to your XML corpus and comment in the next line
# tree = ET.parse('PATH')
root = tree.getroot()

# Some example queries
print(lyrics_sentiment.query_sentiment("Animal", "Troye Sivan", root))
print("")
print(lyrics_sentiment.query_sentiment("Paralyzed", "NF", root))
print("")

print(lyrics_sentiment.query_get_song_recommendation("Lover", "Taylor Swift", root))
print("")
print(lyrics_sentiment.query_get_song_recommendation("Returns", "NF", root))
print("")


# Creates dataframe for results
songtitles = []
artists = []
polarities = []
similar_sentiment = []
for child in root:
    songtitle = song_information.get_songtitle(child)
    artist = song_information.get_artist(child)
    lyrics = song_information.get_lyrics(child)
    polarity = lyrics_sentiment.song_polarity(lyrics)
    similar_song = lyrics_sentiment.similar_sentiment(child, root)
    songtitles.append(songtitle)
    artists.append(artist)
    polarities.append(polarity)
    similar_sentiment.append(similar_song)

songs = {'Songtitle': songtitles,
         'Artist': artists,
         'Song polarity': polarities,
         'Song with a similar sentiment': similar_sentiment
        }

df = pd.DataFrame(songs, columns = ['Songtitle', 'Artist', 'Song polarity',
                                    'Song with a similar sentiment'])

# Insert the path to the folder in which you want to save the results file
# and comment in the next line
# df.to_csv (r'PATH/sentiment_results.csv', sep= ';', index = False, header=True)
print(df)
