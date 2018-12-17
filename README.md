# ParseIt 
[![Build Status](https://travis-ci.org/adityaprakash-bobby/opengenus_internship_task.svg?branch=master)](https://travis-ci.org/adityaprakash-bobby/opengenus_internship_task)
---
A simple script to fetch details about a webpage :
- The size of webpage
- The total links in the webpage in the same domain

### Setup and execute:
```bash
git clone https://github.com/adityaprakash-bobby/opengenus_internship_task.git
cd opengenus_internship_task

# create a virtual environment
virtualenv venv
. venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run the script
python app.py <link to the webpage> # eg.: https://www.google.com

# run the Tests
python app_test.py
```
