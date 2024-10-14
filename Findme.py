import itertools
import random
from datetime import datetime
import argparse
import os
import configparser
from termcolor import colored

CONFIG = {}

# Function to read the configuration file
def read_config(filename):
    if not os.path.isfile(filename):
        print(f"Could not find configuration file {filename}.")
        exit("Exiting...")

    global CONFIG
    config = configparser.ConfigParser()
    config.read(filename)

    # Parse leet mode settings
    CONFIG['LEET'] = {letter: config.get('leet', letter) for letter in {"a", "i", "e", "t", "o", "s", "g", "z"}}
    
    # Parse special characters
    CONFIG['chars'] = config.get('specialchars', 'chars').split(', ')
    
    # Parse number ranges and thresholds
    CONFIG['nums'] = {
        'from': config.getint('nums', 'from'),
        'to': config.getint('nums', 'to'),
        'wcfrom': config.getint('nums', 'wcfrom'),  # Word count minimum
        'wcto': config.getint('nums', 'wcto'),      # Word count maximum
        'threshold': config.getint('nums', 'threshold'),
        'maxsize': config.getint('nums', 'maxsize')
    }

# Improved leet mode conversion
def make_leet(word):
    return ''.join(CONFIG['LEET'].get(c, c) for c in word)

# Enhanced function to generate wordlist
def generate_wordlist(words, add_keywords, special_chars, add_numbers, leet):
    wordlist = set(words)

    # Apply leet mode if enabled
    if leet:
        wordlist.update(make_leet(word) for word in words)

    # Add special characters if enabled
    if special_chars:
        special_characters = CONFIG['chars']
        wordlist.update(word + char for word in words for char in special_characters)

    # Add random numbers if enabled
    if add_numbers:
        wordlist.update(word + str(random.randint(CONFIG['nums']['from'], CONFIG['nums']['to'])) for word in words)

    # Generate complex combinations with special characters and numbers
    combinations = set()
    while len(combinations) < 40000:  # Ensure a minimum of 40,000 combinations
        for word in words:
            random_word = random.choice(list(words))
            random_char = random.choice(CONFIG['chars'])
            random_number = str(random.randint(CONFIG['nums']['from'], CONFIG['nums']['to']))
            combinations.add(random_word + random_char + random_number)

        wordlist.update(combinations)

    # Filter based on word count settings
    wordlist = {word for word in wordlist if CONFIG['nums']['wcfrom'] <= len(word) <= CONFIG['nums']['wcto']}

    # Trim wordlist if it exceeds maximum size
    if len(wordlist) > 100000:
        wordlist = set(list(wordlist)[:100000])

    return wordlist

# Function to validate birthdate in MM/DD/YYYY format
def validate_birthdate(prompt):
    while True:
        birthdate = input(prompt)
        try:
            datetime.strptime(birthdate, "%m/%d/%Y")
            return birthdate
        except ValueError:
            print("\033[31mInvalid date format. Please enter in MM/DD/YYYY format.\033[0m")

# Collect input fields for wordlist generation
def collect_input():
    fields = []

    # Personal info
    name = input("\033[31mTarget Name: \033[0m").strip()
    surname = input("\033[31mTarget surname: \033[0m").strip()
    nickname = input("\033[31mTarget nickname: \033[0m").strip()
    birthdate = validate_birthdate("\033[31mYour birthdate (MM/DD/YYYY): \033[0m")
    fields.extend([name, surname, nickname, birthdate])

    # Partner info
    partner_name = input("\033[31mPartner's name: \033[0m").strip()
    partner_surname = input("\033[31mPartner's surname: \033[0m").strip()
    partner_nickname = input("\033[31mPartner's nickname: \033[0m").strip()
    partner_birthdate = validate_birthdate("\033[31mPartner's birthdate (MM/DD/YYYY): \033[0m")
    fields.extend([partner_name, partner_surname, partner_nickname, partner_birthdate])

    # Ex info
    ex_name = input("\033[31mEx's name: \033[0m").strip()
    ex_surname = input("\033[31mEx's surname: \033[0m").strip()
    ex_nickname = input("\033[31mEx's nickname: \033[0m").strip()
    ex_birthdate = validate_birthdate("\033[31mEx's birthdate (MM/DD/YYYY): \033[0m")
    fields.extend([ex_name, ex_surname, ex_nickname, ex_birthdate])

    # Kids info
    kids_name = input("\033[31mKids' name: \033[0m").strip()
    kids_surname = input("\033[31mKids' surname: \033[0m").strip()
    kids_nickname = input("\033[31mKids' nickname: \033[0m").strip()
    kids_birthdate = validate_birthdate("\033[31mKids' birthdate (MM/DD/YYYY): \033[0m")
    fields.extend([kids_name, kids_surname, kids_nickname, kids_birthdate])

    # Favorite things
    fav_place = input("\033[31mFavorite place: \033[0m").strip()
    fav_food = input("\033[31mFavorite food: \033[0m").strip()
    fav_game = input("\033[31mFavorite game: \033[0m").strip()
    hobby = input("\033[31mHobby: \033[0m").strip()
    fields.extend([fav_place, fav_food, fav_game, hobby])

    # Company name
    company_name = input("\033[31mCompany's name: \033[0m").strip()
    fields.append(company_name)

    # Additional keywords
    add_keywords = input("\033[31mDo you want to add some keywords about the victim? (y/n): \033[0m").lower() == 'y'
    if add_keywords:
        keywords = input("\033[31mEnter keywords (comma separated): \033[0m").split(',')
        fields.extend([kw.strip() for kw in keywords])

    # Special characters, numbers, and leet mode
    special_chars = input("\033[31mDo you want to add special chars at the end of words? (y/n): \033[0m").lower() == 'y'
    add_numbers = input("\033[31mDo you want to add some random numbers at the end of words? (y/n): \033[0m").lower() == 'y'
    leet = input("\033[31mLeet mode? (i.e. password = p4ssw0rd) (y/n): \033[0m").lower() == 'y'

    return fields, name, add_keywords, special_chars, add_numbers, leet

def print_logo():
    logo = r""" 
                      _____ _           _   __  __ _____   _ 
                     |  ___(_)_ __   __| | |  \/  | ____| | |
                     | |_  | | '_ \ / _` | | |\/| |  _|   | |
                     |  _| | | | | | (_| | | |  | | |___  |_|
                     |_|   |_|_| |_|\__,_| |_|  |_|_____| (_)

             |----------------------------------------------------------------------------|
             |                      Created By: Sayantan Saha                             |
             |          Checkout my LinkedIn: https://www.linkedin.com/in/mastersayantan/ |
             |         Lookup at my GitHub Account: https://github.com/MasterSayantan     |
             |----------------------------------------------------------------------------|
    """
    # Define rainbow colors
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']

    # Center the logo and print each line with rainbow colors
    columns, _ = os.get_terminal_size()
    lines = logo.splitlines()
    for i, line in enumerate(lines):
        print(colored(line.center(columns), colors[i % len(colors)], attrs=['bold']))

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Generate a wordlist.')
    parser.add_argument('-i', '--interactive', action='store_true', help='Start interactive mode')
    args = parser.parse_args()

    # Read configuration file for leet mode, special characters, and number ranges
    read_config('findme.cfg')

    # Print logo and author information
    print_logo()

    if args.interactive:
        # Collect input fields and options
        fields, name, add_keywords, special_chars, add_numbers, leet = collect_input()

        # Check if fields are empty
        if not fields or not name:
            print("\033[31mNo valid input collected. Wordlist cannot be generated.\033[0m")
            return

        # Generate the wordlist based on the inputs
        wordlist = generate_wordlist(fields, add_keywords, special_chars, add_numbers, leet)

        # Write the wordlist to a file named after the user's name
        filename = f"{name}.txt"
        if wordlist:
            with open(filename, "w") as f:
                for word in sorted(wordlist):
                    f.write(f"{word}\n")
            print(f"\033[32mWordlist generated successfully and saved to {filename}.\033[0m")
        else:
            print("\033[31mFailed to generate a wordlist. No valid words found.\033[0m")

if __name__ == "__main__":
    main()
