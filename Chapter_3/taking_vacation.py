def hotel_cost():
  nights = raw_input("How many nights are you staying?: ")
  print (140 * int(nights))
  return hotel_cost()


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
        return "That city is not a valid city"
    return plane_ride_cost()