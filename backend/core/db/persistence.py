""" Scraper to Information related to persistence """
import shutil
import os
import pathlib

import pandas as pd


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


def create_dataset(data_dir):
    """ combine csvs from hierarchical directories into one under `data_dir`

    Args:
      data_dir (str): the directory for data. This should be
      `/path/to/project/project_TT/data`

    """

    # create csv
    data_path = pathlib.Path(data_dir)
    csvs = [k for k in data_path.rglob('*_location.csv')]
    dfs = []
    for csv in csvs:
        df = pd.read_csv(csv, quotechar="'")
        dfs.append(df)
    dataset = pd.concat(dfs, ignore_index=True)
    dataset.to_csv(
        os.path.join(data_dir, 'data.csv'), quotechar="'", index=False)

    # create directories
    image_path = data_path / 'images'
    thumbnail_path = data_path / 'thumbnails'
    image_path.mkdir(exist_ok=True)
    thumbnail_path.mkdir(exist_ok=True)

    # copy images
    for img in data_path.rglob('images/*.jpeg'):
        if str(img).find(str(image_path)) > -1:
            continue
        shutil.copy2(img, image_path / os.path.basename(img))

    # copy thumbnails
    for img in data_path.rglob('thumbnails/*.jpeg'):
        if str(img).find(str(thumbnail_path)) > -1:
            continue
        shutil.copy2(img, thumbnail_path / os.path.basename(img))

    return dataset, data_path
