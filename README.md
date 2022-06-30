<img src="media/bomb2.png" align="right" />

# Terminal Blaster ![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
> A text based version of classic minesweeper

Project created while learning the python programming language

## Tech used

Python 3.6+ with external packages:
*  [pyspellchecker](https://pyspellchecker.readthedocs.io/en/latest/#)
* [pandas](https://pandas.pydata.org/)

## Table of content

- [Features](#features)
- [Description of files](#description-of-files)
- [Getting started](#getting-started)
    - [Installation](#installation)
- [Usage](#usage)
    - [How to navigate](#how-to-navigate)
    - [How to play](#how-to-play)
    - [Other](#other)
- [Credits](#credits)
- [License](#license)


## Features

* Minimum moves to complete the board
* Moves efficiency
* Leaderboard update; remove scores

## Description of files

| Filename | Description |
|---|---|
| saper2.py | Python file, here is a game |
| README.md | Markdown-formatted text file with a project description |
| my_words.json | Dictionary words are stored in json data files |
| sb.csv | The csv file contains the scoreboard data |
| media | In this folder can be found GIF's and images |
| LICENSE.md |  The MIT License in Markdown text file |

## Getting started

### Installation

Install with pip:
* `$ pip install saper2.py`
* `$ saper2.py`


## Usage

> Once you setup game you are ready to run it

### How to navigate

* The menu is designed with simple instructions; **select an action** and press **Enter**
<p align="center">
<img src="media/demo.gif" width="" height="280" />
</p> 

### How to play

* Enter a cell's coordinates to make it visible **X Y** (width, height)
<figure align="center">
<img src="media/demo1.gif" alt="my alt text" width="550" height=""/>
<figcaption>[noguess mode] Level easy: grid size 9x9 (8 6 are the coords of S)</figcaption>
</figure>

* Put a **F** at the end of the coordinates to flag a cell **X Y F**
<figure align="center">
<img src="media/demo2.gif" alt="my alt text" width="550" height=""/>
<figcaption>Simply repeat the command to unflag a cell </figcaption>
</figure>

* If you succeed, enter your name to **keep your score**
<figure align="center">
<img src="media/demo4.gif" alt="my alt text" width="550" height=""/>
<figcaption>From the main menu, you may access the leaderboard </figcaption>
</figure>

### Other

* The scoreboard has a sorting feature
<figure align="center">
<img src="media/demo5.gif" alt="my alt text" width="550" height=""/>
<figcaption>Scoreboard only supports standard and noguess modes and always displays the top 10 results. </figcaption>
</figure>

* A misspelling will be corrected by the [pyspellchecker](https://pyspellchecker.readthedocs.io/en/latest/#) module
<figure align="center">
<img src="media/demo3.gif" alt="my alt text" width="550" height=""/>
<figcaption>Works only for a game modes </figcaption>
</figure>

* You can alter the board size and mines number in the saper2.py file (**not advised**), or you can just switch to god mode. Open **saper.py** in your code editor use shortcut `ctrl + f` and search for **def run_game():**

```python
def run_game():
    easy = Board(9, 9, 10, 1200)
    medium = Board(16, 16, 40, 1200)
    advance = Board(16, 30, 100, 1200)
```
easy = Board(**height, width, bombs, timeout**)

## Credits

@thaiboyspeedrun - Without you, it would never have happend<3

<a href="https://www.flaticon.com/free-icons/bomb" title="bomb icons">Bomb icons created by Freepik - Flaticon</a>
















