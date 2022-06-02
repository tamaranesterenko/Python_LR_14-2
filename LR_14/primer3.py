#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class River:
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        River.append(self)

    def get_info(self):
        print("Длина{0} равна {1} км".format(self.name, self.length))
