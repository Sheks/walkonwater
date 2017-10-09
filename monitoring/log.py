# -*- coding: utf-8 -*-
import logging


from walkonwater.settings import VERSION


class AppInfoContextFilter(logging.Filter):
    def filter(self, record):
        record.origin = 'walkonwater'
        record.version = VERSION
        return True
