Yahoo Weather Scraper with Flask

This project is a simple Python web application that scrapes weather information from Yahoo's search results based on user input. It uses Selenium for web scraping and Flask for the web interface.

How It Works

User Input: The user enters a location (e.g., "Siena") in the form on the web page.

Scraping Weather Data: The application uses Selenium to visit Yahoo's search page for the given location and attempts to find the weather information by searching for a specific CSS class (reg.searchTop).

Display Result: If the class is found, the data is returned and displayed on the web page. Otherwise, it informs the user that the class was not found.

Setup Instructions

Prerequisites

Python 3.x

Google Chrome browser installed

ChromeDriver that matches your Chrome version

Required Libraries

Install the necessary libraries using pip:

pip install Flask
pip install selenium

Running the Application

Clone this repository or download the Python script.

Set the path to your chromedriver in the CHROMEDRIVER_PATH variable in the script.

Place the index.html file in the templates folder:

<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Scraper</title>
</head>
<body>
    <h1>Check the Weather</h1>
    <form method="post">
        <label for="location">Enter Location:</label>
        <input type="text" id="location" name="location" required>
        <button type="submit">Search</button>
    </form>

    {% if result %}
    <h2>Result:</h2>
    <p>{{ result }}</p>
    {% endif %}
</body>
</html>

Run the Flask application:

python your_script_name.py

Open your browser and navigate to http://127.0.0.1:5000 to use the application.

Notes

Ensure you have the correct version of ChromeDriver for your Chrome browser.

The script runs Chrome in headless mode by default, meaning it won't open a visible browser window.

Disclaimer

This project is for educational purposes only. Web scraping may be subject to legal and ethical considerations. Always check the terms of service of the website you are scraping.
