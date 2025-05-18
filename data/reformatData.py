import json


f1 = open("data/life_expectancy_clean.csv", "r")
lines = f1.readlines()
year_keys = lines[0].strip().split(",")[4:] #just to get rid of the other stuff before the years
#iteratre through list of lines (lines) 
#split each line into its own list 
# go through that list and create a dictionary with year being the key and left expectancy the value 
dictionary ={}

canada_list = lines[1].split(",")[5:]
mexico_list = lines[2].split(",")[5:]
us_list = lines[3].split(",")[5:]

canada_dict = {}
mexico_dict = {}
us_dict = {}

for i in range(len(year_keys)):
    year = year_keys[i]
    value = canada_list[i]
    if value:
        canada_dict[year] = float(value)
    else:
        canada_dict[year] = None

for i in range(len(year_keys)):
    year = year_keys[i]
    value = mexico_list[i]
    if value:
        mexico_dict[year] = float(value)
    else:
        mexico_dict[year] = None

for i in range(len(year_keys)):
    year = year_keys[i]
    value = us_list[i]
    if value:
        us_dict[year] = float(value)
    else:
        us_dict[year] = None

dictionary = {
    "Canada": canada_dict,
    "Mexico": mexico_dict,
    "USA": us_dict
}

f1.close()

#Save the json object to a file
f2 = open("life_expectancy.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()