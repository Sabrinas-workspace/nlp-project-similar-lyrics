"""This module works only with XML corpora and contains three functions which
all are used to easily get the songtext, title or artist of a song."""

def get_songtext(et_element, songtitle = None, artist = None):
    if songtitle is not None and artist is not None:
        for child in et_element:
            artist_child = child.find("artist")
            if ("".join(child.attrib.values()) == songtitle
                    and "".join(artist_child.attrib.values()) == artist):
                songtext = child.find("songtext").text
    else:
        songtext = et_element.find("songtext").text

    return songtext


def get_songtitle(et_element, songtext = None):
    if songtext is not None:
        for child in et_element:
            if get_songtext(child) == songtext:
                songtitle = "".join(child.attrib.values())
    else:
        songtitle = "".join(et_element.attrib.values())
    return songtitle


def get_artist(et_element, songtext = None):
    if songtext is not None:
        for child in et_element:
            if get_songtext(child) == songtext:
                artist_child = child.find("artist")
                artist = "".join(artist_child.attrib.values())
    else:
        artist_child = et_element.find("artist")
        artist = "".join(artist_child.attrib.values())
    return artist
