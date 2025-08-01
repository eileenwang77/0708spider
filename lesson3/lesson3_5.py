import json
from pprint import pprint
import argparse

class Site:
    def __init__(self,
                 sitename,
                 county,
                 aqi,
                 pollutant,
                 status,
                 pm2_5,
                 pm2_5_avg,
                 latitude,
                 longitude,
                 datacreationdate):      # ← 修正參數名稱
        self.sitename = sitename
        self.county = county
        self.aqi = aqi
        self.pollutant = pollutant
        self.status = status
        self.pm2_5 = pm2_5
        self.pm2_5_avg = pm2_5_avg
        self.latitude = latitude
        self.longitude = longitude
        self.datacreationdate = datacreationdate

def parse_sites_from_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    site_list = []
    for sitename in data['records']:
        site = Site(
            sitename=sitename['sitename'],
            county=sitename['county'],
            aqi=sitename['aqi'],
            pollutant=sitename['pollutant'],
            status=sitename['status'],
            pm2_5=sitename['pm2.5'],
            pm2_5_avg=sitename['pm2.5_avg'],
            latitude=sitename['latitude'],
            longitude=sitename['longitude'],
            datacreationdate=sitename['datacreationdate']
        )
        site_list.append(site)
    return site_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AQI 資料查詢 CLI')
    parser.add_argument('-c', '--county', '--country', dest='county', help='過濾縣市名稱', default=None)
    parser.add_argument('--file', '-f', help='JSON 檔案路徑', default='aqx_p_488.json')
    args = parser.parse_args()

    parsed_sites = parse_sites_from_json(args.file)
    if args.county:
        parsed_sites = [s for s in parsed_sites if s.county == args.county]
    for site in parsed_sites:
        print(f"站點名稱: {site.sitename}, 所在縣市: {site.county}, AQI: {site.aqi}, 主要污染物: {site.pollutant}")