""" custom instagram library """
import requests
import re
import time

from igramscraper.instagram import Instagram
from igramscraper.exception.instagram_exception import InstagramException
from igramscraper.exception.instagram_not_found_exception import InstagramNotFoundException

from .parser import parse_media


def get_media_by_url(insta_obj, media_url, proxy=None):
    """Get media page content from url. This essentially behaves as
    ``igscraper.Instagram.get_media_by_url``. However, the original code is
    broken  and it cannot fetch the comments and carousel. This code fixes those.

    Args:
      insta_obj (Instagram): instagram object
      media_url (str): an instagram URL of image you want to get the
          information from
      (Optional) proxy (dict): a proxy for the request. Use this to avoid being blocked.
          See ``ProxyPoolExecutor`` for more details

    Returns:
      Media: media object with attributes

    """

    # create a one-off session
    __req = requests.session()
    # set proxy
    if proxy and isinstance(proxy, dict):
        __req.proxies = proxy

    url_regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'  # noqa
    if len(re.findall(url_regex, media_url)) <= 0:
        raise ValueError('Malformed media url')
    url = media_url.rstrip('/') + '/?__a=1'

    # Make request to get the information
    time.sleep(insta_obj.sleep_between_requests)
    response = __req.get(url, headers=insta_obj.generate_headers(insta_obj.user_session))

    if Instagram.HTTP_NOT_FOUND == response.status_code:
        raise InstagramNotFoundException(
            'Media with given code does not exist or account is private.')

    if Instagram.HTTP_OK != response.status_code:
        raise InstagramException.default(response.text, response.status_code)

    # close proxy
    __req.close()

    # handle JSON
    media_array = response.json()
    try:
        media_in_json = media_array['graphql']['shortcode_media']
    except KeyError:
        raise InstagramException('Media with this code does not exist')

    return parse_media(media_in_json)
