#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):
	return len(string) % 2 == 0

def get_num_char(string, char):
	number_of_char = 0
	for i in string:
		if i == char:
			number_of_char += 1
	return number_of_char


def get_first_part_of_name(name):
	trait = "-"
	position_of_trait = name.index(trait)
	first_name = name[:position_of_trait].capitalize() #Eliminate the rest of the name
	return first_name #Capitalize First Name

def get_random_sentence(animals, adjectives, fruits):
	return ""


if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
