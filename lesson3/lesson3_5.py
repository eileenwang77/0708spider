import json
from pprint import pprint

class Site:
    def __init__(self,sitename, county, aqi, pollutant, status, pm25,  latitude, longitude, datacreationdate):
        self.sitename = sitename
        self.county = county        
        self.aqi = aqi
        self.pollutant = pollutant
        self.status = status
        self.pm25 = pm25
            
        self.latitude = latitude
        self.longitude = longitude
        self.datacreationdate = datacreationdate

def load_sites_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    sites = []
    for record in data['records']:
        site = Site(
            sitename=record['sitename'],
            county=record['county'],
            aqi=record['aqi'],
            pollutant=record['pollutant'],
            status=record['status'],
            pm25=record['pm2.5'],
            latitude=record['latitude'],
            longitude=record['longitude'],
            datacreationdate=record['datacreationdate']
        )
        sites.append(site)
    return sites


parsed_sites = load_sites_from_json('aqx_p_488.json')
for site in parsed_sites:
    print(f"站點名稱: {site.sitename}, 所在縣市: {site.county}, AQI: {site.aqi}, 主要污染物: {site.pollutant}")