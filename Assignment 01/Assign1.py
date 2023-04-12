# COMPSCI 1026 - Assignment 01
# Hayden Wies
# Program us used to calculate the "feels like" tempterature which includes humidex or wind chill.
# User is prompted to enter basic information such as raw temperature and wind speed (if temperaure falls in certain range) or dew point (if temperature falls in certain range).
# Program then runs calculations based on this information and returns the "feels like" temperature, along with any heat, cold dependent health warnings.

import math


# --- calc_cold_temp --- #
# Invoked in calculator when temperature falls in specified range (-50 <= temp <= 0)
def calc_cold_temp(temp: float):
    
    try:
        # Prompt user for wind velocity
        wind_velocity = float(input('Enter a wind speed between 1 and 99 km/h: '))
    except ValueError:
        # Input can't be converted to float
        # Invoke recursion to run function from start
        print('That wind speed is invalid.')
        calc_cold_temp(temp)

    # Will execute if wind velocity falls in range (1 <= wind_velocity <= 99) 
    if 1 <= wind_velocity <= 99:
        # Calculates wind chill using wind_velocity
        # wind_chill is rounded to whole number
        wind_chill = round(13.12 + (0.6125 * temp) - (11.37 * (wind_velocity**0.16)) + (0.3965 * temp * (wind_velocity**0.16)))
        
        # Sends a print statement to the user depending on the value of the wind chill
        if 0 >= wind_chill >= -9:
            print(f'The windchill is {wind_chill}. Low risk.')
        elif -10 >= wind_chill >= -27:
            print(f'The windchill is {wind_chill}. Moderate risk.')
        elif -28 >= wind_chill >= -39:
            print(f'The windchill is {wind_chill}. High Risk. Skin can freeze in 10-30 minutes.')
        else:
            print(f'The windchill is {wind_chill}. Very High Risk. Skin can freeze in under 10 minutes.')

    else:
        # Entered wind velocity is out of range (1 <= wind_velocity <= 99)
        # Invoke recursion to run function from start
        print('That wind speed is invalid.')
        calc_cold_temp(temp)


# --- calc_warm_temp --- #
# Invoked in calculator when 20 <= temp <= 50
def calc_warm_temp(temp: float):
    
    try:
        # Prompt user for dew point
        dew_pt = float(input('Enter the dewpoint between -50 and 50: '))
    except ValueError:
        # Input can't be converted to float
        # Invoke recursion to run function from start
        print('That dew point is invalid.')
        calc_warm_temp(temp)

    # Will execute if dew point falls in range (-50 <= dew_pt <= 50) 
    if -50 <= dew_pt <= 50 and dew_pt <= temp:
        # Calculates humidex using dew_pt
        # humidex is rouded to whole number
        f = 6.11 * math.exp(5417.7530 * ((1/273.16) - (1/(273.16 + dew_pt))))
        g = (5/9) * (f-10)
        humidex = round(temp + g)
        
        # Sends a print statement to the user depending on the value of the dew point
        if 20 <= humidex <= 29:
            print(f'The humidex is {humidex}. Little or no discomfort.')
        elif 30 <= humidex <= 39:
            print(f'The humidex is {humidex}. Some discomfort.')
        elif 40 <= humidex <= 44:
            print(f'The humidex is {humidex}. Great discomfort. Avoid exertion.')
        else:
            print(f'The humidex is {humidex}. Dangerous. Heat stroke possible.')

    else:
        # Entered dew point is out of range (-50 <= dew_pt <= 50)
        # Invoke recursion to run function from start
        print('That dew point is invalid.')
        calc_warm_temp(temp)


# --- calculator --- #
# Main program used to dictate which calculation to run and whether to re-run program after use
def calculator():
    # Variables pertaining to handling prompt to re-run program
    cont = None
    valid_cont_values = ["y", "Y", "n", "N"]

    # If users doesn't declare "n" or "N" when asked if they want to check another weather condition, following will run
    while cont != "n" and cont != "N":
        
        try:
            # Prompt user for temperature
            temp = float(input('Enter a temperature between -50 and 50: '))
        except ValueError:
            # Input can't be converted to float
            # Invoke recursion to run program from start
            print('That temperature is invalid.')
            calculator()

        # Does action depending on the value of the temperature
        if -50 <= temp <= 50:
            if -50 <= temp <= 0:
                print('Calculating windchill.')
                calc_cold_temp(temp)
            elif 0 < temp < 20:
                print('Windchill and humidex are not a factor at this temperature.')
            elif 20<= temp <= 50:
                print('Calculating humidex.')
                calc_warm_temp(temp)

            # Reset continue var and re-prompt user until a value contained in valid_cont_values is entered
            cont = None
            while cont not in valid_cont_values:
                cont = input('Check another weather condition (Y/N)? ')
                if cont not in valid_cont_values:
                    print('That input is invalid.')

        else:
            # Entered temperature is out of range (-50 <= temp <= 50)
            print('That temperature is invalid.')


# Calls calculator function to start the program
calculator()