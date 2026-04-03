
import time
import cfbd
import json
from cfbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collegefootballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cfbd.Configuration(
    host = "https://api.collegefootballdata.com"
)

# Configure Bearer authorization: apiKey
configuration = cfbd.Configuration(
    access_token = "ANwrLmh7bIKfnl70S1zZNm+NqYkdTc7jTH/7uEfjuBjGQHe/7nGDFEx/VE8gsFdC"

)

#will tell what tier and how many call i have left
def CallsLeft():
    with cfbd.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = cfbd.InfoApi(api_client)

        try:
            api_response = api_instance.get_user_info()
            print("The response of InfoApi->get_user_info:\n")
            pprint(api_response)
        except Exception as e:
            print("Exception when calling InfoApi->get_user_info: %s\n" % e)


def callPlayerSeasonStats(year,team,start_week,end_week):
    with cfbd.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = cfbd.StatsApi(api_client)
        #parameters
        try:
            api_response = api_instance.get_player_season_stats(year=year, team =team, start_week=start_week, end_week=end_week) #
            # Convert to readable JSON
            readable = [coach.to_dict() for coach in api_response]
            with open('output_file.txt', 'w') as text_file:
                json.dump(readable, text_file, indent=4, default=str) #
            #print(json.dumps(readable, indent=4, default=str))
        except Exception as e:
            print("Exception: %s\n" % e)




