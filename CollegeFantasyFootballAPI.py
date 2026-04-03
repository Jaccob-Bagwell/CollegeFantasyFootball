
import time
import cfbd
import json
from cfbd.rest import ApiException
from pprint import pprint


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



# Defining the host is optional and defaults to https://api.collegefootballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cfbd.Configuration(
    host = "https://api.collegefootballdata.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = cfbd.Configuration(
    access_token = "ANwrLmh7bIKfnl70S1zZNm+NqYkdTc7jTH/7uEfjuBjGQHe/7nGDFEx/VE8gsFdC"

)


with cfbd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cfbd.GamesApi(api_client)
    #parameters
    year = 2019 # int | Optional year filter (optional)
    team = 'michigan' # str | Optional team filter (optional)
    week = 5
    


    try:
        api_response = api_instance.get_games(year=year,week=week,team=team)
        # Convert to readable JSON
        readable = [coach.to_dict() for coach in api_response]
        with open('output_file.txt', 'w') as text_file:
            json.dump(readable, text_file, indent=4, default=str) #
        #print(json.dumps(readable, indent=4, default=str))
        
    except Exception as e:
        print("Exception when calling CoachesApi->get_coaches: %s\n" % e)


CallsLeft()


