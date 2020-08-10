#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import curses

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, 'おめでとう！うまくpython3の実行環境がセットアップされています。')
    stdscr.refresh()
    stdscr.getkey()

if __name__ == '__main__':
    curses.wrapper(main)
