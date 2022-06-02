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


tom = Pet("cat", "Tom")
avocado = Pet("dog", "Avocado")
ben = Pet("goldfish", "Benjamin")

Pet.n_pets += 3
Pet.n_pets
tom.n_pets
avocado.n_pets
ben.n_pets

tom.n_pets += 1
avocado.n_pets += 1
ben.n_pets += 1
Pet.n_pets
tom.n_pets
avocado.n_pets
ben.n_pets

ben.kind = "fish"
Pet.kind
tom.kind
avocado.kind
ben.kind

Pet.pet_names
tom.pet_names
avocado.pet_names
ben.pet_names

tom.pet_names = ["Tom"]
avocado.pet_names = ["Avocado"]
ben.pet_names = ["Benjamin"]
Pet.pet_names
tom.pet_names
avocado.pet_names 
ben.pet_names
