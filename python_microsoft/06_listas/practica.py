planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune"]
user_planet = input("Please enter the name of the planet (with a capital letter to start): ")
planet_index = planets.index(user_planet) 

# los planetas mas cerca de # user_planet
print("Here are the planets closer than " + user_planet)
print(planets[0:planet_index])

# los planetas mas lejos de # user_planet
print("Here are the planets further than " + user_planet)
print(planets[planet_index + 1:]) # print(planets[planet_index + 1:len(planets)]) 