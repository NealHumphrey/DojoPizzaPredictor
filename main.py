import math

print("----------------")
print("Welcome to the Dojo Pizza Predictor!!")

# Assumptions about consumption
noshow_rate = 0.4
extra_attendee_rate = 0.1
slices_per_attendee = 2
beers_per_attendee = 2

#Calculate how many are coming
meetup_yes_rsvp = 25
attendee_count = math.ceil(meetup_yes_rsvp* (1 - noshow_rate + extra_attendee_rate))

# Delivery mechanics
slices_per_pizza = 8
beers_per_case = 24
beers_per_six_pack = 6

# Do the math
pizza_slices_needed = attendee_count * slices_per_attendee

pizzas = math.ceil(pizza_slices_needed / slices_per_pizza)
pizza_slices_actual = slices_per_pizza * pizzas
leftover_pizza = pizza_slices_actual - pizza_slices_needed

# We want to buy cases first, and make up the difference in six packs. 
# Round down on cases since we can get the rest in six packs
# We don't want to run out of beer, so we'll round up at the end. 
beers_needed = attendee_count * beers_per_attendee

beer_cases = math.floor(beers_needed / beers_per_case)
beer_remainder = beers_needed % beers_per_case
beer_six_packs = math.ceil(beer_remainder / beers_per_six_pack)
leftover_beer = beer_remainder % (beers_per_six_pack * beer_six_packs)

print("----------------")
print("Attendee best guess: {} (out of {} rsvps)".format(attendee_count, meetup_yes_rsvp))
print("----------------")
print("Number of pizzas: {}".format(pizzas))
print("Slices eaten: {}".format(pizza_slices_needed))
print("Leftover pizza slices: {}".format(leftover_pizza))

print("----------------")
print("Number of Beers: {} cases and {} six packs".format(beer_cases, beer_six_packs))
print("Leftover beer: {}".format(leftover_beer))
print("Actual leftover beer: 0")

