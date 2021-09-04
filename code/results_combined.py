"""This module combines and compares all methods and exports the results.
"""
import xml.etree.ElementTree as ET
import pandas as pd
import song_information
import lyrics_topics
import lyrics_adjectives
import lyrics_sentiment

# Insert the path to your XML corpus and comment in the next line
# tree = ET.parse('PATH')
root = tree.getroot()

# Creates dataframe to compare the results of each method
songtitles = []
artists = []
similar_topics = []
might_have_similar_topics = []
similar_adjectives = []
similar_sentiment = []
for child in root:
    songtitle = song_information.get_songtitle(child)
    artist = song_information.get_artist(child)
    more_similar_songs_nouns = lyrics_topics.more_similar_songs(child, root)
    less_similar_songs_nouns = lyrics_topics.less_similar_songs(child, root)
    similar_songs_adj = lyrics_adjectives.find_similar_songs(child, root)
    similar_song_sentiment = lyrics_sentiment.similar_sentiment(child, root)
    songtitles.append(songtitle)
    artists.append(artist)
    similar_topics.append(more_similar_songs_nouns)
    might_have_similar_topics.append(less_similar_songs_nouns)
    similar_adjectives.append(similar_songs_adj)
    similar_sentiment.append(similar_song_sentiment)

songs = {'Songtitle': songtitles,
         'Artist': artists,
         'Songs with similar topics': similar_topics,
         'Songs that might have similar topics': might_have_similar_topics,
         'Songs with similar adjectives': similar_adjectives,
         'Song with a similar sentiment': similar_sentiment
        }

df_compare = pd.DataFrame(songs, columns = ['Songtitle', 'Artist',
                    'Songs with similar topics',
                    'Songs that might have similar topics',
                    'Songs with similar adjectives',
                    'Song with a similar sentiment'])

# Insert the path to the folder in which you want to save the results file
# and comment in the next line
# df_compare.to_csv (r'PATH/compare_results.csv', sep= ';', index = False, header=True)
print(df_compare)

# To combine the results, creates a new dataframe with only those similar songs
# that were a result for similar song with more than one method

same_result = []
for ind in df_compare.index:
    result_topics = df_compare['Songs with similar topics'][ind]
    result_topics_might = df_compare['Songs that might have similar topics'][ind]
    result_adj = df_compare['Songs with similar adjectives'][ind]
    result_sentiment = df_compare['Song with a similar sentiment'][ind]
    song_list = []
    if len(result_adj) != 0:
        for song in result_adj:
            count_adj = 1
            if song == result_sentiment:
                count_adj += 1
            if song in result_topics:
                count_adj += 1
            elif song in result_topics_might:
                count_adj += 1
            if count_adj > 1:
                song_list.append({song: count_adj})
    if result_sentiment not in result_adj:
        count_sentiment = 1
        if result_sentiment in result_topics:
            count_sentiment += 1
        elif result_sentiment in result_topics_might:
            count_sentiment += 1
        if count_sentiment > 1:
            song_list.append({result_sentiment: count_sentiment})
    same_result.append(song_list)

combine = {'Songtitle': songtitles,
         'Artist': artists,
         'Similar songs (same result)': same_result
        }

df_combine = pd.DataFrame(songs, columns = ['Songtitle', 'Artist',
                    'Similar songs (same result)'])

# Insert the path to the folder in which you want to save the results file
# and comment in the next line
# df_combine.to_csv (r'PATH/combine_results.csv', sep= ';', index = False, header=True)
print(df_combine)
