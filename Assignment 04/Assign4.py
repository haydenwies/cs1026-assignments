from moviedb import MovieDatabase

COMMAND=0
TITLE=1
YEAR=2
REVIEW=3

NEW_COMMAND = 'NEW'
REVIEW_COMMAND = 'REV'
SHOW_COMMAND = 'SHO'
PRINT_COMMAND = 'PRI'


def read_file(input):
    """Reads designated file and performs actions outlined in the file. Parameters: input (name of file)."""

    # SOME CODE MAY NEED TO GO HERE
    mdb = MovieDatabase()

    with open(input,'r') as fh:
        for line in fh:
            data = line.strip().split('-')

            command = data[COMMAND]

            if command == NEW_COMMAND:
                title = data[TITLE]
                year = data[YEAR]

                mdb.add_movie(title, year)

            elif command == REVIEW_COMMAND:
                title = data[TITLE]
                year = data[YEAR]
                review = int(data[REVIEW])

                movie = mdb.find_movie(title, year)

                if movie is not None:
                    movie.add_review(review)

            elif command == SHOW_COMMAND:
                
                mdb.show_all()

            elif command == PRINT_COMMAND:
                title = data[TITLE]
                year = data[YEAR]
                
                movie = mdb.find_movie(title, year)

                if movie is not None:
                    review = movie.long_review()
                    print(review)


def main():
    """Prompts user for name of file and calls read_file."""

    file_name = input("Enter the name of the file: ")
    read_file(input=file_name)


main()