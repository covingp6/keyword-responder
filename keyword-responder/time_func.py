import requests
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime

def get_timezone(location_name):
    locator = Nominatim(user_agent="keyword-responder")
    location = locator.geocode(location_name)

    if not location:
        raise ValueError("Location not found. Please try again.")
    
    tf = TimezoneFinder()
    timezone = tf.timezone_at(lng=location.longitude, lat=location.latitude)

    if not timezone:
        raise ValueError("Could not determine timezone.")
    
    return timezone
        
def get_time(location_name):
    try:
        timezone = get_timezone(location_name)
        url = f"http://worldtimeapi.org/api/timezone/{timezone}"
        response = requests.get(url)

        if response.status_code != 200:
            raise ValueError("Unable to fetch time data.")
        
        data = response.json()
        datetime_str = data["datetime"]
        dt = datetime.fromisoformat(datetime_str.split(".")[0])
        formatted_time = dt.strftime("%I:%M %p")

        return f"The current time in {location_name.title()} ({timezone}) is {formatted_time}"
    
    except Exception as e:
        return f"Error: {str(e)}"
    
def convert_time_display(time_str):
    dt = datetime.fromisoformat(time_str)

    return dt.strftime("%I:%M %p")


