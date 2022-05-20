#PYTHON SCRIPT

import json
import requests

def get_info():
    """
    This method is used to retrieve info from climate clock and return some critical information.

    Returns:
        dict: critical info dictionaries
    """

    url = "https://api.climateclock.world/v1/clock"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    carbon_deadline_1 = parsed["data"]["modules"]["carbon_deadline_1"]
    renewables_1 = parsed["data"]["modules"]["renewables_1"]
    green_climate_fund_1 = parsed["data"]["modules"]["green_climate_fund_1"]
    indigenous_land_1 = parsed["data"]["modules"]["indigenous_land_1"]
    newsfeed_1 = parsed["data"]["modules"]["newsfeed_1"]

    return {"carbon_deadline_1":carbon_deadline_1,"renewables_1":renewables_1,"green_climate_fund_1":green_climate_fund_1,"indigenous_land_1":indigenous_land_1,"newsfeed_1":newsfeed_1}