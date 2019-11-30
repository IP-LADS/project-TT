""" Scraper to Information related to persistence """
import shutil
import os
import pathlib

import pandas as pd

from core.db.models import MediaImage

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


def aggregate_dataset(data_dir):
    """ combine csvs from hierarchical directories into one under `data_dir`

    Args:
      data_dir (str): the directory for data. This should be
      `/path/to/project/project_TT/data`

    """

    # create dataframe from all csvs
    data_path = pathlib.Path(data_dir)
    csvs = [k for k in data_path.rglob('*_location.csv')]
    dfs = []
    for csv in csvs:
        df = pd.read_csv(csv, quotechar="'")
        dfs.append(df)
    dataset = pd.concat(dfs, ignore_index=True)

    target_csv = data_path / 'data.csv'

    # if data.csv already exists, update the table
    if target_csv.exists():
        existing_ids = pd.read_csv(target_csv, quotechar="'").media_id
        new_data = dataset[~dataset.media_id.isin(existing_ids)]
        new_data.to_csv(
            target_csv, quotechar="'",
            mode='a', header=False, index=False)
        print(f'Appended {len(new_data)} elements to data.csv')
    else :
        existing_ids = []
        new_data = dataset
        new_data.to_csv(target_csv, quotechar="'", index=False)
        print('Created data.csv')

    # create directories
    image_path = data_path / 'images'
    thumbnail_path = data_path / 'thumbnails'
    image_path.mkdir(exist_ok=True)
    thumbnail_path.mkdir(exist_ok=True)

    # copy images
    existing_ids = list(existing_ids)
    for img in data_path.rglob('images/*.jpeg'):
        img_id = os.path.basename(img).split('.')[0]
        if img_id in existing_ids:
            continue
        if str(img).find(str(image_path)) > -1:
            continue

        shutil.copy2(img, image_path / os.path.basename(img))

    # copy thumbnails
    for img in data_path.rglob('thumbnails/*.jpeg'):
        img_id = os.path.basename(img).split('.')[0]
        if img_id in existing_ids:
            continue
        if str(img).find(str(thumbnail_path)) > -1:
            continue

        shutil.copy2(img, thumbnail_path / os.path.basename(img))

    return dataset, data_path


def load_dataset(root_dir, load_image=False, load_thumbnail=False):
    # list to keep track of them
    root_dir = pathlib.Path(root_dir)
    dataset = pd.read_csv(root_dir / 'data/data.csv', quotechar="'")
    media_images = []
    for _, row in dataset.iterrows():
        media_image = MediaImage.create_from_row(row)
        if load_image:
            media_image.load_image(root_dir=root_dir)
        if load_thumbnail:
            media_image.load_thumbnail(root_dir=root_dir)
        media_images.append(media_image)
    return media_images
