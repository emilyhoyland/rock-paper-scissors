
# Rock Paper Scissors

A virtual twist on a classic childhood game

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/emilyhoyland/rock-paper-scissors) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd rock-paper-scissors
```

Use Anaconda to create and activate a new virtual environment, perhaps called "rock-paper-scissors-env":

```sh
conda create -n rock-paper-scissors-env python=3.8
conda activate rock-paper-scissors-env
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

## Setup

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username (then make sure to SAVE the ".env" file aftwards):

    PLAYER_NAME="My Name"
  
## Usage

Run the Python script:

```py
python game.py
```

NOTE: User input is CASE SENSITIVE