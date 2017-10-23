#!/usr/bin/env python
"""An interface for Web Json Apis."""

import sys
import urllib.request
import json
import options

__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.2"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Beta"


class DummyAPI(object):
    """Gotta have docstrings."""

    def __init__(self, options=None):
        """Make sure the options are properly set."""
        self.options = options

    def __call__(self, options=None):
        """Be through."""
        return True

    def main(self):
        """Sanity check with your api keys and info."""
        # print(self.options)
        print(self.basic_get_command())
        return True

    def basic_get_command(self):
        data = None
        with urllib.request.urlopen('https://api.nicehash.com/api') as url:
            data = json.loads(url.read().decode('UTF-8'))
        return data


def main():
    """Launcher for the app."""
    config = options.Options()
    app = DummyAPI(config)

    if app.main():
        sys.exit('Alphagriffin.com | 2017')
    return True

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("and thats okay too.")
        sys.exit(e)
