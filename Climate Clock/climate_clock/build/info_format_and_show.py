#PYTHON SCRIPT

from datetime import datetime,timezone
from dateutil.relativedelta import relativedelta


def show_info(list_info):
    """
    This method is used to show the input text as messages on the oled disply.

    Returns:
        int: 0 Always for Success.
    """
    CARBON_DEADLINE_1 = {
        "timestamp":datetime.fromisoformat(list_info["carbon_deadline_1"]["timestamp"]),
        "label":list_info["carbon_deadline_1"]["labels"][1]
    }
    RENEWABLES_1 = {
    "initial": list_info["renewables_1"]["initial"],
    "timestamp": datetime.fromisoformat(list_info["renewables_1"]["timestamp"]),
    "rate": list_info["renewables_1"]["rate"],
    "label":list_info["renewables_1"]["labels"][0]
    }

    GREEN_CLIMATE_FUND_1 = {
            "initial":list_info["green_climate_fund_1"]["initial"],
            "timestamp": datetime.fromisoformat(list_info["green_climate_fund_1"]["timestamp"]),
            "unit_labels":list_info["green_climate_fund_1"]["unit_labels"][0],
            "label":list_info["green_climate_fund_1"]["labels"][0]
    }

    INDIGENOUS_LAND_1 = {
        "initial":list_info["indigenous_land_1"]["initial"],
        "timestamp": datetime.fromisoformat(list_info["indigenous_land_1"]["timestamp"]),
        "unit_labels":list_info["indigenous_land_1"]["unit_labels"][0],
        "label":list_info["indigenous_land_1"]["labels"][0]
    }

    NEWS_FEED_1 = {
        "feed_1":list_info["newsfeed_1"]["newsfeed"][0]["headline"],
        "feed_2":list_info["newsfeed_1"]["newsfeed"][1]["headline"],
        "feed_3":list_info["newsfeed_1"]["newsfeed"][2]["headline"],
        "feed_4":list_info["newsfeed_1"]["newsfeed"][3]["headline"],
        "feed_5":list_info["newsfeed_1"]["newsfeed"][4]["headline"],
        "feed_6":list_info["newsfeed_1"]["newsfeed"][5]["headline"],
        "feed_7":list_info["newsfeed_1"]["newsfeed"][6]["headline"],
        "feed_8":list_info["newsfeed_1"]["newsfeed"][7]["headline"],
        "feed_9":list_info["newsfeed_1"]["newsfeed"][8]["headline"],
        "feed_10":list_info["newsfeed_1"]["newsfeed"][9]["headline"],

    }
    now = datetime.now(timezone.utc)
    deadline_delta = relativedelta(CARBON_DEADLINE_1["timestamp"], now)
    years = deadline_delta.years
    rdays = relativedelta(months=deadline_delta.months, days=deadline_delta.days)
    days = ((rdays + now) - now).days
    hours = deadline_delta.hours
    minutes = deadline_delta.minutes
    seconds = deadline_delta.seconds
    cs = deadline_delta.microseconds // 10000

    t = (datetime.now(timezone.utc) - RENEWABLES_1["timestamp"]).total_seconds()
    percent = RENEWABLES_1["rate"] * t + RENEWABLES_1["initial"]

    fund_units = list(GREEN_CLIMATE_FUND_1["unit_labels"])
    land_units = INDIGENOUS_LAND_1["unit_labels"].split()
    if land_units[0] == 'M':
        places = 10**6
    elif land_units[0] == 'B':
        places = 10**9
    if fund_units[1] == "M":
        suffix = "MILLION"
    elif fund_units[1] == "B":
        suffix = "BILLION"
    elif fund_units[1] == "T":
        suffix = "TRILLION"
    elif fund_units[1] == "QA":
        suffix = "QUADRILLION"
    elif fund_units[1] == "QI":
        suffix = "QUINTRILLION"
    elif fund_units[1] == "SX":
        suffix = "SEXTILLION"
    elif fund_units[1] == "SP":
        suffix = "SEPTILLION"

    message_dictionary = {CARBON_DEADLINE_1["label"]:"{} {} {} {} {}".format(years,"YEAR" if years == 1 else "YEARS",str(days).zfill(2),"DAY" if days == 1 else "DAYS",str(hours).zfill(2)+":"+str(minutes).zfill(2)+":"+str(seconds).zfill(2)+"."+str(cs)),
                    RENEWABLES_1["label"]:str(format(percent,".2f"))+'%',
                    GREEN_CLIMATE_FUND_1["label"]:"{}{} {}".format(fund_units[0],GREEN_CLIMATE_FUND_1["initial"],suffix),
                    INDIGENOUS_LAND_1["label"]:"{} {}".format(f'{INDIGENOUS_LAND_1["initial"]*places:,}',land_units[1]),
                    "News Feed 1":NEWS_FEED_1["feed_1"],
                    "News Feed 2":NEWS_FEED_1["feed_2"],
                    "News Feed 3":NEWS_FEED_1["feed_3"],
                    "News Feed 4":NEWS_FEED_1["feed_4"],
                    "News Feed 5":NEWS_FEED_1["feed_5"],
                    "News Feed 6":NEWS_FEED_1["feed_6"],
                    "News Feed 7":NEWS_FEED_1["feed_7"],
                    "News Feed 8":NEWS_FEED_1["feed_8"],
                    "News Feed 9":NEWS_FEED_1["feed_9"],
                    "News Feed 10":NEWS_FEED_1["feed_10"],}
    print_msg_box(message_dictionary)

    return 0

def print_msg_box(message_dictionary,indent=10, width=None):
    """Print message-box with title."""
    now = datetime.now()
    time_left = message_dictionary[list(message_dictionary.keys())[0]]
    energy = message_dictionary[list(message_dictionary.keys())[1]]
    fund = message_dictionary[list(message_dictionary.keys())[2]]
    protected_land = message_dictionary[list(message_dictionary.keys())[3]]

    box = """
                          ╔═════════════════════════════════╗
    ╔═════════════════════║              {}         ║══════════════════════════╗
    ║                     ╚═════════════════════════════════╝                          ║
    ║                                                                                  ║
    ╚══════════════════════════════════════════════════════════════════════════════════╝
    ║   {}  ║      \033[91m{}\033[0m      ║
    ╚══════════════════════════════════════════════════════════════════════════════════╝
    ║      {}      ║                 \033[1;32m{}\033[0m                ║
    ╚══════════════════════════════════════════════════════════════════════════════════╝
    ║            {}            ║              \033[1;32m{}\033[0m            ║
    ╚══════════════════════════════════════════════════════════════════════════════════╝
    ║   {}    ║             \033[1;32m{}\033[0m          ║
    ╚══════════════════════════════════════════════════════════════════════════════════╝
    ║           {}.        ║
    ╚══════════════════════════════════════════════════════════════════════════════════╝
    ║                {}.             ║
    ╚══════════════════════════════════════════════════════════════════════════════════╝
    ║     {}    ║
    ║                              {}.                         ║
    ╚══════════════════════════════════════════════════════════════════════════════════╝
    ║     {}     ║
    ║                               {}.                       ║
    ╚══════════════════════════════════════════════════════════════════════════════════╝

    """.format(now.strftime("%a %d %b"),list(message_dictionary.keys())[0],time_left,list(message_dictionary.keys())[1],energy,list(message_dictionary.keys())[2],fund,list(message_dictionary.keys())[3],protected_land,message_dictionary[list(message_dictionary.keys())[4]],message_dictionary[list(message_dictionary.keys())[5]],message_dictionary[list(message_dictionary.keys())[6]].rsplit(" ",5)[0]," ".join(message_dictionary[list(message_dictionary.keys())[6]].rsplit(" ",5)[1:]),message_dictionary[list(message_dictionary.keys())[7]].rsplit(" ",4)[0]," ".join(message_dictionary[list(message_dictionary.keys())[7]].rsplit(" ",4)[1:]))
    print(box)
