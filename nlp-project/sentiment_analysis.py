import xml.etree.ElementTree as ET

import SongtextSentiment

tree = ET.parse('D:/Data/Nextcloud/Documents/Uni/Advanced NLP with Python/AP Projekt/Data_songtexts_genius.xml')

root = tree.getroot()

for child in root:
    text = child.find("songtext")
    songtext = text.text
    # print(SongtextSentiment.song_polarity(songtext))
    print(SongtextSentiment.song_polarity_lines(songtext))
    print(SongtextSentiment.pos_neg_neutral_polarity(songtext, root))

print("")
print(SongtextSentiment.similar_mood_polarity("Clouds", "NF", root))
print("")
print(SongtextSentiment.similar_mood_polarity("Paralyzed", "NF", root))
print("")
print(SongtextSentiment.similar_mood_polarity("Remember This", "NF", root))
print("")
print(SongtextSentiment.similar_mood_polarity("Returns", "NF", root))
print("")
print(SongtextSentiment.similar_mood_polarity("If you want love", "NF", root))
print("")
