"""This module can access the main information of a song stored in an XML file.

   Functions:

   get_(xml.etree.ElementTree.Element) -> string
   or get_lyrics(xml.etree.ElementTree.Element, string, string) -> string

   get_songtitle(xml.etree.ElementTree.Elementt) -> string
   or get_songtitle(xml.etree.ElementTree.Elementt, string) -> string

   get_artist(xml.etree.ElementTree.Element) -> string
   or get_artist(xml.etree.ElementTree.Element, string) -> string
"""

def get_lyrics(et_element, songtitle=None, artist=None):
    """Finds the lyrics of a song.

    Args:
        et_element: An xml.etree.ElementTree.Element. If this is the only passed
            parameter, it has to be a child of an ElementTree.
            If this is not the only passed parameter, it has to be the root of
            an ElementTree.
        songtitle: Optional; A string containing the title of the song which is
            necessary to find the lyrics in the XML tree if only the root
            is passed.
        artist: Optional; A string containing the artist of the song which is
            necessary to find the lyrics in the XML tree if only the root
            is passed.

    Returns:
        A string containing the corresponding lyrics either to the child of
        the tree that was passed or to the song title and artist that were
        passed.
    """
    if songtitle is not None and artist is not None:
        for child in et_element:
            artist_child = child.find("artist")
            if ("".join(child.attrib.values()) == songtitle
                    and "".join(artist_child.attrib.values()) == artist):
                lyrics = child.find("lyrics").text
    else:
        lyrics = et_element.find("lyrics").text
    return lyrics

def get_songtitle(et_element, lyrics=None):
    """Finds the song title of a song.

    Args:
        et_element: An xml.etree.ElementTree.Element. If this is the only passed
            parameter, it has to be a child of an ElementTree.
            If this is not the only passed parameter, it has to be the root of
            an ElementTree.
        lyrics: Optional; A string containing the lyrics of a song which
            is necessary to find the song title of this lyrics in the XML tree
            if only the root is passed.

    Returns:
        A string containing the corresponding song title either to the child of
        the tree that was passed or to the lyrics that was passed.
    """
    if lyrics is not None:
        for child in et_element:
            if get_lyrics(child) == lyrics:
                songtitle = "".join(child.attrib.values())
    else:
        songtitle = "".join(et_element.attrib.values())
    return songtitle

def get_artist(et_element, lyrics=None):
    """Finds the artist of a song.

    Args:
        et_element: An xml.etree.ElementTree.Element. If this is the only passed
            parameter, it has to be a child of an ElementTree.
            If this is not the only passed parameter, it has to be the root of
            an ElementTree.
        lyrics: Optional; A string containing the lyrics of a song which
            is necessary to find the artist of this lyrics in the XML tree
            if only the root is passed.

    Returns:
        A string containing the corresponding artist either to the child of the
        tree that was passed or to the lyrics that was passed.
    """
    if lyrics is not None:
        for child in et_element:
            if get_lyrics(child) == lyrics:
                artist_child = child.find("artist")
                artist = "".join(artist_child.attrib.values())
    else:
        artist_child = et_element.find("artist")
        artist = "".join(artist_child.attrib.values())
    return artist
