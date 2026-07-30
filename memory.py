tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Fetch current weather for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name, e.g. New York, NY"}
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_calendar_event",
            "description": "Schedule a calendar event for a user.",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "Event name"},
                    "date_time": {"type": "string", "description": "Date and time ISO string"}
                },
                "required": ["title", "date_time"]
            }
        }
    }
]
