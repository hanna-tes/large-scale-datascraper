#!/bin/bash

# Install system dependencies needed by Chromium
apt-get update && apt-get install -y \
    wget \
    ca-certificates \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libgbm1 \
    libasound2 \
    libxshmfence1 \
    libxss1 \
    libxtst6 \
    lsb-release \
    fonts-liberation \
    libappindicator3-1 \
    xdg-utils

# Install Playwright and Chromium
pip install -r requirements.txt
playwright install chromium
