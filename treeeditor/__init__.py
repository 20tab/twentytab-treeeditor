VERSION = (0, 2)
__version__ = '.'.join(map(str, VERSION))
DATE = "2014-06-09"

try:
    from . import conf
except:
    pass
