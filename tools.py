import json

# Real Python tools for the assistant
def get_weather(location: str) -> str:
    # Mock API response
    return json.dumps({"location": location, "temperature": "72°F", "condition": "Sunny"})

def create_calendar_event(title: str, date_time: str) -> str:
    # Mock Calendar API call
    return json.dumps({"status": "Success", "event": title, "scheduled_at": date_time})

# Map function names to executable Python functions
tool_map = {
    "get_weather": get_weather,
    "create_calendar_event": create_calendar_event
}
