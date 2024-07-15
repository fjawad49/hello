import requests

def get_current_time(timezone):
    """Fetches the current time from the WorldTimeAPI for a specified timezone."""
    base_url = "http://worldtimeapi.org/api/timezone/"
    complete_url = f"{base_url}{timezone}"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if response.status_code == 200:
        # Assuming the datetime key is present in the response
        current_time = data['datetime']
        return current_time
    else:
        print("Failed to get time data")
        return None

def main():
    timezone = input("Enter the timezone (e.g., Europe/London): ")
    current_time = get_current_time(timezone)
    
    if current_time:
        print(f"Current time in {timezone} is: {current_time}")

if __name__ == "__main__":
    main()