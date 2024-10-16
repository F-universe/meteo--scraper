from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from flask import Flask, render_template, request
import time

# Set the path to your chromedriver
CHROMEDRIVER_PATH = r'C:\Users\fabio\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# Configure Flask
app = Flask(__name__)

# Configure Selenium
def get_weather_status(location):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run the browser in headless mode (optional)
    service = Service(CHROMEDRIVER_PATH)
    browser = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # URL to visit
        url = f"https://it.search.yahoo.com/search?fr=mcafee&type=E210IT91082G0&p=meteo+{location}"
        browser.get(url)
        
        # Wait a few seconds for the page to load
        time.sleep(3)
        
        # Search for the specific class
        elements = browser.find_elements(By.CLASS_NAME, "reg.searchTop")
        
        # Check if the class is present and download the data
        if elements:
            data = [element.text for element in elements]
            return "Class found! Data: " + "\n".join(data)
        else:
            return "Class not found."

    finally:
        # Close the browser
        browser.quit()

# Main route
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        location = request.form['location']
        result = get_weather_status(location)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)