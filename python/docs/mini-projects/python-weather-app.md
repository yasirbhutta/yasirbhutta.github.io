---
layout: page
title: "Mini Project: Simple Weather App with API Integration"
description: Learn how to use the SUM function and AutoSum in Microsoft Excel to quickly add values across cells, columns, or rows. Includes syntax, examples, and tips for efficient usage.
keywords: Excel SUM function, how to use SUM in Excel, Excel functions guide, Excel SUM formula, Excel add cells, Excel basics, Excel tutorials, Microsoft Excel functions, SUM formula examples
---

**Learning focus:**

- Python API requests
- JSON data handling
- User input processing
- Exception and error handling
- Displaying API results

## **1. Project Overview**

Develop a simple Weather Application using Python that retrieves current weather information from an external Weather API.

The application should allow users to enter a city name and display its current weather information.

## **2. Required Features**

1. **Search by City:** Enter a city name to retrieve weather information.
2. **Display Weather Information:**
   - City name and country
   - Temperature in Celsius
   - Weather condition (sunny, rainy, cloudy, etc.)
   - Humidity percentage
   - Wind speed
   - Weather description
3. **Error Handling:**
   - Invalid city name
   - Internet connection problems
   - Invalid API key
   - API response errors

## **3. Implementation Steps**

### **Step 1: Get a Free API Key**

Register at [OpenWeatherMap API](https://openweathermap.org/) and obtain a free API key.

### **Step 2: Install Required Python Library**

Open the terminal or command prompt and execute:

```bash
pip install requests
```

**Library:** `requests`

Purpose: To send HTTP requests to the Weather API and receive weather information.

### **Step 3: Create Project Files**

Create a project folder named `WeatherApp` with the following files:

```
WeatherApp/
│
├── config.py
├── weather.py
└── main.py
```

### **Step 4: Create&#x20;**`config.py`**&#x20;(API Configuration)**

Store the API key and API URL in this file.

```python
API_KEY = "type your api key here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
```

Replace `your_api_key_here` with your actual API key.

### **Step 5: Create **`weather.py`** (API Integration)**

This file will contain the function responsible for retrieving weather information.

```python
import requests
from config import API_KEY, BASE_URL


def get_weather(city):

    # API request parameters
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        # Send GET request to the Weather API
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        # Check for HTTP errors
        response.raise_for_status()

        # Convert JSON response into a Python dictionary
        data = response.json()

        # Extract required weather information
        weather = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": round(data["main"]["temp"]),
            "humidity": data["main"]["humidity"],
            "wind": data["wind"]["speed"],
            "description": data["weather"][0]["description"]
        }

        return weather

    # Handle HTTP errors
    except requests.exceptions.HTTPError:

        if response.status_code == 404:
            print("Error: City not found.")

        elif response.status_code == 401:
            print("Error: Invalid API key.")

        else:
            print("Error: Unable to retrieve weather data.")

    # Handle connection and timeout errors
    except requests.exceptions.RequestException:
        print("Error: Please check your internet connection.")

    # Handle JSON and missing data errors
    except (KeyError, ValueError):
        print("Error: Invalid weather data received.")

    return None
```

### **Step 6: Create& **`main.py`** (Main Application)**

This file will accept the city name from the user and display the weather information.

```python
import weather

print("===== WEATHER APPLICATION =====")
city = input("Enter city name: ")
weather = weather.get_weather(city)

if weather:
    print("\n===== CURRENT WEATHER =====")
    print("City:", weather["city"])
    print("Country:", weather["country"])
    print("Temperature:", weather["temperature"], "°C")
    print("Weather:", weather["description"])
    print("Humidity:", weather["humidity"], "%")
    print("Wind Speed:", weather["wind"], "m/s")
else:
    print("Unable to display weather information.")
```

### **Step 7: Run the Application**

Open the terminal in the project folder and execute:

```bash
python main.py
```

**Sample Output**

## **WEATHER APPLICATION**

Example output – illustrative values

**Enter city name:** Dera Ghazi Khan

# **28°C**

**Dera Ghazi Khan, PK**

**Clear Sky**

**Humidity**

35%

**Wind Speed**

3.5 m/s

## **4. Key Learning Points**

| Concept            | Learning outcome                           |
| ------------------ | ------------------------------------------ |
| API Integration    | Connect Python with an external API        |
| Requests Library   | Send HTTP GET requests                     |
| JSON Handling      | Extract information from JSON responses    |
| Dictionaries       | Store and access weather information       |
| Functions          | Organize code into reusable functions      |
| Exception Handling | Handle API and connection errors           |
| Modules            | Divide the application into separate files |

## **5. Suggested Enhancement Ideas**


**5-Day Weather Forecast**

Retrieve and display weather information for the next five days.

[Retrieve and display weather information for the next five days](https://images.openai.com/static-rsc-4/A_bw0FaugQDDxDmOBIYcycbrV4k2gps-PaznHhFc5pajIBxoCebKgZjnwcLwQrQfFAL6RBn2pkuuXGpwIBTDrLkLiiB0MzKwMax42y_tPOfKsqFYCO52kVoR-5KYDvs_1oLkLofRNSDPXLy2x_JvwDuFlavPGQGOmMUxal_OC_w?purpose=inline)

**Web-Based Weather Application**

Use Python Flask with HTML and CSS to develop a web application.

