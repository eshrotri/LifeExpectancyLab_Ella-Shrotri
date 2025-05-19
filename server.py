# flask --app data_server run
from flask import Flask
from flask import render_template
from flask import request
from data.reformatData import dictionary 
import json


app = Flask(__name__, static_url_path='', static_folder='static')

with open("data/life_expectancy.json") as f:
    life_data = json.load(f)

@app.route('/')
def index():
    f = open("data/life_expectancy.json", "r")
    data = json.load(f)
    f.close()
    usa_endpoints = []
    canada_endpoints = []
    mexico_endpoints = []
    avg_endpoints = []

    years = sorted([int(y) for y in data["USA"].keys()])

    for i in range(len(years) - 1):
        year1 = str(years[i])
        year2 = str(years[i + 1])

        usa_y1 = float(data["USA"][year1])
        usa_y2 = float(data["USA"][year2])
        usa_endpoints.append([usa_y1, usa_y2])

        canada_y1 = float(data["Canada"][year1])
        canada_y2 = float(data["Canada"][year2])
        canada_endpoints.append([canada_y1, canada_y2])

        mexico_y1 = float(data["Mexico"][year1])
        mexico_y2 = float(data["Mexico"][year2])
        mexico_endpoints.append([mexico_y1, mexico_y2])

        avg_y1 = (mexico_y1 + usa_y1 + canada_y1)/3
        avg_y2 = (mexico_y2 + usa_y2 + canada_y2)/3
        avg_endpoints.append([avg_y1, avg_y2])
    return render_template(
    "index.html",
    usa_endpoints=usa_endpoints,
    canada_endpoints=canada_endpoints,
    mexico_endpoints=mexico_endpoints,
    avg_endpoints = avg_endpoints,
    years=years
    )
    print (data)
@app.route('/year')
def year(): 
    f = open("data/life_expectancy.json", "r")
    data = json.load(f)
    f.close()
    year = request.args.get("year")

    usa_value = float(data["USA"][str(year)])
    canada_value = float(data["Canada"][str(year)])
    mexico_value = float(data["Mexico"][str(year)]) 

    return render_template(
        "year.html",
        year=year,
        usa_value=usa_value,
        canada_value=canada_value,
        mexico_value=mexico_value
    )


app.run(debug=True)