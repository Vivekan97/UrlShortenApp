# a module that has the bit.ly shortening approach
from pyshorteners import Shortener
from typing import Union  # for type hinting

shortener_instance = Shortener()  # an instance of the Shortener


# for url shortening purpose
def get_shortened_url(full_url: str) -> Union[str, None]:
    # if it is an empty string
    if len(str(full_url)) < 1:
        return full_url
    # getting the shortened url
    try:
        return shortener_instance.tinyurl.short(str(full_url))
    # in case of any error returning None
    except Exception as ex:
        print(f"Shortening Function - {full_url} - ", ex)
        return None


# for retrieving full url from short url
def get_long_url(short_url: str) -> Union[str, None]:
    # if it is an empty string
    if len(str(short_url)) < 1:
        return short_url
    # retrieving the url
    try:
        return shortener_instance.tinyurl.expand(str(short_url))
    # in case of any error returning None
    except Exception as ex:
        print(f"Retrieving Function - {short_url} - ", ex)
        return None
