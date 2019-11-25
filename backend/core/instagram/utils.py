""" utility and helpers for custom instagram library """


def get_type(typename):
    if typename == 'GraphImage':
        return 'image'
    elif typename == 'GraphVideo':
        return 'video'
