#!/bin/bash
echo "Setting up SE11's project"
sudo apt update
sudo add-apt-repository -y universe
sudo apt install -y python3 python3-tk python3-venv python3-pip expect
python3 -m venv se11_env
source se11_env/bin/activate

if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

echo "Installing MySQL Server..."
sudo apt install -y mysql-server

echo "Adding MySQL user..."
if [ -f setup.sql ]; then
    # Using expect to handle password input
    expect -c "
    spawn sudo mysql -u root -p
    expect \"Enter password:\"
    send \"\r\"
    expect \"mysql>\"
    send \"source setup.sql\r\"
    expect \"mysql>\"
    send \"exit\r\"
    interact
    "
else
    python3 mysql_setup.py
    if [ -f setup.sql ]; then
        # Using expect to handle password input
        expect -c "
        spawn sudo mysql -u root -p
        expect \"Enter password:\"
        send \"\r\"
        expect \"mysql>\"
        send \"source setup.sql\r\"
        expect \"mysql>\"
        send \"exit\r\"
        interact
        "
    fi
fi

echo "Enjoy!"
if [ -f main.py ]; then
    python3 main.py
fi

deactivate
