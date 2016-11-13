#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):

    def __init__(self, logfilename):
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        handled = []
        try:
            fhandler = open(self.logfilename, 'a')
        except IOError as error:
            self.log("target logfile cannot be opened")  
            raise error
                 
        for index, entry in enumerate(self.msgs):
            try: 
                fhandler.write(str(entry) + '\n')
                handled.append(index)
            except IOError as error:  
                self.log(" cannot write to target error")
                break
            except:
                
                self.log("error")
                continue 
        fhandler.close()

        for index in handled[::-1]:
            del self.msgs[index]
