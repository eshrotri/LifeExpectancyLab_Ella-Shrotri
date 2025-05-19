import json


f1 = open("data/life_expectancy_clean.csv", "r")
lines = f1.readlines()
years = lines[0].strip().split(",")[4:]

dictionary ={}

canada_list = lines[1].split(",")[5:]
mexico_list = lines[2].split(",")[5:]
us_list = lines[3].split(",")[5:]

canada_dict = {}
mexico_dict = {}
us_dict = {}

for i in range(len(years)):
    year = years[i]
    current = canada_list[i]
    if current:
        canada_dict[year] = float(current)
    else:
        canada_dict[year] = None

for i in range(len(years)):
    year = years[i]
    current = mexico_list[i]
    if current:
        mexico_dict[year] = float(current)
    else:
        mexico_dict[year] = None

for i in range(len(years)):
    year = years[i]
    current = us_list[i]
    if current:
        us_dict[year] = float(current)
    else:
        us_dict[year] = None

dictionary = {
    "Canada": canada_dict,
    "Mexico": mexico_dict,
    "USA": us_dict
}

f1.close()

f2 = open("life_expectancy.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()