# FindME - Wordlist Generator Tool

FindME is a customizable wordlist generator tool designed for creating wordlists based on personal and contextual information. It allows you to generate a variety of combinations, including leet speak variations, special characters, and random numbers, making it a versatile tool for security professionals and researchers.

![image](https://github.com/MasterSayantan/FindME/blob/main/Screenshot%202024-10-17%20182415.png)

## Features

- **Customizable Input**: Collects personal, partner, ex-partner, children's, and favorite things information for tailored wordlist generation.
- **Leet Speak Conversion**: Supports leet speak mode, converting letters to numbers (e.g., 'a' to '4', 's' to '5').
- **Special Characters and Numbers**: Option to add special characters and random numbers to the generated words.
- **Combination Generation**: Ensures a minimum of 40,000 combinations using various word parts, characters, and numbers.
- **Word Count Filtering**: Customizable minimum and maximum word length settings.
- **User-Friendly Interface**: Interactive mode that prompts users for necessary inputs.

## How It Works

1. **Configuration**: The tool reads a configuration file (`findme.cfg`) for settings related to leet mode, special characters, and number ranges.
2. **User Input**: In interactive mode, users are prompted to enter personal details, favorite things, and specify their preferences for leet mode, special characters, and random numbers.
3. **Wordlist Generation**:
    - The tool generates a base wordlist from the user input.
    - Applies leet speak transformations if enabled.
    - Adds special characters and random numbers based on user choices.
    - Creates complex combinations ensuring a minimum of 40,000 entries.
4. **Output**: The generated wordlist is saved to a text file named after the user's provided name.

## Installation Requirements

To run the FindME tool, ensure you have Python 3.x installed along with the following libraries:

- `termcolor`: For colored terminal output.
- `configparser`: For reading configuration files.

## Installation Steps

1. **Clone this repository**:
   ```bash
   git clone https://github.com/MasterSayantan/FindME.git
   cd FindME
   pip install -r requirements.txt
   ```
## Usage

1. Run in Interactive Mode:
   ``` bash
   python3 Findme.py -i
   ```

   
