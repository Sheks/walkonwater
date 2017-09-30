# -*- coding: UTF-8 -*-
# pylint: disable=wildcard-import
from .production import *
try:
    from .local import *
except ImportError:
    pass
try:
    from .development import *
except ImportError:
    pass
from .version import *
