from flask import Flask , request, render_template, jsonify, Response
import random
import xml.etree.ElementTree as ET

app = Flask(__name__)



indian_cities = [
    "mumbai", "delhi", "bengaluru", "hyderabad", "chennai",
    "kolkata", "pune", "jaipur", "ahmedabad", "surat",
    "visakhapatnam", "kochi", "lucknow", "bhopal", "patna",
    "thiruvananthapuram", "nagpur", "indore", "guwahati", "vadodara"
]

temperatures = [25, 30, 28, 32, 22, 27, 33, 29, 31, 26, 24, 35, 21, 34, 23, 20, 19, 36, 18, 17]
pressures = [1015, 1013, 1011, 1018, 1016, 1014, 1012, 1010, 1009, 1017, 1020, 1022, 1008, 1021, 1007, 1019, 1006, 1005, 1004, 1023]
wind_speeds = [5, 10, 7, 12, 9, 15, 8, 6, 20, 18, 13, 25, 4, 11, 22, 14, 3, 17, 16, 23]
humidities = [60, 65, 70, 55, 75, 80, 85, 90, 95, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 88]
clouds = [20, 30, 40, 50, 60, 70, 80, 90, 10, 25, 35, 45, 55, 65, 75, 85, 95, 100, 0, 15]
visibility = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 13, 14, 15, 16, 17, 18, 19, 20]
aqi = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 40, 30, 20, 10, 160, 170, 180, 190, 200]
chance_of_rain = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 0, 5, 15, 25, 35, 45, 55, 65, 75, 85]


def generate_fake():
    return{
            'city': random.choice(indian_cities),
            'temperature': random.choice(temperatures),
            'pressure': random.choice(pressures),
            'wind_speeds': random.choice(wind_speeds),
            'aqi': random.choice(aqi),
            'clouds': random.choice(clouds),
            'probability of rain': random.choice(chance_of_rain)

    }

weather_data = [generate_fake() for _ in range(30)]

#print(weather_data[0]['city'])


def get_weather(city):
    for data in weather_data:
        if data.get("city") == city:
            return data


@app.route("/<string:city>",methods=['GET'])
@app.route("/<string:city>?<string:format>/", methods = ['GET'])
def weather(city , format="xml"):
    fcity = city
    fformat = format
    if request.method == 'GET':
        fcity = request.args.get('city', city)
        fformat = request.args.get('format', format)
    else:
        if 'Content-Type' in requests.headers:
            if request.headers['Content-Type'] in ['application/json']:
                fcity = request.json.get('city', city)
                fformat = request.json.get('format', format)
            else:  # XML 
                if 'Content-Type' in request.headers:
                    if request.headers['Content-Type'] in ['application/xml']:
                        root = ET.fromstring(request.data)
                        el = root.findall("./name")
                        if el:
                            fcity = el[0].text
                        else:
                            fcity = city
                        fformat = "xml"
                    else:
                        return "Content type not recognised"
    weather_out = get_weather(city.lower())
    if fformat == 'json':
       if city is not None:
           return jsonify(weather_out)
       else:
           resp = 'Error'
           resp.status_code = 500 
       return resp  
    elif fformat == 'xml':
       response = f"""<?xml version="1.0" encoding="UTF-8"?>
        <data>
            <city>{weather_out['city']}</city>
            <temperature>{weather_out['temperature']}</temperature>
            <pressure>{weather_out['pressure']}</pressure>
            <wind_speed>{weather_out['wind_speeds']}</wind_speed>
            <aqi>{weather_out['aqi']}</aqi>
            <clouds>{weather_out['clouds']}</clouds>
            <probability_of_rain>{weather_out['probability of rain']}</probability_of_rain>
        </data>"""
       resp = Response(response=response, status=200, mimetype="application/xml")
       return resp
    else:
       return "Format not recognized"
    


if __name__=='__main__':
    app.run()