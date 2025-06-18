# Pokemon Battle Game

## 🤝 Pair Programmed by 

<table>
  <tr>
    <td><strong>Iohane</strong><br>
      <a href="https://github.com/Yoyo-su">
        <img src="https://img.shields.io/badge/GitHub-000?logo=github&logoColor=white" />
      </a><br>
    </td>
    <td><strong>Myles</strong><br>
      <a href="https://github.com/TraderMyles">
        <img src="https://img.shields.io/badge/GitHub-000?logo=github&logoColor=white" />
    </td>
  </tr>
</table>

## 🔰 Overview
A Pokemon battle game using Object-Oriented Programming (OOP) principles, where two users can choose their own Pokemon and battle against each other. The game is designed to be played in the terminal, with a simple text-based interface.

## 🔧 Tech Stack
- **Python 3.13** - Primary programming language
  - **Pytest** - Test Driven Development (TDD)
- **Github** - Repository management

## 🏛️ Architecture

The application uses a python script, **game.py**, that contains the main game logic.
The game allows two players to choose 6 Pokemon each and battle against each other. Each player can choose from a list of available Pokemon, and the game will handle the battle mechanics, including hitpoint calculations, and victory conditions.

The game is structured using Object-Oriented Programming (OOP) principles, with the following classes defined in the **pokemon.py** file:
- **Pokemon**, including their attributes and methods
- Child classes for each Pokemon type (**Fire**, **Water**, **Grass** & **Normal**)
- **Pokeball**, which is used to capture and store Pokemon
- **Trainer**, which manages the players belt containing their Pokemon
- **Battle**, which handles the battle mechanics between two Pokemon

Each method is tested individually using TDD in the test/test_pokemon.py file.


## 📁 File Structure

```
NC-POKEMON
├── src
│   ├── game.py             # Main application file for the Pokemon battle game
│   └── pokemon.py          # Contains the class objects for Pokemon, Pokeball, Trainer, and Battle
├── tests/                          
│   └── test_pokemon.py     # Unit tests for python functions (pytest)
├── .gitignore                      # Files not to be pushed to remote repository
├── README.md                       # Documentation
└── requirements.txt                # Third party Python modules required to run the application
```

## 🚀 Setup

To run the game locally on a Linux or MacOS machine, please follow these steps:

1. Ensure you have Python 3.13 installed on your machine.

2. Clone the repository to your local machine:
    ```bash
        git clone https://github.com/Yoyo-su/NC-Pokemon.git
    ```

3. Navigate to the project directory:
    ```bash
        cd NC-Secrets-Manager
    ```

4. Setup the local virtual environment by running the following commands:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. To run the tests, use:
    ```bash
    pytest tests/test_pokemon.py
    ```

7. To run the application, use:
    ```bash
    python src/game.py
    ```

##
*A Northcoders Data Engineering Bootcamp Project*
