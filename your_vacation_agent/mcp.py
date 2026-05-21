from fastmcp import FastMCP
from datetime import datetime, timezone, timedelta


mcp = FastMCP("Your Vacation Assistant MCP Server")


@mcp.tool
def get_weather(city: str) -> dict:
    """Get the current weather for a city.
    Note: uses mock data — replace with a real API (e.g. OpenWeatherMap) in production.
    """
    weather_data = {
        "tokyo": {"temperature_c": 22, "condition": "Partly cloudy", "humidity_pct": 65},
        "paris": {"temperature_c": 18, "condition": "Light rain", "humidity_pct": 82},
        "new york": {"temperature_c": 15, "condition": "Sunny", "humidity_pct": 40},
        "london": {"temperature_c": 12, "condition": "Overcast", "humidity_pct": 75},
        "sydney": {"temperature_c": 28, "condition": "Clear", "humidity_pct": 55},
    }
    data = weather_data.get(city.lower(), {"temperature_c": 20, "condition": "Clear", "humidity_pct": 50})
    return {"city": city, **data}

@mcp.tool
def get_current_time(city: str) -> dict:
    """Get the current local time for a city based on its UTC offset."""
    utc_offsets = {
        "tokyo": 9,
        "paris": 1,
        "new york": -5,
        "london": 0,
        "sydney": 11,
        "dubai": 4,
        "los angeles": -8,
    }
    offset_hours = utc_offsets.get(city.lower(), 0)
    local_time = datetime.now(timezone.utc) + timedelta(hours=offset_hours)
    return {
        "city": city,
        "local_time": local_time.strftime("%H:%M"),
        "date": local_time.strftime("%Y-%m-%d"),
        "utc_offset": f"UTC{offset_hours:+d}",
    }

@mcp.tool
def convert_currency(amount: float, from_currency: str, to_currency: str) -> dict:
    """Convert an amount between two currencies.
    Note: uses approximate rates — replace with a real API in production.
    """
    # Mock rates. Replace with a real API in production.
    rates_to_usd = {"USD": 1.0, "EUR": 1.17, "JPY": 0.0063, "GBP": 1.34, "AUD": 0.71, "CHF": 1.27}
    amount_in_usd = amount * rates_to_usd.get(from_currency.upper(), 1.0)
    converted = round(amount_in_usd / rates_to_usd.get(to_currency.upper(), 1.0), 2)
    return {
        "original": f"{amount} {from_currency.upper()}",
        "converted": f"{converted} {to_currency.upper()}",
    }


def get_travel_advisory(country: str) -> dict:
    """Get mock travel safety advisory information for a country."""
    advisory_data = {
        "turkiye": {
            "safety_level": 3,
            "advisory": "Exercise increased caution in large cities and near border areas.",
            "entry_requirements": "Some nationalities are visa-exempt for short stays; others need an e-Visa.",
        },
        "canada": {
            "safety_level": 1,
            "advisory": "Low overall risk. Follow normal safety precautions.",
            "entry_requirements": "Visa-exempt travelers may require an eTA when arriving by air.",
        },
        "netherlands": {
            "safety_level": 1,
            "advisory": "Low risk destination. Be mindful of petty theft in crowded tourist areas.",
            "entry_requirements": "Schengen entry rules apply; visa requirements depend on nationality.",
        },
    }

    default_advisory = {
        "safety_level": 3,
        "advisory": "No specific advisory data available. Exercise standard travel precautions.",
        "entry_requirements": "Check official immigration guidance for current entry rules.",
    }
    return {"country": country, **advisory_data.get(country.lower(), default_advisory)}
