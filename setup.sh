#!/bin/bash
echo "Starting setup.sh"

# Update package lists
apt-get update -y

# Install Chromium system-wide (no sandbox for Streamlit Cloud)
apt-get install -y chromium

echo "Chromium installed system-wide"

# Install Python dependencies
pip install -r requirements.txt
echo "Python dependencies installed"

# Tell Playwright to use the system-installed Chromium
export PLAYWRIGHT_BROWSERS_PATH=/usr/bin

echo "PLAYWRIGHT_BROWSERS_PATH set to /usr/bin"

echo "setup.sh completed successfully"
exit 0
