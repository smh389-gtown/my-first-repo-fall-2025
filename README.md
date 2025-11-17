
# My First Repo!
Learning and Practicing Version Control


## Setup
Clone the Repo to download it from GitHub. Perhaps onto the Desktop.



Create a virtual environment
```sh
conda create -n my-frist-env-fall-2025 python=3.11
```
Activate the virtual environment
```sh
conda activate my-frist-env-fall-2025
```
Install dependences:

```sh
pip install -r requirements.txt
```


Navigate to the repo using the command line.


```sh
cd ~/Desktop/my-first-repo-fall-2025
```
## Configuration
The stocks functionality requires an AlphaVantage API key. Obtain a premium AlphaVantage API Key (using the [form](https://www.alphavantage.co/support/#api-key) or shared by the prof).

Create a local ".env" file and store your environment variable in there:


```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="______________"
#also tell flask where our web app is defined:
FLASK_APP=web_app
```



## Usage
Example script:

```sh
python apps/my_script.py

```
Game of rock, paper, scissors:

```sh
python apps/rps.py

# alternative "modular style" command
python -m apps/rps

```


Stocks Dashboard

```sh
python -m apps/stocks.py
```


### Web App
Run the web app (then view in the browser at http://localhost:5000/):

```sh
# if we have the FLASK_APP=web_app env var in the .env file
flask run


# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

## Testings

Run tests:

```sh
pytest
```