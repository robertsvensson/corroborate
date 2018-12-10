# corroborate
Give any Web Application Security Scanner a run for its money

## What is corroborate
I created corroborate as a testing ground when I was looking to buy a Web Application Security Scanner to scan a number of public website for vulnerabilities.

The core of Corroborate is a security-flawed web app. You can use Corroborate to test if the Web Application Security Scanner you're evaluating is any good.

## List of vulnerabilities
Corroborate currently has the following vulnerabilities

- Outdated libraries
- Sensitive information in source code

## Usage

git clone https://github.com/robertsvensson/corroborate.git

cd corroborate/

python3 -m venv .

source bin/activate

export FLASK_APP=corroberate.py

flask run --host=0.0.0.0

This will start a server running on 0.0.0.0:5000. Now scan away

![Screen](screenshot.png)
