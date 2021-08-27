import xml.etree.ElementTree as ET

from multimethod import multimethod

def get_songtext(child):
    songtext = child.find("songtext").text
    return songtext

def get_songtitle(songtext, root):
    for child in root:
        if get_songtext(child) == songtext:
            songtitle = "".join(child.attrib.values())
    return songtitle

def get_artist(songtext, root):
    for child in root:
        if get_songtext(child) == songtext:
            artist_child = child.find("artist")
            artist = "".join(artist_child.attrib.values())
    return artist


# @multimethod
# def get_songtext(songtitle, artist, root):
#     for child in root:
#         artist_child = child.find("artist")
#         if "".join(child.attrib.values()) == songtitle and "".join(artist_child.attrib.values()) == artist:
#             songtext = child.find("songtext").text
#     return songtext

# @multimethod
# def get_songtext(child):
#     songtext = child.find("songtext").text
#     return songtext

# @multimethod()
# def get_songtitle(songtext: str, root: ET.Element):
#     for child in root:
#         if get_songtext(child) == songtext:
#             songtitle = "".join(child.attrib.values())
#     return songtitle

# @multimethod()
# def get_songtitle(child : ET.Element):
#     songtitle = "".join(child.attrib.values())
#     return songtitle

# @multimethod()
# def get_artist(songtext: str, root: ET.Element):
#     for child in root:
#         if get_songtext(child) == songtext:
#             artist_child = child.find("artist")
#             artist = "".join(child.attrib.values())
#     return artist

# @multimethod()
# def get_artist(child: ET.Element):
#     artist_child = child.find("artist")
#     artist = "".join(artist_child.attrib.values())
#     return artist
