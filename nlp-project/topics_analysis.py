import xml.etree.ElementTree as ET

import pandas as pd

import SongtextTopics 

import SongInformation


tree = ET.parse('D:/Data/Nextcloud/Documents/Uni/Advanced NLP with Python/AP Projekt/Data_songtexts_genius.xml')

root = tree.getroot()

#print(root.tag)
#print(type(root))

for child in root:
    #print(child.tag)
    #print(child.tag, child.attrib)
    # for name, value in child.attrib.items():
    #     print(value)
    #print(type(child))
    #songtitle = "".join(child.attrib.values())
    #print(songtitle)
    art = child.find("artist")
    artist_value = "".join(art.attrib.values())
    # print(artist_value)
    #print(art.attrib)
    text = child.find("songtext")
    s = text.text
    #print(s)
    #art = tree.SubElement(child, "artist") #funtioniert nicht
    #print(art)

    # print("")
    # print(SongtextTopics.get_nouns(s))
    # print("")
    # print(SongtextTopics.nouns_sorted(s))
    # print("")
    # print(SongtextTopics.find_topics(s))
    # print("")
    # print(SongtextTopics.find_main_topics(s))
    # print("")

    # print(SongtextTopics.get_adjectives(s))
    # print("")
    # print(SongtextTopics.adjectives_sorted(s))
    # print("")
    # print(SongtextTopics.find_repeated_adjectives(s))
    # print("")
    # print(SongtextTopics.find_main_adjectives(s))
    #print("")

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

songtitles = []
artists = []
songs_with_similar_topics = []
songs_that_might_have_similar_topics = []

for child in root:
    songtitle = SongInformation.get_songtitle_child(child)
    artist = SongInformation.get_artist_child(child)
    more_similar_songs = SongtextTopics.more_similar_songs(songtitle, artist, root)
    less_similar_songs = SongtextTopics.less_similar_songs(songtitle, artist, root)
    #n = "\n".join(more_similar_songs)
    #more_similar_songs_string = '\\n'.join(more_similar_songs)
    # more_similar_songs_string = more_similar_songs_string.split("\n")
    # print(more_similar_songs_string)
    songtitles.append(songtitle)
    artists.append(artist)
    #songs_with_similar_topics.append(f"{n}")
    songs_with_similar_topics.append(more_similar_songs)
    songs_that_might_have_similar_topics.append(less_similar_songs)

# songs_with_similar_topics = [item.split("\n") for item in songs_with_similar_topics]

# for list in songs_with_similar_topics:
#     #list = '\\n'.join(list)
#     #list = "\n".join("{}: {}".format(i) for i in list)
#     n = "\n".join(list)
#     list = f"{n}"
#     print(list)

# print(songtitles)
# print("")
# print(artists)
# print("")
# print(songs_with_similar_topics)
# print("")
# print(songs_that_might_have_similar_topics)
# print("")

# import pandas as pd

# cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
#         'Price': [22000,25000,27000,35000]
#         }

# df = pd.DataFrame(cars, columns = ['Brand','Price'], index=['Car_1','Car_2','Car_3','Car_4'])

# print (df)

songs = {'Songtitle': songtitles,
         'Artist': artists,
         'Songs with similar topics': songs_with_similar_topics,
         'Songs that might have similar topics': songs_that_might_have_similar_topics
        }
# pd.set_option('display.max_columns', 10)

df = pd.DataFrame(songs, columns = ['Songtitle','Artist', 'Songs with similar topics'])

df.to_csv (r'D:/Data/Nextcloud/Documents/Uni/Advanced NLP with Python/AP Projekt/Data_topics.csv', sep= ';', index = False, header=True)
# gfg_csv_data = df.to_csv(r'D:/Data/Nextcloud/Documents/Uni/Advanced NLP with Python/AP Projekt/Data_topics.csv', index = False)
# print('\nCSV String:\n', gfg_csv_data)
print (df)

# saving the DataFrame as a CSV file
# gfg_csv_data = df.to_csv('GfG.csv', index = False)
# print('\nCSV String:\n', gfg_csv_data)

# my_df = {'Name': ['Rutuja', 'Anuja'], 
#          'ID': [1, 2], 
#          'Age': [20, 19]}
# dftest = pd.DataFrame(my_df)
  
# # displaying the DataFrame
# print('DataFrame:\n', dftest)
   
# # saving the DataFrame as a CSV file
# csv_data = dftest.to_csv('D:/Data/Nextcloud/Documents/Uni/Advanced NLP with Python/AP Projekt/Data_test.csv', sep= ';', index = False)
# print('\nCSV String:\n', csv_data)