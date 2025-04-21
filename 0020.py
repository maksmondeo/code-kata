"""
https://www.codewars.com/kata/52742f58faf5485cae000b9a

Detailed rules

The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
"""

def format_duration(seconds):
    years = seconds // (60 * 60 * 24 * 365)
    days = (seconds - years * 60 * 60 * 24 * 365) // (60 * 60 * 24)
    hours = (seconds - days * 60 * 60 * 24 - years * 60 * 60 * 24 * 365) // (60 * 60)
    minutes = (seconds - hours * 60 * 60 - days * 60 * 60 * 24 - years * 60 * 60 * 24 * 365) // 60
    seconds = (seconds - minutes * 60 - hours * 60 * 60 - days * 60 * 60 * 24 - years * 60 * 60 * 24 * 365)

    result = ""

    if years == 1:
        result += f"{years} year"
    elif years > 1:
        result += f"{years} years"

    if days == 1:
        if result:
            if hours or minutes or seconds:
                result += ", "
            else:
                result += " and "
            result += f"{days} day"
        else:
            result += f"{days} day"
    elif days > 1:
        if result:
            if hours or minutes or seconds:
                result += ", "
            else:
                result += " and "
            result += f"{days} days"
        else:
            result += f"{days} days"

    if hours == 1:
        if result:
            if minutes or seconds:
                result += ", "
            else:
                result += " and "
            result += f"{hours} hour"
        else:
            result += f"{hours} hour"
    elif hours > 1:
        if result:
            if minutes or seconds:
                result += ", "
            else:
                result += " and "
            result += f"{hours} hours"
        else:
            result += f"{hours} hours"

    if minutes == 1:
        if result:
            if seconds:
                result += ", "
            else:
                result += " and "
            result += f"{minutes} minute"
        else:
            result += f"{minutes} minute"
    elif minutes > 1:
        if result:
            if seconds:
                result += ", "
            else:
                result += " and "
            result += f"{minutes} minutes"
        else:
            result += f"{minutes} minutes"

    if seconds == 1:
        if result:
            result += f" and {seconds} second"
        else:
            result += f"{seconds} second"
    elif seconds > 1:
        if result:
            result += f" and {seconds} seconds"
        else:
            result += f"{seconds} seconds"

    if result == "":
        return "now"

    return result
