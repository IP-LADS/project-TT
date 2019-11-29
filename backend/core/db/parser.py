import datetime

from core.envs import START_TIME

def parse_comments(comment_row):
    """ Comments """
    # handle the case when the row is "nan"
    if isinstance(comment_row, float):
        return []
    else:
        return comment_row.split('_[COMMENT_SEP]_')


def parse_datetime(time_row):
    return START_TIME + datetime.timedelta(seconds=int(time_row))


def parse_carousel(row):
    medias = []
    for media in zip(
        row['carousel_ids'].split(','),
        row['carousel_types'].split(','),
        row['carousel_thumbnail_urls'].split(','),
        row['carousel_highres_urls'].split(','),
    ):
        medias.append({
            'id': media[0].strip(),
            'type': media[1].strip(),
            'url': media[2].strip(),
            'thumbnail_url': media[3].strip(),
        })
    return medias
