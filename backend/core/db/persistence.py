""" Information related to persistence """

DATA_ATTRIBUTES = [
    'media_id',
    'media_code',
    'media_link',
    'user_id',
    'username',
    'user_full_name',
    'type',
    'created_time',
    'likes_count',
    'img_thumbnail_url',
    'img_highres_url',
    'carousel_ids',
    'carousel_types',
    'carousel_thumbnail_urls',
    'carousel_highres_urls',
    'caption',
    'comments_count',
    'comments',
    'location_id',
    'location_name',
    'location_slug',
]


def media_to_row(media):
    """ Convert media object to a row in dataset, with default values.

    Args:
      media (igscraper.Media): media object

    Returns:
      row (List[str]): a list of string

    """
    if hasattr(media, 'thumbnail_src'):
        media.image_thumbnail_url = media.thumbnail_src

    # check if media has carousels extracted
    if not hasattr(media, 'carousel_ids'):
        media.carousel_ids = ''
        media.carousel_types = ''
        media.carousel_thumbnail_urls = ''
        media.carousel_image_highres_urls = ''

    row = [
        media.identifier,
        media.short_code,
        media.link,
        media.owner.identifier,
        media.owner.username,
        media.owner.full_name,
        media.type,
        media.created_time,
        media.likes_count,
        media.image_thumbnail_url,
        media.image_high_resolution_url,
        media.carousel_ids,
        media.carousel_types,
        media.carousel_thumbnail_urls,
        media.carousel_image_highres_urls,
        media.caption,
        media.comments_count,
        media.comments,
        media.location_id,
        media.location_name,
        media.location_slug,
    ]
    return row
