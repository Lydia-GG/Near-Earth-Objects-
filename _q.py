from models import CloseApproach,NearEarthObject

neo = NearEarthObject("433","Eros",16.84,"N")
# print(neo.designation)
# print(neo.name)
print(neo)

ca = CloseApproach("2020 FK", "2020-Jan-01 12:30", 0.25, 56.78 )

# print(type(ca.time))
# print(ca.time_str)
print(ca)

# filter.py
# 1- create_filters function will produce a collection of instances of subclasses of AttributeFilter 

# 2- concrete subclasses will be able to override this method (get) to actually get a specific attribute of interest

# The op argument will represent the operation corresponding to either <=, ==, or >= - Python's operator module makes these available to us as operator.le, operator.eq, and operator.ge. That is, operator.ge(a, b) is the same as a >= b. Lastly, the value will just be our target value, as supplied by the user at the command line and fed to create_filters by the main module.

# three things that seem to be shared between all of our filters are (1) a way to get the attribute we're interested in and (2) a way to compare that attribute against (3) some reference value. Where there's shared behavior, there's an opportunity for decomposition.
