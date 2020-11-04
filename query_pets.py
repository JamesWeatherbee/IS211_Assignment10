#!/usr/bin/python
# -*- coding: utf-8 -*-
# IS211_Assignment 10 query_pets.py

import sqlite3 as sql

connect = sql.connect("pets.db")
with connect:
    cursor = connect.cursor()

    while True:
        number = input('Enter ID number or enter -1 to exit. -> ')
        if number == '-1':
            raise SystemExit

        cursor.execute("SELECT first_name, last_name, person.age, name, breed,"
                    "pet.age, dead FROM person, pet, person_pet "
                    "WHERE person.id = person_pet.person_id AND "
                    "pet.id = person_pet.pet_id AND person.id=(?)", (number))

        person = cursor.fetchall()

        for row in person:
            first_name = row[0]
            last_name = row[1]
            age = row[2]
            pet_name = row[3]
            pet_type = row[4]
            pet_age = row[5]
            dead = row[6]
            if dead == 1:
                # print(f'{first_name} {last_name}, owned a {pet_type} named {pet_name} that was {pet_age} years old.')
                print("{} {}, owned a {} named {} that was {} years old.".format(first_name, last_name, pet_type,
                                                                                 pet_name, pet_age))
            else:
                # print(f'{first_name} {last_name}, owns a {pet_type} named {pet_name} that is {pet_age} years old.')
                print("{} {}, owns a {} named {} that is {} years old.".format(first_name, last_name, pet_type,
                                                                               pet_name, pet_age))

