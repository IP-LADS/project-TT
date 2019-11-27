""" parser for custom instagram scraper API """
from igramscraper.model import Media

from .utils import get_type


def parse_media(media_in_json):
    """Parse comments from media_json page.

    Args:
      media_in_json (json): json object representing the media content

    Returns: (Media)

    """
    media = Media(media_in_json)

    # add comment info
    comments = parse_comments(media_in_json)
    media.comments_count = len(comments)
    media.comments = '_[COMMENT_SEP]_'.join(comments)  # into a string

    # add carousel info
    carousel = parse_carousel(media_in_json)
    media.carousel_ids = carousel['media_ids']
    media.carousel_types = carousel['media_types']
    media.carousel_thumbnail_urls = carousel['thumbnails']
    media.carousel_image_highres_urls = carousel['image_highres_urls']

    return media


def parse_comments(media_json):
    """Parse comments from media_json page.

    TODO(js3611): Note that this is not fully tested. For example, there might
    be paginated comments, in which I don't know how this code behaves.

    Args:
      media_json (json): json object representing the media content

    Returns:
      comments (List[str]): a list of comments

    """
    comments_attributes = media_json['edge_media_to_parent_comment']

    # iterate over comments
    comments = []
    for edge in comments_attributes['edges']:
        comments.append(edge['node']['text'])

    return comments


def parse_carousel(media_json):
    """Parse carousel from media_json page.

    Args:
      media_json (json): json object representing the media content

    Returns:
      (dict): containing the following keys, were each is a comma separated
        list in string: 'media_ids', 'media_types', 'thumbnails',
        'image_highres_urls'.  If no carousel is found, each string will be
        empty.

    """
    media_ids = []
    media_types = []
    thumbnails = []
    image_highres_urls = []
    if 'edge_sidecar_to_children' in media_json:
        sidecars = media_json['edge_sidecar_to_children']['edges']
        for sidecar in sidecars:
            node = sidecar['node']
            media_ids.append(node['id'])
            media_types.append(get_type(node['__typename']))
            thumbnails.append(node['display_resources'][0]['src'])
            image_highres_urls.append(node['display_resources'][-1]['src'])
    media_ids = ','.join(media_ids)
    media_types = ','.join(media_types)
    thumbnails = ' , '.join(thumbnails)
    image_highres_urls = ' , '.join(image_highres_urls)

    return {
        'media_ids': media_ids,
        'media_types': media_types,
        'thumbnails': thumbnails,
        'image_highres_urls': image_highres_urls,
    }
