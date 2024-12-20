#!/bin/bash
echo "Setting up SE11's project"

# Update and install necessary packages
sudo apt update
sudo add-apt-repository -y universe
sudo apt install -y python3 python3-tk python3-venv python3-pip expect

# Set up the Python virtual environment
python3 -m venv se11_env
source se11_env/bin/activate

# Install required Python packages if 'requirements.txt' exists
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

# Install MySQL Server
echo "Installing MySQL Server..."
sudo apt install -y mysql-server

# Run mysql_setup.py first
echo "Running mysql_setup.py..."
python3 mysql_setup.py

echo "Adding MySQL user..."

# Using expect to handle password input for MySQL
expect -c "
spawn sudo mysql -u root -p
expect \"Enter password:\"
send \"\r\" 
expect \"mysql>\"
send \"SET GLOBAL log_bin_trust_function_creators=1;\r\"
expect \"mysql>\"
send \"source setup.sql\r\"
expect \"mysql>\"
send \"exit\r\"
interact
"

echo "Enjoy!"
if [ -f mock_data.sql ]; then
    echo "Running mock_data.sql..."
    expect -c "
    spawn sudo mysql -u root -p
    expect \"Enter password:\"
    send \"\r\"
    expect \"mysql>\"
    send \"source mock_data.sql\r\"
    expect \"mysql>\"
    send \"exit\r\"
    interact
    "
fi
# If main.py exists, run it
if [ -f main.py ]; then
    python3 main.py
fi

# Deactivate the Python virtual environment
deactivate
