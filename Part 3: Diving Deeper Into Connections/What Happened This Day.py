import requests


def fetch_on_this_day(month, day):
    url = f"https://en.wikipedia.org/api/rest_v1/feed/onthisday/events/{month}/{day}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("events", [])
    except requests.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return []


def display_events(events):
    if not events:
        print("No historical events found for this day.")
        return

    print(f"\nHistorical events:")
    for event in events:
        year = event.get("year", "Unknown Year")
        text = event.get("text", "No description available.")
        print(f"- {year}: {text}")


def on_this_day():
    print("Welcome to the Historical Events Lookup!")
    try:
        month = int(input("Enter month (1 - 12): "))
        day = int(input("Enter day (1 - 31): "))
        if not (1 <= month <= 12 and 1 <= day <= 31):
            print("Invalid date. Please enter valid month and day values.")
            return

        events = fetch_on_this_day(month, day)
        display_events(events)

    except ValueError:
        print("Invalid input! Please enter numeric values for month and day.")


on_this_day()
