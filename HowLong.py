#!/usr/bin/env python3

__author__ = "Matthew Egan"

from datetime import timedelta
from subprocess import Popen
from sys import argv
from time import time, sleep

class HowLong:
    def __init__(self):
        self.command = " ".join(argv[1:])

    def run(self):
        print("Running", self.command)
        process = Popen(argv[1:])
        start_time = time()

        while process.poll() is None:
            sleep(1)
            print('\033[91m', str(timedelta(seconds=int(time() - start_time))), '\033[0m')

        print("Finished", self.command)

if __name__ == "__main__": HowLong().run()