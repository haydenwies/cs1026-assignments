# COMPSCI - Assignment 02
# Hayden Wies
# Program will convert names to a Soundex encoding, which is used to compare names that sound similar by matching these codes to eachother

from ast import NameConstant
import re


# Contains valued specified by soundex key (position in array is each letter's replacement digit)
soundex_key = [
    ["a", "e", "i", "o", "u", "y", "h", "w"],
    ["b", "f", "p", "v"],
    ["c", "g", "j", "k", "q", "s", "x", "z"],
    ["d", "t"],
    ["l"],
    ["m", "n"],
    ["r"]
]


def soundex_convert(name):
    """soundex_convert -> Converts a given name into its corresponding Soundex code. Parameters -> name: Must be type str.lower(). Returns -> Soundex encoding of name provided in parameter (contains duplicate numbers, longer than 4) as type str."""

    # Value that will contain the converted string
    name_converted = name[:1].lower()
    # Value that has the first letter of the name removed and will be converted into numbers 
    name = name.lower()

    # Itterate through each letter of the name_remainder
    for letter in name:
        i = 0
        # Compare each item in the soundex_key with the letter being evaluated
        for digit in soundex_key:
            # If item contains the letter being evaluated, add the replacement digit (i) to name_converted
            # Exit the loop for efficiency
            if letter in digit:
                name_converted = name_converted + str(i)
                break
            # If item doesn't contain letter being evaluated, add to counter and repeat process
            else:
                i += 1

    return (name_converted)


def soundex_remove_duplicates(name):
    """soundex_remove_duplicates -> Takes return value from soundex_convert and removes duplicate numbers. Parameters -> name: Must be type str in format returned from soundex_convert. Returns -> Soundex encoding provided in parameter with removed instances of duplicate numbers."""

    # Value to contain string with no duplicates
    no_duplicate = ""
    
    # Itterate through each letter in name
    i = 0
    for letter in name:
        # Add character to no_duplicates if it doesn't equal the character that follows it
        try:
            if letter != name[i+1]:
                no_duplicate = no_duplicate + letter
        except IndexError:
            no_duplicate = no_duplicate + letter
        
        i += 1

    # Remove all instances of 0
    no_duplicate = no_duplicate.replace("0", "")

    # Check if string contains any numbers
    if len(no_duplicate) > 1:
        # Check if corresponding number of leading letter is equal to first digit in string
        i = 0
        for digit in soundex_key:
            if no_duplicate[0] in digit:
                if str(i) == no_duplicate[1]:
                    # If yes, remove first digit of string
                    no_duplicate = no_duplicate[:1] + no_duplicate[2:]
            else:
                i += 1
    else:
        # Set first digit of string equal to corresponding number of leading character
        i = 0
        for digit in soundex_key:
            if no_duplicate[0] in digit:
                no_duplicate = no_duplicate + str(i)
            else:
                i += 1

    return (no_duplicate)


def soundex_shortened(name):
    """soundex_shortened -> Takes return value from soundex_remove_duplicates and converts it to length of 5. Parameters -> name: Must be type str in format returned by soundex_remove_duplicates. Returns -> Soundex encoding provided by parameter modified to be length of 5 (including leading letter and 4 trailing intigers.)"""

    # Value to contain shortened string
    shortened_name = ""

    # If length of name if less than 4, add enough zeros to make it 4
    if len(name) < 4:
        zeros = 4 - len(name)
        shortened_name = name + "0"*zeros
    # If length of name is 4, return name
    elif len(name) == 4:
        shortened_name = name
    # If length of name is greater than 4, remove all characters past the 4th character
    else:
        shortened_name = name[:4]

    return (shortened_name)


def main_prompt():
    """main_prompt -> Prompts user for list of names, ends when user types DONE. Returns -> List of names converted to type str.lower()."""

    name_list = []
    name = ""

    print("Enter names, one on each line. Type DONE to quit entering names.")

    while name != "DONE":
        name = input()

        # Prevent DONE from being added at the end of name_list
        if name != "DONE":
            # Remove accidental punctuation
            clean_name = re.sub("[^A-Za-z0-9 ]+", "", name)
            # Add to the current name list
            name_list.append(clean_name)

    return (name_list)
    

def main_soundex(name_list):
    """main_soundex -> Compiles functions predefines with leading word 'soundex'. Parameters -> name_list: Must be list formatted by main_prompt. Returns -> List of tuples formatted as [[soundex_encoding, name]]."""

    # List for holding converted names
    converted_name_list = []

    # Itterate through each name and apply the soundex algorythm to convert it into a comparable value
    for name in name_list:
        converted_name = soundex_convert(name)
        no_duplicate_name = soundex_remove_duplicates(converted_name)
        soundex_code = soundex_shortened(no_duplicate_name)
        
        # Create object with initial name and it's matching soundex encoding
        converted_name_list.append([soundex_code, name])
    
    return (converted_name_list)


def main_compare(converted_name_list):
    """main_compare -> Compares all names and corresponding soundex encodings to check which sound similar. Parameters -> converted_name_list: List formatted by main_soundex. Returns -> List of tuples which include the name and soundex encoding of 2 unique names that sound the same."""

    # List for holding matches
    matches = []

    # Itterate list of name objects (with name and soundex_code property)
    for name in converted_name_list:
        # List to hold all name objects that have the same soundex_code
        match = []

        # Itterate through name list again and add matches to list
        # Skip name that is already being compared
        for compare_name in converted_name_list:

            # Add name that's being compared to list
            match.append(name)

            if name[0] == compare_name[0] and name[1] != compare_name[1]:
                match.append(compare_name)
                # Sort match and add to matches if it contains more than one name object
                # All match lists contain at least one name object from initial append (match.append(name))
                sorted_match = []
                sorted_match.append(min(match))
                sorted_match.append(max(match))
                if sorted_match not in matches and len(match) > 1:
                    matches.append(sorted_match)
            match.clear()

    return (matches)


def main():
    # Call prompt to create a name list
    name_list = main_prompt()
    # Call convert_name_list to create a list of objects, each which have a name and soundex_code attribute
    converted_name_list = main_soundex(name_list)
    # Call compare to create a list of array of matching 
    matches = main_compare(converted_name_list)

    statements = []
    for match in matches:
        statements.append(f"{match[0][1]} and {match[1][1]} have the same Soundex encoding.")
    statements.sort()
    for statement in statements:
        print(statement)



main()