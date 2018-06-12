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


def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif cost >= 3:
        cost -= 20
        return cost


def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money
    print trip_cost("Los Angeles", 5, 600)

