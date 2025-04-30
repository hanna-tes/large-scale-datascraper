# Update package lists and install system dependencies
apt-get update && apt-get install -y \
    libnss3 \
    libx11-xcb1 \
    libxcb1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0

# Install Python dependencies from requirements.txt
pip install -r requirements.txt

# Install Playwright browser binaries
playwright install
