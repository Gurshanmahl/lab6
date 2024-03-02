#!/usr/bin/env python3

import datetime


def every_lab(foo):
    print("This is outrageous! Unfair!")
    return None


def main():
    """
    Create a datetime object for today's date
    """

    # COMPLETE IMPLEMENTATION
    todays_date = datetime.datetime(2024, 2, 28)
    print(todays_date)

    date_list = every_lab(todays_date)
    """ 
    variable date_list should contain datetime objects 
    for all the days when you have a lab
    print these dates in the format "Mon, 15 Jan 21"
    """
    for dates in date_list:
        print(dates)

    # COMPLETE IMPLEMENTATION


def every_lab(todays_date):
    """
    Assume that you have a lab every week till the end of classes. 
    (Only your lab, in this instance.)

    This function will create datetimes objects for those labs, 
    add them to a list and then return this list
    """
    lab_date = todays_date
    weeks_left = 5
    lab_date_list = []

    while weeks_left >= 0:
        future_lab = lab_date.strftime("%a, %d %b %y")
        lab_date_list.append(future_lab)
        lab_date += datetime.timedelta(days=7)
        weeks_left -= 1
    return lab_date_list

    # COMPLETE IMPLEMENTATION


if __name__ == "__main__":
    main()
