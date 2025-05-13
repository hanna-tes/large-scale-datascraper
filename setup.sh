#!/bin/bash

# Install Chrome dependencies
apt-get update
apt-get install -y wget curl gnupg2 unzip software-properties-common

# Add Google Chrome’s signing key
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -

# Add Chrome repository
sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Install Chrome
apt-get update
apt-get install -y google-chrome-stable

