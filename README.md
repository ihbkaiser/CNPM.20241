# Introduction to Software Engineer - Group 11
Thank you to all the contributors! 🎄✨ We all wish you a Merry Christmas 🎅🎁 and a Happy New Year! 🎆🎉  
<div style="display: flex; gap: 10px; align-items: center;">
  <a href="https://github.com/TranDucChinh">
    <img src="https://avatars.githubusercontent.com/u/12264354?s=64" alt="TranDucChinh" style="border-radius: 50%; width: 64px; height: 64px;"/>
  </a>
  <a href="https://github.com/ihbkaiser">
    <img src="https://avatars.githubusercontent.com/u/53372458?s=64" alt="ihbkaiser" style="border-radius: 50%; width: 64px; height: 64px;"/>
  </a>
  <a href="https://github.com/langkhachhoha">
    <img src="https://avatars.githubusercontent.com/u/10720962?s=64" alt="langkhachhoha" style="border-radius: 50%; width: 64px; height: 64px;"/>
  </a>
  <a href="https://github.com/chung140204">
    <img src="https://avatars.githubusercontent.com/u/104688868?s=64" alt="chung140204" style="border-radius: 50%; width: 64px; height: 64px;"/>
  </a>
</div>

![Coverage Status](https://img.shields.io/badge/coverage-90%25-brightgreen)
![Last Commit](https://img.shields.io/github/last-commit/ihbkaiser/CNPM.20241)
![Repo Size](https://img.shields.io/github/repo-size/ihbkaiser/CNPM.20241)
![Contributors](https://img.shields.io/github/contributors/ihbkaiser/CNPM.20241)
![Issues](https://img.shields.io/github/issues/ihbkaiser/CNPM.20241)
![Pull Requests](https://img.shields.io/github/issues-pr/ihbkaiser/CNPM.20241)
![Forks](https://img.shields.io/github/forks/ihbkaiser/CNPM.20241?style=social)
![Stars](https://img.shields.io/github/stars/ihbkaiser/CNPM.20241?style=social)
![Commit Activity](https://img.shields.io/github/commit-activity/m/ihbkaiser/CNPM.20241)
![Open Issues](https://img.shields.io/github/issues/ihbkaiser/CNPM.20241)
![Closed Issues](https://img.shields.io/github/issues-closed/ihbkaiser/CNPM.20241)
![Language Count](https://img.shields.io/github/languages/count/ihbkaiser/CNPM.20241)
![Top Language](https://img.shields.io/github/languages/top/ihbkaiser/CNPM.20241)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows-lightgrey)


<div style="text-align: center;">
    <img src="assets/INTRO.png" alt="Introduction Image">
</div>

## 1. Instructions for Windows Users

### Step 1: Install MySQL Server and MySQL Workbench
- Download [MySQL Installer](https://dev.mysql.com/downloads/installer/) for Windows.
- Run the installer and select the following components:
  - MySQL Server
  - MySQL Workbench
- Follow the installation wizard:
  1. Set up the MySQL Server with a root password.
  2. Configure the MySQL Server to run as a service.
  3. Test the MySQL Workbench connection to ensure it's working.

### Step 2: Clone the Repository
- Open a terminal (Command Prompt or PowerShell) and execute:
  ```bash
  git clone https://github.com/ihbkaiser/CNPM.20241.git
  cd CNPM.20241
  ```
### Step 3: Configure Parameters
- Open the `config.yml` file in a text editor.
- Update the `user` and `password` fields with your MySQL credentials (e.g., the root password set during installation).
- Obtain an API key from [OpenWeather](https://home.openweathermap.org/users/sign_up).
- Replacing `YOUR_API_KEY` with your actual OpenWeather API key:
    ```yaml
    weather:
        api_key: YOUR_API_KEY
    ```
### Step 4: Create a Virtual Environment
```
python -m venv venv
venv/Scripts/activate
```
### Step 5: Install Dependencies
```
pip install -r requirements.txt
```
### Step 6: Run the Project
```
python main.py
```
## 2. Instructions for Linux Users
<p style="color:yellow; background-color:black; padding:5px;">
<strong>Our app may behave unexpectedly for Linux users. Use at your own risk.</strong>
</p>

Simply run the following command to test our project:

```bash
./se11.sh
```
If you encounter errors while running `./se11.sh`, you may need to convert the script to UNIX format:
```
sudo apt install dos2unix
dos2unix se11.sh
```
## 3. Optional
Our group also provides a `mock_data.sql ` file, which can be executed in MySQL Workbench to generate sample data simulating an apartment for testing our application.




