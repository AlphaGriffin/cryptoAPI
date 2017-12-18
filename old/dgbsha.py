#!/usr/bin/env python
"""An interface for the dgb-sha.theblocksfactory.com mining program."""

import os
import sys
import urllib.request
import json

__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.2"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Beta"


class DGB_SHA(object):
    """Access to the Blockfactory API."""

    def __init__(self, options=None):
        """Use the options to load your API key."""
        self.options = options
        self.api = self.options.blockfactory_api

    def main(self):
        """Sanity Check."""
        print(self.options)
        return True

    ## Private Methods ##
    def my_account(self):
        """Should be entry level here. Make it easy."""
        msg = "https://dgb-sha.theblocksfactory.com/api.php?api_key={}".format(self.api)
        # print("Requesting this URL: {}".format(msg))
        with urllib.request.urlopen(msg) as url:
            data = json.loads(url.read().decode('UTF-8'))
        # print("Completed Api request")
        return data



def main():
    """Launcher for the app."""
    app = DGB_SHA()

    if app.main():
        y = app.my_account()
        sys.exit('Alphagriffin.com | 2017')
    return True


if __name__ == '__main__':
    main()
