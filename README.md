# Knitting Project Calculator 🧶

## Description

The Knitting Project Calculator is a command-line Python program that helps users calculate how much yarn and money they have spent on individual knitting projects. The program guides the user through a menu-driven interface and validates all inputs to prevent invalid data.

## Features

- Add a new knitting project
- Calculate:
    - Total yarn used (in grams)
    - Total cost of yarn
- Menu-based navigation
- Input validation with clear error messages
- Option to return to the main menu at any time by pressing Enter

## File structure

```bash
knitting_project_calculator/
│
├── README.md
├── LICENSE
├── src/
│ ├── main.py # Main program loop and user interaction
│ └── functions.py # Helper functions for input, validation, and calculations
└── .gitignore
```

## How to run

- To get a local copy of the project:

    ```bash
    git clone https://github.com/henrikawerling/knitting_project_calculator.git
    cd knitting_project_calculator/src
    ```

- Make sure Python 3 is installed.

- Run the program:
    - Windows: ```python main.py```
    - macOS / Linux: ```python3 main.py```

## Usage

- Select an option from the main menu by entering ```1``` or ```2```.
- Follow the prompts to enter project details.
- Press Enter without typing anything at any prompt to return to the main menu or exit the program.

## Future improvements

- Store projects in a data structure or file so they persist between program runs
- Implement the “List all projects” feature
- Display summary statistics (total yarn used and total cost across all projects)
- Reduce repeated input-validation logic by introducing reusable helper functions
- Add automated tests for validation and calculation functions

## License

MIT license
