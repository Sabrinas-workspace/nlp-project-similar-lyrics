import xml.etree.ElementTree as ET

from multimethod import multimethod

# def get_songtext_child(child):
#     songtext = child.find("songtext").text
#     return songtext

# def get_songtext(songtitle, artist, root):
#     for child in root:
#         artist_child = child.find("artist")
#         if "".join(child.attrib.values()) == songtitle and "".join(artist_child.attrib.values()) == artist:
#             songtext = child.find("songtext").text
#     return songtext

# def get_songtitle_child(child):
#     songtitle = "".join(child.attrib.values())
#     return songtitle

# def get_songtitle(songtext, root):
#     for child in root:
#         if get_songtext_child(child) == songtext:
#             songtitle = "".join(child.attrib.values())
#     return songtitle

# def get_artist_child(child):
#     artist_child = child.find("artist")
#     artist = "".join(artist_child.attrib.values())
#     return artist

# def get_artist(songtext, root):
#     for child in root:
#         if get_songtext_child(child) == songtext:
#             artist_child = child.find("artist")
#             artist = "".join(artist_child.attrib.values())
#     return artist


def get_songtext(et_element, songtitle = None, artist = None):
    if songtitle != None and artist != None:
        for child in et_element:
            artist_child = child.find("artist")
            if "".join(child.attrib.values()) == songtitle and "".join(artist_child.attrib.values()) == artist:
                songtext = child.find("songtext").text
    else:
        songtext = et_element.find("songtext").text

    return songtext


def get_songtitle(et_element, songtext = None):
    if songtext != None:
        for child in et_element:
            if get_songtext(child) == songtext:
                songtitle = "".join(child.attrib.values())
    else:
        songtitle = "".join(et_element.attrib.values())
    return songtitle


def get_artist(et_element, songtext = None):
    if songtext != None:
        for child in et_element:
            if get_songtext(child) == songtext:
                artist_child = child.find("artist")
                artist = "".join(artist_child.attrib.values())
    else:
        artist_child = et_element.find("artist")
        artist = "".join(artist_child.attrib.values())
    return artist
    
