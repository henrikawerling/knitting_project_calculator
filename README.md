# Knitting Project Calculator 🧶

## Description

The Knitting Project Calculator is a command-line Python program that helps users calculate how much yarn and money they have spent on individual knitting projects. The program guides the user through a menu-driven interface and validates all inputs to prevent invalid data.

## Features

- Add a knitting project
- Calculate total yarn used and total cost of yarn
- List all projects and calculate total yarn and cost of all (not yet implemented)
- Menu-based navigation
- Input validation with error messages
- Return to the main menu at any time by pressing Enter

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

## How to run & Usage

- To get a local copy of the project:

    ```bash
    git clone https://github.com/henrikawerling/knitting_project_calculator.git
    cd knitting_project_calculator/src
    ```

- Make sure Python 3 is installed.

- Run the program:
    - Windows: ```python main.py```
    - macOS / Linux: ```python3 main.py```

- Select an option from the main menu.
- Follow the prompts to enter project details.
- Hit enter (without typing anything) at any prompt to return to the main menu and/or exit the program.

### Example input and output:

![screenshot from terminal with entered inputs and the resulting output](<examples/usage_example.png>)

## License

MIT license
