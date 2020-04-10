planet_list = ["Mercury", "Mars"]

# planet_list.append("Jupiter")
# planet_list.append("Saturn")

planet_list.extend(["Jupiter", "Saturn"])

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

planet_list.append("Pluto")

rocky_planets = planet_list[0:4]

del planet_list[-1]

# print(planet_list)
# print(rocky_planets)

# ----Challenge---- 

# Example spacecraft list
spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
]

for planet in planet_list:
    for satellite in spacecraft:
        if satellite[1] == planet:
            print(f'{satellite[0]} has visited {satellite[1]}')


