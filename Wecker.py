#! /usr/bin/env python

__author__ = 'medusa'

import time
import tkSnack

def main():
    print()
    print "Das hier ist ein Timer."
    min = raw_input("Wann willst du erinnert werden? (in Minuten)")
    sec = float(min)*60
    print "Der Timer läuft."
    time.sleep(sec)
    print "RING RING RING"
    s = Sound()
    s.read('sound.mp3')
    s.play()
    print()

main()
