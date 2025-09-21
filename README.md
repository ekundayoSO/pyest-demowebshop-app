# End-to-End Testing - DemoWebShop Web App

This repository contains automated end-to-end (E2E) tests for the Demo Web Shop application.
The tests are written in Python and validate critical workflows such as registration, login, shopping cart logic, 
customer addresses, and navigation.

# Clone Repo
```bash
git clone https://github.com/ekundayoSO/pyest-demowebshop-app.git
cd pyest-demowebshop-app
```

# Install Dependencies
```bash
pip install -r requirements.txt 
```

# Run tests
```bash
Set Environment Variables Manually

On Windows:
set BROWSER=chrome, firefox ...
set RESULTS_DIR=path_to_your_report_directory
    
On Mac:
export BROWSER=chrome, firefox ...
export RESULTS_DIR=path_to_your_report_directory

Set Environment Variables using bash shell script
Windows:
env.bat

Mac:
chmod +x env.sh
source env.sh
```
```bash
cd pytest-demowebshop-app
run: pytest
```

