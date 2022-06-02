#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Pet:
    kind = "mammal"
    n_pets = 0
    pet_names = [] 

    def __init__(self, spec, name):
        self.spec = spec
        self.name = name
        self.legs = 4

