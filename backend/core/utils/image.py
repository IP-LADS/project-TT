from io import BytesIO
import requests

import numpy as np
import matplotlib.pyplot as plt
import PIL
from PIL import Image


def imresize(x, imsize):
    """ Resize numpy array """
    return np.array(Image.fromarray(x).resize(imsize, PIL.Image.BICUBIC))


def get_thumbnail(url, imsize=None, proxies=None):
    """ download the image and return a numpy array representing the image

    Args:
      url (str): URL to download the image from.
      (optional) imsize (tuple): Resize image, specify in (nx, ny) format.
      (optional) proxies (dict[str,str]): a proxy adress to use for the request
    Returns:
       (np.ndarray): the downloaded image which is resized
    """
    # fetch the rawdata from URL
    response = requests.get(url, proxies=proxies)
    # convert rawdata into an image
    img = Image.open(BytesIO(response.content))
    # resize the image using bicubic interpolation
    if imsize:
        img = img.resize(imsize, PIL.Image.BICUBIC)
    # convert to numpy array so we can process
    img_array = np.array(img)
    # return the numpy array
    return img_array


def show_thumbnail(img, media_caption):
    """ Show thumbnail using matplotlib """
    plt.figure()
    plt.imshow(img)
    plt.axis('off')
    # format long title
    if len(media_caption) > 20:
        media_caption = media_caption[:17] + '...'
    plt.title(media_caption)
    plt.show()
