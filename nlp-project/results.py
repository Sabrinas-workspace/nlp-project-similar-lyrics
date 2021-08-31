import xml.etree.ElementTree as ET

import pandas as pd

import SongInformation

import SongtextSentiment

import SongtextTopics 


tree = ET.parse('D:/Data/Nextcloud/Documents/Uni/Advanced NLP with Python/AP Projekt/Data_songtexts_genius_complete.xml')

root = tree.getroot()

# create dataframe for results

songtitles = []
artists = []
songs_with_similar_topics = []
songs_that_might_have_similar_topics = []
songs_with_similar_mood = []

for child in root:
    songtitle = SongInformation.get_songtitle(child)
    artist = SongInformation.get_artist(child)
    more_similar_songs = SongtextTopics.more_similar_songs(songtitle, artist, root)
    less_similar_songs = SongtextTopics.less_similar_songs(songtitle, artist, root)
    similar_mood = SongtextSentiment.similar_mood_polarity_title(songtitle, artist, root)   
    songtitles.append(songtitle)
    artists.append(artist)
    songs_with_similar_topics.append(more_similar_songs)
    songs_that_might_have_similar_topics.append(less_similar_songs)
    songs_with_similar_mood.append(similar_mood)

compare_results = {'Songtitle': songtitles,
         'Artist': artists,
         'Songs with similar topics': songs_with_similar_topics,
         'Songs that might have similar topics': songs_that_might_have_similar_topics,
         'Song with a similar mood': songs_with_similar_mood
        }


df = pd.DataFrame(compare_results, columns = ['Songtitle','Artist', 'Songs with similar topics', 'Songs that might have similar topics', 'Song with a similar mood'])

df.to_csv (r'D:/Data/Nextcloud/Documents/Uni/Advanced NLP with Python/AP Projekt/results.csv', sep= ';', index = False, header=True)

print (df)

