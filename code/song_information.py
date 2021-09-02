"""This module can access the main information of a song stored in a XML file.

   Functions:

   get_songtext(xml.etree.ElementTree.Element) -> string
   or get_songtext(xml.etree.ElementTree.Element, string, string) -> string

   get_songtitle(xml.etree.ElementTree.Elementt) -> string
   or get_songtitle(xml.etree.ElementTree.Elementt, string) -> string

   get_artist(xml.etree.ElementTree.Element) -> string
   or get_artist(xml.etree.ElementTree.Element, string) -> string
"""

def get_songtext(et_element, songtitle=None, artist=None):
    """Finds the songtext of a song.

    Args:
        et_element: A xml.etree.ElementTree.Element. If this is the only passed
            parameter, it has to be a child of an ElementTree.
            If this is not the only passed parameter, it has to be the root of
            an ElementTree.
        songtitle: Optional; A string containing the title of the song which is
            necessary to find the songtext in the XML tree if only the root
            is passed.
        artist: Optional; A string containing the artist of the song which is
            necessary to find the songtext in the XML tree if only the root
            is passed.

    Returns:
        A string containing the corresponding songtext either to the child of
        the tree that was passed or to the songtitle and artist that were
        passed.
    """
    if songtitle is not None and artist is not None:
        for child in et_element:
            artist_child = child.find("artist")
            if ("".join(child.attrib.values()) == songtitle
                    and "".join(artist_child.attrib.values()) == artist):
                songtext = child.find("songtext").text
    else:
        songtext = et_element.find("songtext").text
    return songtext

def get_songtitle(et_element, songtext=None):
    """Finds the songtitle of a song.

    Args:
        et_element: A xml.etree.ElementTree.Element. If this is the only passed
            parameter, it has to be a child of an ElementTree.
            If this is not the only passed parameter, it has to be the root of
            an ElementTree.
        songtext: Optional; A string containing the songtext of a song which
            is necessary to find the songtitle of this songtext in the XML tree
            if only the root is passed.

    Returns:
        A string containing the corresponding songtitle either to the child of
        the tree that was passed or to the songtext that was passed.
    """
    if songtext is not None:
        for child in et_element:
            if get_songtext(child) == songtext:
                songtitle = "".join(child.attrib.values())
    else:
        songtitle = "".join(et_element.attrib.values())
    return songtitle

def get_artist(et_element, songtext=None):
    """Finds the artist of a song.

    Args:
        et_element: A xml.etree.ElementTree.Element. If this is the only passed
            parameter, it has to be a child of an ElementTree.
            If this is not the only passed parameter, it has to be the root of
            an ElementTree.
        songtext: Optional; A string containing the songtext of a song which
            is necessary to find the artist of this songtext in the XML tree
            if only the root is passed.

    Returns:
        A string containing the corresponding artist either to the child of the
        tree that was passed or to the songtext that was passed.
    """
    if songtext is not None:
        for child in et_element:
            if get_songtext(child) == songtext:
                artist_child = child.find("artist")
                artist = "".join(artist_child.attrib.values())
    else:
        artist_child = et_element.find("artist")
        artist = "".join(artist_child.attrib.values())
    return artist
