def hotel_cost(nights):
    nights = raw_input("How many nights are you staying?: ")
    return 140 * nights


def plane_ride_cost(city):
    city = raw_input("What destination? ")
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return "That is not a valid city"
