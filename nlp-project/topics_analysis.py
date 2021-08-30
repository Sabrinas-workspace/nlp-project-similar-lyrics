import xml.etree.ElementTree as ET

import SongtextTopics 

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
    songtitle = "".join(child.attrib.values())
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
    print(SongtextTopics.find_main_topics(s))
    print("")

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
