<p align="center">
  <img src="images/projectcover.png" alt="Project Cover"/>
</p>

> [中文说明请见 README.md](./README.md)

# MCP Weather Warning Service

This project is built on FastMCP and provides a professional weather and disaster alert assistant for cities in China and worldwide. It supports querying a unique LocationID by city name and retrieving real-time weather and disaster warnings. Seamlessly integrate this tool into your workflow to stay informed and protected, wherever you are.

## Features
- Query LocationID by city name
- Retrieve real-time weather and disaster alerts for any supported city worldwide

## Tool Overview
This project provides two core tools, which are designed to work together:
1. `lookup_city_tool(city: str)`: Query the unique LocationID for a given city name.
2. `get_warning_tool(city: str = "")`: Retrieve weather and disaster alerts for a specified city using its LocationID.

**Recommended workflow:** First use `lookup_city_tool` to obtain the LocationID for your target city, then pass this ID to `get_warning_tool` to get the latest alerts.

## Quick Start

### 1. Clone the repository
```bash
git clone git@github.com:Jayden-hong/MCP_weatherwarning_Server.git
cd MCP_weatherwarning_Server
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configuration
Edit `config.py` and fill in your QWeather API credentials. You can obtain these from https://dev.qweather.com/:
```python
API_HOST = "Your API host (see your QWeather console settings)"
API_KEY = "Your API key"
DEFAULT_ID = "101280606"  # Default to Longgang District; update as needed for your region. If you change this, also update the tool description in server.py.
```

### 4. Start the service
```bash
python3 server.py
```
Or use the procfile:
```bash
# procfile
worker: python3 server.py
```

## API Reference
- `lookup_city_tool(city: str)`: Query the LocationID for a city
- `get_warning_tool(city: str = "")`: Retrieve weather and disaster alerts for a specified city

## Dependencies
- requests
- fastmcp

## Configuring mcp.json for Cursor Client

To use this MCP tool service locally in the Cursor client, add the following configuration to your `.cursor/mcp.json` file:

```json
{
  "weather-tools": {
    "command": "/path/to/your/python3",
    "args": [
      "/path/to/your/project/server.py"
    ],
    "env": {}
  }
}
```

- `command`: The absolute path to your Python interpreter (preferably from your virtual environment)
- `args`: The absolute path to your `server.py`
- `env`: Set any required environment variables here (usually can be left empty)

> Tip: Activate your virtual environment and load your `.env` file before starting Cursor to ensure all environment variables are available to the MCP tool. 