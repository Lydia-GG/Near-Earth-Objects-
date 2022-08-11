import csv
import json

with open(r'D:\programming\Shell Udacity\python\python project\workspace\data\neos.csv', 'r') as infile:
    reader = csv.reader(infile)
    next(reader)
    # count of line 
    # rowcount = 0
    # for row in reader:  
    #   rowcount += 1
    # print(rowcount)

    #Look at the first row of the CSV, under the header "pdes"
    # rows = list(reader)
    # print(rows[0][3])

    # diameter if name "Apollo"
    # for row in reader:
    #   name = row[4]
    #   diameter = row[15]
    #   if name == "Apollo":
    #     print(diameter)

    # #Count the number of rows that have nonempty entries in the "name" column.
    # rowcount = 0
    # for row in reader:
    #   name = row[4]
    #   if name != "":
    #     rowcount +=1

    # print(rowcount)

    #Count the number of rows that have nonempty entries in the "diameter" column.
    # rowcount = 0
    # for row in reader:
    #   diameter = row[15]
    #   if diameter != "":
    #     rowcount += 1
    # print(rowcount)

    with open(r"D:\programming\Shell Udacity\python\python project\workspace\data\cad.json", "r") as file:
      contents = json.load(file)
    #How many close approaches are in the cad.json data set?
    #Hint: Instead of manually counting the entries, you can use the value of the "count" key
    # print(contents["count"])


# On January 1st, 2000, how close did the NEO whose primary designation is "2015 CL" pass by Earth?

# Hint: Find entries whose date starts with '2000-Jan-01'. One of the lists represents the close approach of the NEO "2015 CL". What is the value corresponding to the distance from Earth?
# data[0] = des = "2015"
# data[3] = cd = normal date = '2000-Jan-01'
# data[4] = dist = distance from Earth = 



# for data in contents["data"]:
#   if data[3].startswith("2000-Jan-01") and data[0] == "2015 CL":
#     print(data[4])

# On January 1st, 2000, how fast did the NEO whose primary designation is "2002 PB" pass by Earth?

# Hint: Find entries whose date starts with '2000-Jan-01'. One of the lists represents the close approach of the NEO "2002 PB". What is the value corresponding to the velocity relative to Earth?

for data in contents["data"]:
  if data[3].startswith("2000-Jan-01") and data[0] == "2002 PB":
    print(data[7])

      
  







# cad.json format description:
# des - primary designation of the asteroid or comet (e.g., 443, 2000 SG344)

# orbit_id - orbit ID

# jd - time of close-approach (JD Ephemeris Time)

# cd - time of close-approach (formatted calendar date/time, in UTC)

# dist - nominal approach distance (au)

# dist_min - minimum (3-sigma) approach distance (au)

# dist_max - maximum (3-sigma) approach distance (au)

# v_rel - velocity relative to the approach body at close approach (km/s)

# v_inf - velocity relative to a massless body (km/s)

# t_sigma_f - 3-sigma uncertainty in the time of close-approach (formatted in days, hours, and minutes; days are not included if zero; example "13:02" is 13 hours 2 
# minutes; example "2_09:08" is 2 days 9 hours 8 minutes)

# h - absolute magnitude H (mag)