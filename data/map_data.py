import requests
import json
import os
from collections import OrderedDict
from pathlib import Path

DATA_URL = "https://code.highcharts.com/mapdata/countries/ug/ug-all.geo.json"


class MapData:
    pass

    def get_uganda_data(self):
        res = requests.get(DATA_URL).content
        uganda_data = json.loads(res)
        return uganda_data.get("features")

    def get_districts_farmer_data(self):
        farmer_data = self.get_district_farmer_data()
        uganda_data = self.get_uganda_data()
        districts_farmers_data = []
        for data in uganda_data:
            properties = data.get("properties")
            hc_key = properties.get("hc-key")
            district_name = properties.get("name")
            number_of_farmers = self.get_district_farmer_numbers(
                farmer_data, district_name
            )
            districts_farmers_data.append([hc_key, number_of_farmers])
        return districts_farmers_data

    def get_district_farmer_numbers(self, farmer_data, district_name):
        return [
            item.get("number")
            for item in farmer_data
            if item.get("district") == district_name
        ][0]

    def get_district_farmer_data(self):
        farmer_data_file = (
            f"{Path(os.path.dirname(__file__)).parent}/static/interview.json"
        )
        with open(farmer_data_file, "r") as json_file:
            return json.load(json_file, object_pairs_hook=OrderedDict)
