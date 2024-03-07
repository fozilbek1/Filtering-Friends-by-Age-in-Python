# filter() = creates a collection of elements from an interable for which a function returns true

frineds = [("Rachel", 19),
           ("Monica", 18),
           ("Sandy", 17),
           ("Justin", 16),
           ("Ross", 20),
           ("Fozil", 21)]

age = lambda  data:data[1] >= 18

drinking_buddies = list(filter(age, frineds))

for i in drinking_buddies:
    print(i)