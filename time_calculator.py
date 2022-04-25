def add_time(start, duration, start_day=""):
    no_of_days = int(int(duration.split(":")[0]) / 24)
    rem_hours = int(duration.split(":")[0]) - no_of_days * 24
    rem_minutes = int(duration.split(":")[1])
    starting_hours = int(start.split(":")[0])
    starting_minutes = int(start.split(":")[1].split(" ")[0])
    if start.split(":")[1].split(" ")[1].casefold() == "PM".casefold() and starting_hours != 12:
        starting_hours += 12
    while rem_hours != 0 or rem_minutes != 0:
        if rem_hours != 0 and 24 - starting_hours > rem_hours:
            starting_hours += rem_hours
            rem_hours = 0
        elif starting_hours == 23:
            starting_minutes += rem_minutes
            if 0 != starting_minutes % 60:
                no_of_days += 1
            rem_minutes = 0
            starting_hours = 0
            starting_minutes = starting_minutes % 60
        else:
            starting_hours += rem_hours
            starting_minutes += rem_minutes
            if starting_minutes > 60:
                starting_minutes %= 60
                starting_hours += 1
            if starting_hours > 24:
                starting_hours %= 24
                no_of_days += 1
            rem_minutes = 0
            rem_hours = 0
    if starting_hours > 11:
        starting_hours -= 12
        z = " PM"
    else:
        z = " AM"
    if starting_hours == 0:
        starting_hours = 12
    next_time = str(starting_hours) + ":" + str(starting_minutes).rjust(2, '0') + z
    end_date = start_day
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if len(start_day) > 1:
        start_day = start_day[0].capitalize() + start_day[1:].lower()
        for day in days:
            if start_day == day:
                index = days.index(start_day)
                index += no_of_days
                index = index % 7
                end_date = days[index]
    if len(end_date) > 1:
        next_time += ", " + end_date
    if no_of_days == 0:
        pass
    elif no_of_days == 1:
        next_time += " (next day)"
    else:
        next_time += " ({} days later)".format(no_of_days)

    return next_time


#print(add_time("8:16 PM", "466:02"))
