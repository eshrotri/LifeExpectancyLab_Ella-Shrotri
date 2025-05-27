import json


f1 = open("data/Abuse_Borough - Sheet1.csv", "r")
lines = f1.readlines()
years = lines[2].strip().split(",")[1:]

dictionary ={}

bronx_list = lines[3].split(",")[1:]
brook_list = lines[4].split(",")[1:]
manh_list = lines[5].split(",")[1:]
queens_list = lines[6].split(",")[1:]
s_i_list = lines[7].split(",")[1:]
outside_list = lines[8].split(",")[1:]
total_list = lines[9].split(",")[1:]

bronx_dict = {}
brook_dict = {}
manh_dict = {}
queens_dict = {}
s_i_dict = {}
outside_dict = {}
total_dict = {}

for i in range(len(years)):
    year = years[i]
    current = bronx_list[i].strip().replace('"', '')
    if current:
        bronx_dict[year] = float(current)
    else:
        bronx_dict[year] = None

for i in range(len(years)):
    year = years[i]
    current = brook_list[i].strip().replace('"', '')
    if current:
        brook_dict[year] = float(current)
    else:
        brook_dict[year] = None

for i in range(len(years)):
    year = years[i]
    current = manh_list[i].strip().replace('"', '')
    if current:
        manh_dict[year] = float(current)
    else:
        manh_dict[year] = None

for i in range(len(years)):
    year = years[i]
    current = queens_list[i].strip().replace('"', '')
    if current:
        queens_dict[year] = float(current)
    else:
        queens_dict[year] = None

for i in range(len(years)):
    year = years[i]
    current = s_i_list[i].strip().replace('"', '')
    if current:
        s_i_dict[year] = float(current)
    else:
        s_i_dict[year] = None
for i in range(len(years)):
    year = years[i]
    current = outside_list[i].strip().replace('"', '')
    if current:
        outside_dict[year] = float(current)
    else:
        outside_dict[year] = None

for i in range(len(years)):
    year = years[i]
    current = total_list[i].strip().replace('"', '')
    if current:
        total_dict[year] = float(current)
    else:
        total_dict[year] = None
dictionary = {
    "The Bronx": bronx_dict,
    "Brooklyn": brook_dict,
    "Manhattan": manh_dict,
    "Queens": queens_dict,
    "Staten Island": s_i_dict,
    "Outside": outside_dict,
    "Total": total_dict
}

f1.close()

f2 = open("abuse_per_borough.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()