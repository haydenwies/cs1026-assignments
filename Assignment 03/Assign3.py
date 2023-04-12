# COMPSCI - Assignment 03
# Hayden Wies
# Program takes in a csv file representing votes collected from an election and uses an IRV algorythm to determine a winner to the election. Results are printed in order of elimination process meaning the last id to be listed in the result is the wining contender.

# P.S. I know I didn't incorporate all the defined algorithms seperately into this program as specified in the assignment, however I chose to do this because I found some of the required functions (such as determining the winner of a tie) could be done with a single line of code, which I found more efficient than writing a seperate function. Hopefully you still find everything straight forward and easy to read. Thank you for acknowledging this disclaimer.


def get_data():
    """Prompts user for csv file and creates a nested array of every line entry as the var 'data'. Returns data."""

    data = []

    # Prompt user for file name.
    file_name = input("Enter the name of the file: ")

    # Locate file, format and add to data variable. Formatted as array of numbers for each line in file.
    with open(file_name, "r") as votes:
        for line in votes:
            formatted_line = line.strip().split(",")
            formatted_line = list(filter(None, formatted_line))
            for i in range(len(formatted_line)):
                formatted_line[i] = int(formatted_line[i])
            data.append(formatted_line)

    return(data)


def remove_one(data, remove_order, removed):
    """Used to remove a single candidate id from the data array and return a new version. Parameters: data (candidate data), remove_order (ordered list of which sequence candidated were removed), remove (id of candidate to be removed from data). Returns updated data and remove_order."""

    # Add removed id to remove_order variable.
    remove_order.append(removed)

    # Loop through each entry of data and edit it to remove the specified id.
    for idx, vote in enumerate(data):
        data[idx] = list(filter(lambda x: x != removed, vote))

    return(data, remove_order)


def remove_all(data, remove_order, winner):
    """Used to remove all candidate ids from the data array except a specified id and return a new version. Parameters: data (candidate data), remove_order (ordered list of which sequence candidated were removed), winner (id of candidate to not be removed from data). Returns updated data and remove_order."""

    container = []

    # Loop through data and add id value to container if it doesn't equal specified winning id.
    for vote in data:
        for id in vote:
            if id not in container and id != winner:
                container.append(id)

    # Loop through each array in data and remove all numberes except for specified winner.
    for idx, vote in enumerate(data):
        data[idx] = list(filter(lambda x: x == winner, vote))

    # Append all removed ids to remove_order sorted in ascending order.
    remove_order += sorted(container)
    
    return(data, remove_order)


def compare_votes(data, remove_order):
    """Reconstructs data to identify most and least voted for candidate(s), then removes specified candidate(s) based on conditions. Parameters: data (candidate data), remove_order (ordered list of which sequence candidated were removed). Returns updated data and remove_order."""
    vote_tally = {}
    vote_percent = {}
    vote_total = 0

    # Create dictionary which keeps track of how many first place votes each id recieved.
    for vote in data:
        try:
            if vote[0] in vote_tally:
                vote_tally[vote[0]] += 1
            else:
                vote_tally[vote[0]] = 1
            vote_total += 1
        except IndexError:
            continue
    
    # Convert previous dictionary to percentages.
    for vote in vote_tally:
        vote_percent[vote] = vote_tally[vote] / vote_total
    
    # Flip percent array and group ids that have the same percent value.
    flipped_dict = {}
    for key, value in vote_percent.items():
        if value not in flipped_dict:
            flipped_dict[value] = [key]
        else:
            flipped_dict[value].append(key)

    # Retrieve min and max percentages and associated values.
    min_percent = min(flipped_dict)
    min_id = flipped_dict[min_percent]
    max_percent = max(flipped_dict)
    max_id = flipped_dict[max_percent]

    # If there is a winner by majority, remove all ids except winner.
    if max_percent > .5:
        winner = max_id[0]
        data, remove_order = remove_all(data, remove_order, winner)
    
    # If there is a tie, set candidate with highest id to be removed.
    elif len(min_id) > 1:
        removed = max(min_id)
        data, remove_order = remove_one(data, remove_order, removed)
    
    # Otherwise, remove candidate with least amount of first place votes.
    else:
        removed = min_id[0]
        data, remove_order = remove_one(data, remove_order, removed)

    return(data, remove_order)
    

def count_ids(data):
    """Used to count the number of ids/candidates remaining in given data. Parameters: data (candidate data). Returns intiger representing number of candidates left in data."""

    id_counter = []

    # Loop through data and add all unique ids to array.
    for vote in data:
        for id in vote:
            if id not in id_counter:
                id_counter.append(id)

    # Return size of array representing number of unique ids within data.
    return(len(id_counter))


def get_last(data):
    """Once certain only one id remains in data, used to retrieve that candidate id. Parameters: data (candidate data). Returns intiger representing the id of last candidate from provided date."""

    last_id = None

    # Loop through data and set last_id to the remaining id within the data set.
    for vote in data:
        if vote != []:
            last_id = vote[0]

    return(last_id)
            

def main():
    data = None
    remove_order = []
    
    # Prompt user for file name and retrieve data.
    data = get_data()

    # Run through elimination process until only one candidate remains.
    id_counter = None
    while id_counter != 1:
        data, remove_order = compare_votes(data, remove_order)
        id_counter = count_ids(data)
    
    # Add winner to end of remove_order array.
    remove_order.append(get_last(data))

    # Convert array to printable format and log results.
    converted_array = [str(element) for element in remove_order]
    converted_string = ", ".join(converted_array)
    print(f"Elimination order: {converted_string}")


main()