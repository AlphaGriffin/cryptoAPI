#!/usr/bin/env python
"""
A recursive json printer. And other fun stuff.
"""

import os
import sys
import shlex
import struct
import platform
import subprocess
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


class Printer(object):
    """A class that formats a cleaner CLI look."""

    def __init__(self, options):
        """Probably dont need options but you never know."""
        self.options = options
        self.res_x, self.res_y = self._get_terminal_size_windows() if not None else (0,0)

    def __call__(self, data=None):
        """Call this Class without any functions."""
        self.printer(data)
        return True

    def __str__(self):
        """Tie up those loose ends."""
        return str("AG_Printer Ver: {}".format(__version__))

    def printer(self, data=None):
        """Pretty recursive json printer, or line printer."""
        border = '|-|'
        filler = ' '
        spacer = '----'
        blocker = '    '
        scr_size = self.res_x-(len(border)*2)
        if data == None:
            print("{border}{0:{filler}^{size}}{border}".format(
            '#'*scr_size, size=scr_size, border=border, filler=filler
            ))
        if type(data) == str:
            print("{border}{0:{filler}^{size}}{border}".format(
            data[:self.res_x-8], size=scr_size, border=border, filler=filler
            ))
        if type(data) == dict:
            for i in data:
                print("{border}{0:{filler}<{size}}{border}".format(
                i[:self.res_x-4], size=scr_size, border=border, filler=filler
                ))
                try:
                    for x in data[i]:
                        if type(data[i][x]) == dict:
                            try:
                                print("{border}{block}{0:{filler}<{size}}{border}".format(
                                x[:self.res_x-4], size=scr_size-len(spacer), border=border, filler=filler, block=blocker
                                ))
                                for y in data[i][x]:
                                    msg = "{}: {}".format(y, data[i][x][y])
                                    print("{border}{space}{0:{filler}<{size}}{border}".format(
                                    msg[:self.res_x-4], size=scr_size-len(spacer)*2, border=border, filler=filler, space=spacer*2
                                    ))
                            except:
                                pass
                        if type(data[i][x]) == list:
                            try:
                                print("{border}{block}{0:{filler}<{size}}{border}".format(
                                x[:self.res_x-4], size=scr_size-len(spacer), border=border, filler=filler, block=blocker
                                ))
                                for index, y in enumerate(data[i][x]):
                                    msg = "{}: {}".format(y, data[i][x][index])
                                    print("{border}{space}{0:{filler}<{size}}{border}".format(
                                    msg[:self.res_x-4], size=scr_size-len(spacer)*2, border=border, filler=filler, space=spacer*2
                                    ))
                            except:
                                pass
                        else:
                            msg = "{}: {}".format(x, data[i][x])
                            print("{border}{space}{0:{filler}<{size}}{border}".format(
                            msg[:self.res_x-4], size=scr_size-4, border=border, filler=filler, space=spacer
                            ))
                except:
                    pass

    def main(self):
        """Sanity Check."""
        print("ResX: {}, ResY: {}".format(self.res_x, self.res_y))
        return True

    def _get_terminal_size_windows(self):
        """Source: https://gist.github.com/jtriley/1108174"""
        try:
            from ctypes import windll, create_string_buffer
            # stdin handle is -10
            # stdout handle is -11
            # stderr handle is -12
            h = windll.kernel32.GetStdHandle(-12)
            csbi = create_string_buffer(22)
            res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
            if res:
                (bufx, bufy, curx, cury, wattr,
                 left, top, right, bottom,
                 maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
                sizex = right - left + 1
                sizey = bottom - top + 1
                return sizex, sizey
        except:
            # src: http://stackoverflow.com/questions/263890/how-do-i-find-the-width-height-of-a-terminal-window
            try:
                cols = int(subprocess.check_call(shlex.split('tput cols')))
                rows = int(subprocess.check_call(shlex.split('tput lines')))
                return (cols, rows)
            except:
                pass
            pass


def main():
    """Launcher for the app."""
    config = options.Options()
    app = Printer(config)
    if app.main():
        app()
        app("This is just a test")
        app.printer("this test string is clearly way way too long to fit into this field, surely, too long.")
        app(str(app))
        app.printer("AlphaGriffin.com | 2017")
        app()
        dick = {'test': {'thing1': '1', 'Thing2': '2', 'thing3': {'thing4' : '4'}}}
        app(dick)
        app()
        sys.exit('Alphagriffin.com | 2017')
    return True

if __name__ == '__main__':
    try:
        # os.system("mode con cols=80 lines=75")
        os.system("clear")
        main()
    except Exception as e:
        print("and thats okay too.")
        sys.exit(e)
