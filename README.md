
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

## Testings

Run tests:

```sh
pytest
```