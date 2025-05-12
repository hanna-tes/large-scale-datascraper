import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os

# Set environment variables
os.environ['CHROME_BIN'] = '/usr/bin/chromium'
os.environ['CHROME_DRIVER'] = '/usr/bin/chromedriver'

st.title("✅ Chromium Test")

if st.button("Launch Browser"):
    try:
        # Configure browser
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.binary_location = "/usr/bin/chromium"

        # Launch browser
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )

        driver.get("https://example.com ")
        st.success(f"Page title: {driver.title}")
        driver.quit()

    except Exception as e:
        st.error(f"Error: {str(e)}")
