# Mouse Clicker
A simple useless (is it?) python script for emulating mouse clicks periodically for a given duration.

### Requirements

- python 3.5 or above
- autopy

### Usage

Clone the repository and navigate to the project directory

```
git clone https://github.com/Arutselvan/mouse_clicker
cd mouse_clicker
```

Install dependencies

```
pip install -r requirements.txt
```

Run the script

```
python mouse_clicker.py
```

Run the script with custom duration and frequency values

```
python mouse_clicker.py --frequency=60 --duration=120
```

```
usage: mouse_clicker.py [-h] [--duration DURATION] [--frequency FREQUENCY]

optional arguments:
  -h, --help            show this help message and exit
  --duration DURATION   Running duration of the script (in minutes)
  --frequency FREQUENCY
                        Frequency of mouse clicks (in seconds)
```

