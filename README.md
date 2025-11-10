
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