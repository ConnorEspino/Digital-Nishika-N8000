#!/bin/bash

# List of dependencies
DEPENDENCIES=(
    fltk
    wiringpi
    i2c-tools
    libi2c-dev
    python-smbus
)

# Check and install dependencies
for dep in "${DEPENDENCIES[@]}"; do
    if ! dpkg -s "$dep" > /dev/null 2>&1; then
        echo "Installing $dep..."
        sudo apt-get install -y "$dep"
    else
        echo "$dep is already installed."
    fi
done

echo "Dependencies installation complete."
