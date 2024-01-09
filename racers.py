"""
Your goal is to write a function to identify which drivers in a dataset have NOT won any race.

The dataset will be a dictionary. The keys will be the names of races and the values will be, the top three drivers to finish at that race. 
The first driver in the tuple will be the one who won the race. An example dataset is shown below:

races_1 = {
    "Suzuka": ("Tsunoda", "Latifi", "Stroll"),
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
    "Silverstone": ("Hamilton", "Latifi", "Tsunoda")
}

In this example, Tsunoda won at Suzuka, Pérez won at Mexico City, and Hamilton won at Silverstone. Latifi and Stroll are present in the dictionary, but they did 
not win any of the races.

Write a function that accepts a races dicitonary and returns a *set* of all drivers that are present in that dictionary but did NOT win any race. For example, 
for the above dictionary, your function should return:

{"Latifi", "Stroll"}

See assertions below for more test cases.

looping through the tuple and save in a new list all the items but the first one
"""
def non_winners(races):
    # Your solution here!
    no_winner_list = []
    winner_list = []
    for drivers_tuple in races.values():
        for i in range(len(drivers_tuple)):
            if i > 0:
                no_winner_list.append(drivers_tuple[i])
            else:
                winner_list.append(drivers_tuple[i])

    no_winners_set = set()

    for driver in no_winner_list:
        if driver not in winner_list:
            no_winners_set.add(driver)
    print(no_winners_set)
    
    return no_winners_set


races_1 = {
    "Suzuka": ("Tsunoda", "Latifi", "Stroll"),
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
    "Silverstone": ("Hamilton", "Latifi", "Tsunoda")
}
assert non_winners(races_1) == {"Latifi", "Stroll"}

races_2 = {
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
}
assert non_winners(races_2) == {"Hamilton", "Tsunoda"}

races_3 = {
    "Monaco": ("Leclerc", "Verstappen", "Sainz"),
    "Barcelona": ("Sainz", "Verstappen", "Leclerc"),
    "Zandvoort": ("Verstappen", "Sainz", "Leclerc")
}
# If all drivers present in the dictionary won a race
# then the return value should be an empty set
assert non_winners(races_3) == set()