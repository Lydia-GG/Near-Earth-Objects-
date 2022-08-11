from models import CloseApproach,NearEarthObject

neo = NearEarthObject("433","Eros",16.84,"N")
# print(neo.designation)
# print(neo.name)
print(neo)

ca = CloseApproach("2020 FK", "2020-Jan-01 12:30", 0.25, 56.78 )

# print(type(ca.time))
# print(ca.time_str)
print(ca)
