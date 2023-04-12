class Movie:


    def __init__(self, title, year):
        self.__title = title
        self.__year = year
        self.__reviews = {
            1:0,
            2:0,
            3:0,
            4:0,
            5:0
        }
    

    def __calc_average(self):
        """Calculates average movie rating /5 rounded to one decimal. Returns average as float."""

        rating = 0
        count = 0

        for x in self.__reviews:
            count += self.__reviews[x]
            rating += x*self.__reviews[x]

        try:
            avg_rating = round(rating/count, 1)

            return(avg_rating)

        except ZeroDivisionError:

            return(0.0)


    def get_title(self):
        """Returns title of movie."""

        return(self.__title)

    
    def get_year(self):
        """Returns year of movie."""

        return(self.__year)


    def short_review(self):
        """Returns string containing short review of moview formatted as TITLE (YEAR): RATING"""


        avg_rating = self.__calc_average()

        return(f"{self.__title} ({self.__year}): {avg_rating}/5")

    
    def long_review(self):
        """Returns longs review breaking down number of each star review."""
        avg_rating = self.__calc_average()
        ln_one = f"{self.__title} ({self.__year})\n"
        ln_two = f"Average review: {avg_rating}/5\n"
        ln_three = f"*****: {self.__reviews[5]}\n"
        ln_four = f"**** : {self.__reviews[4]}\n"
        ln_five = f"***  : {self.__reviews[3]}\n"
        ln_six = f"**   : {self.__reviews[2]}\n"
        ln_seven = f"*    : {self.__reviews[1]}"

        return(ln_one + ln_two + ln_three + ln_four + ln_five + ln_six + ln_seven)


    def add_review(self, rating):
        """Adds review to corresponding section of review dictionary. Parameters: rating (intiger representing number of stars for rating)."""

        if 1 <= rating <= 5:
            self.__reviews[rating] += 1
        else:
            pass