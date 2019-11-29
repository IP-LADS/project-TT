import os
from PIL import Image

from core.envs import IMAGE_DIR, THUMBNAIL_DIR

from .parser import (
    parse_carousel,
    parse_comments,
    parse_datetime,
)


class User:
    def __init__(self, id, username, full_name):
        if isinstance(id, float):
            id = ""
        if isinstance(username, float):
            username = ""
        if isinstance(full_name, float):
            full_name = ""

        self.id = id
        self.username = username
        self.full_name = full_name

    def __str__(self):
        return f"User({self.username})"


class Location:
    def __init__(self, id, name, slug):
        if isinstance(id, float):
            id = ""
        if isinstance(name, float):
            name = ""
        if isinstance(slug, float):
            slug = ""

        self.id = id
        self.name = name
        self.slug = slug

    def __str__(self):
        return f"Location({self.name})"


class Media:
    """ Abstract class representing Media object """
    def __init__(
        self,
        id,
        media_code,
        media_link,
        media_type,
        time,
        likes_count,
        caption,
        comments,
        user,
        location,
    ):
        self.id = id
        self.media_code = media_code
        self.media_link = media_link
        self.media_type = media_type
        self.time = time
        self.likes_count = likes_count
        self.caption = caption
        self.comments = comments
        self.user = user
        self.location = location

    def __attr_str__(self):
        return (
            f"id={self.id},"
            f"date={self.time.strftime('%Y-%m-%d')},"
            f"likes={self.likes_count},"
            f"user={self.user},"
            f"loc={self.location}"
        )

    def __str__(self):
        return f"Media({self.__attr_str__()})"


class MediaImage(Media):
    """ Concrete class representing image media """
    def __init__(
        self,
        id,
        media_code,
        media_link,
        media_type,
        time,
        likes_count,
        caption,
        comments,
        user,
        location,
        image_url,
        thumbnail_url,
        image=None,
        thumbnail=None,
    ):
        super().__init__(
            id,
            media_code,
            media_link,
            media_type,
            time,
            likes_count,
            caption,
            comments,
            user,
            location,
        )
        self.image_url = image_url
        self.thumbnail_url = thumbnail_url
        self.image = image
        self.thumbnail = thumbnail

    def load_image(self, root_dir=""):
        self.image = Image.open(
            os.path.join(root_dir, IMAGE_DIR, f"{self.id}.jpeg"))
        return self.image

    def load_thumbnail(self, root_dir=""):
        self.thumbnail = Image.open(
            os.path.join(root_dir, THUMBNAIL_DIR, f"{self.id}.jpeg"))
        return self.thumbnail

    @staticmethod
    def create_from_row(row):
        user = User(
            row['user_id'],
            row['username'],
            row['user_full_name'],
        )
        location = Location(
            row['location_id'],
            row['location_name'],
            row['location_slug'],
        )
        image_url = row['img_highres_url']
        thumbnail_url = row['img_thumbnail_url']
        return MediaImage(
            row['media_id'],
            row['media_code'],
            row['media_link'],
            row['type'],
            parse_datetime(row['created_time']),
            row['likes_count'],
            row['caption'],
            parse_comments(row['comments']),
            user,
            location,
            image_url,
            thumbnail_url,
        )

    def __str__(self):
        return f"MediaImage({self.__attr_str__()})"


class MediaVideo(Media):
    """ Concrete class representing video media """
    def __init__(
        self,
        id,
        media_code,
        media_link,
        media_type,
        time,
        likes_count,
        caption,
        comments,
        user,
        location,
        video_url,
        thumbnail_url,
    ):
        super().__init__(
            id,
            media_code,
            media_link,
            media_type,
            time,
            likes_count,
            caption,
            comments,
            user,
            location,
        )
        self.video_url = video_url
        self.thumbnail_url = thumbnail_url

    def load_image(self, root_dir=""):
        image = Image.open(os.path.join(root_dir, IMAGE_DIR, self.id))
        return image

    def load_thumbnail(self, root_dir=""):
        thumbnail = Image.open(
            os.path.join(root_dir, THUMBNAIL_DIR, self.id))
        return thumbnail

    @staticmethod
    def create_from_row(row):
        video_url = row['img_highres_url']
        thumbnail_url = row['img_thumbnail_url']
        user = User(
            row['user_id'],
            row['username'],
            row['user_full_name'],
        )
        location = Location(
            row['location_id'],
            row['location_name'],
            row['location_slug'],
        )
        return MediaVideo(
            row['media_id'],
            row['media_code'],
            row['media_link'],
            row['type'],
            parse_datetime(row['created_time']),
            row['likes_count'],
            row['caption'],
            parse_comments(row['comments']),
            user,
            location,
            video_url,
            thumbnail_url,
        )

    def __str__(self):
        return f"MediaVideo({self.__attr_str__()})"


class MediaCarousel(Media):
    """ Concrete class representing carousel media """
    def __init__(
        self,
        id,
        media_code,
        media_link,
        media_type,
        time,
        likes_count,
        caption,
        comments,
        user,
        location,
        medias,
    ):
        super().__init__(
            id,
            media_code,
            media_link,
            media_type,
            time,
            likes_count,
            caption,
            comments,
            user,
            location,
        )
        self.medias = medias

    @staticmethod
    def create_from_row(row):
        user = User(
            row['user_id'],
            row['username'],
            row['user_full_name'],
        )
        location = Location(
            row['location_id'],
            row['location_name'],
            row['location_slug'],
        )
        return MediaCarousel(
            row['media_id'],
            row['media_code'],
            row['media_link'],
            row['type'],
            parse_datetime(row['created_time']),
            row['likes_count'],
            row['caption'],
            parse_comments(row['comments']),
            user,
            location,
            parse_carousel(row),
        )

    def __str__(self):
        return f"MediaCarousel({self.__attr_str__()})"
