#!/bin/bash
# system dependencies needed for Chromium
echo "Starting setup.sh"
apt-get update && apt-get install -y \
    libnss3 \
    libx11-xcb1 \
    libxcb1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libxcomposite1 \
    libxrandr2 \
    libgbm1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libx11-6 \
    libxss1 \
    libgconf-2-4 \
    libnss3-tools \
    fonts-liberation \
    libappindicator1 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libdrm2 \
    xdg-utils \
    wget \
    ca-certificates \
    fonts-ipafont-gothic
echo "System dependencies installed"
# install playwright dependencies
pip install -r requirements.txt
echo "Python dependencies installed"
# install only Chromium 
playwright install chromium
echo "Chromium installed"
echo "setup.sh completed"
