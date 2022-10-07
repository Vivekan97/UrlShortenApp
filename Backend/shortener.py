from pyshorteners import Shortener
from typing import Union

shortener_instance = Shortener()

def get_shortened_url(full_url:str) -> Union[str, None]:
    if len(full_url)<1:
        return full_url
    try:
        return shortener_instance.tinyurl.short(full_url)
    except:
        return None


def get_long_url(short_url:str) -> Union[str, None]:
    if len(short_url)<1:
        return short_url
    try:
        return shortener_instance.tinyurl.expand(short_url)
    except:
        return None
