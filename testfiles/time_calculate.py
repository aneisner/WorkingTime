#!=/usr/bin/python3.6

# https://favtutor.com/blogs/timedelta-python

#Beispiel 1

from datetime import datetime, timedelta

# get the current date and time

now = datetime.now()

# create a timedelta object for 1 day

one_day = timedelta(days=1)

# add the timedelta object to the current date and time

next_day = now + one_day

# print the current date and time and the next day

print("Current Date and Time:", now)

print("Next Day:", next_day)


# Beispiel 2

from datetime import datetime, timedelta

# create a datetime object for May 1st, 2023 at 12:00:00

dt = datetime(2023, 5, 1, 12, 0, 0)

# create a timedelta object for 5 days

five_days = timedelta(days=5)

# subtract the timedelta object from the datetime object

result = dt - five_days

# print the result

print("---------------------")
print(result)
print("---------------------")