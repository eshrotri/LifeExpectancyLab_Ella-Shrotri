from flask import Flask, render_template, json, request

app = Flask(__name__)

def scale(value, min_val, max_val):
    normalized = (value - min_val) / (max_val - min_val)
    lightness = 80 - normalized * 60
    return round(lightness, 2)

@app.route("/")
def about():
    return render_template("about.html")

@app.route("/all_data")
def macro():
    with open('data/abuse_per_borough.json') as f:
        data = json.load(f)
    years = list(data["Total"].keys())
    boroughs = data
    return render_template("index.html", years=years, boroughs=boroughs)

    
@app.route("/year/<int:year>")
def micro(year):
    with open("data/abuse_per_borough.json") as f:
        data = json.load(f)

    year = str(year)

    borough_data = {
        "bronx": data["The Bronx"][year],
        "brooklyn": data["Brooklyn"][year],
        "manhattan": data["Manhattan"][year],
        "queens": data["Queens"][year],
        "staten": data["Staten Island"][year],
    }

    max_val = max(borough_data.values())
    avg_val = sum(borough_data.values()) / len(borough_data)
    lightness = {
        borough: 80 - (val / max_val) * 60
        for borough, val in borough_data.items()
    }

    return render_template(
        "year.html",
        year=year,
        bronx_value=borough_data["bronx"],
        brooklyn_value=borough_data["brooklyn"],
        manhattan_value=borough_data["manhattan"],
        queens_value=borough_data["queens"],
        staten_value=borough_data["staten"],
        bronx_light=lightness["bronx"],
        brooklyn_light=lightness["brooklyn"],
        manhattan_light=lightness["manhattan"],
        queens_light=lightness["queens"],
        staten_light=lightness["staten"],
        average_value=round(avg_val, 0),
        manhattan_comp = abs(round((avg_val - borough_data["manhattan"]),0)),
        brooklyn_comp = abs(round((avg_val - borough_data["brooklyn"]),0)),
        queens_comp = abs(round((avg_val - borough_data["queens"]),0)),
        staten_comp = abs(round((avg_val - borough_data["staten"]),0)),
        bronx_comp = abs(round((avg_val - borough_data["bronx"]),0))
    )

if __name__ == "__main__":
    app.run(debug=True)
