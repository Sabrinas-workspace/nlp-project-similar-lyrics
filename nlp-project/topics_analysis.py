import xml.etree.ElementTree as ET

import pandas as pd

import SongtextTopics 

import SongInformation


tree = ET.parse('D:/Data/Nextcloud/Documents/Uni/Advanced NLP with Python/AP Projekt/Data_songtexts_genius_complete.xml')

root = tree.getroot()

for child in root:
    songtitle = SongInformation.get_songtitle(child)
    artist = SongInformation.get_artist(child)
    songtext = SongInformation.get_songtext(child)
    # print("")
    # print(SongtextTopics.get_nouns(s))
    # print("")
    # print(SongtextTopics.nouns_sorted(s))
    # print("")
    # print(SongtextTopics.find_topics(s))
    # print("")
    # print(SongtextTopics.find_main_topics(s))
    # print("")
    print(SongtextTopics.find_similar_song(songtitle, artist, root))
    print("")


# print("")

# print(SongtextTopics.find_song_about("people", root))

# print("")

# print(SongtextTopics.find_song_about("love", root))

# print("")

# print(SongtextTopics.find_song_about("hate", root))

# print("")

# print(SongtextTopics.find_song_about("pain", root))

# print("")

# print(SongtextTopics.find_topics_of_artist("NF", root))

# print("")

# print(SongtextTopics.find_similar_song("My Stress", "NF", root))

# print("")


# create dataframe for results

# songtitles = []
# artists = []
# songs_with_similar_topics = []
# songs_that_might_have_similar_topics = []

# for child in root:
#     songtitle = SongInformation.get_songtitle(child)
#     artist = SongInformation.get_artist(child)
#     more_similar_songs = SongtextTopics.more_similar_songs(songtitle, artist, root)
#     less_similar_songs = SongtextTopics.less_similar_songs(songtitle, artist, root)
#     songtitles.append(songtitle)
#     artists.append(artist)
#     songs_with_similar_topics.append(more_similar_songs)
#     songs_that_might_have_similar_topics.append(less_similar_songs)




# print(songtitles)
# print("")
# print(artists)
# print("")
# print(songs_with_similar_topics)
# print("")
# print(songs_that_might_have_similar_topics)
# print("")


# songs = {'Songtitle': songtitles,
#          'Artist': artists,
#          'Songs with similar topics': songs_with_similar_topics,
#          'Songs that might have similar topics': songs_that_might_have_similar_topics
#         }


# df = pd.DataFrame(songs, columns = ['Songtitle','Artist', 'Songs with similar topics', 'Songs that might have similar topics'])

# # df.to_csv (r'D:/Data/Nextcloud/Documents/Uni/Advanced NLP with Python/AP Projekt/Data_topics.csv', sep= ';', index = False, header=True)

# print (df)

