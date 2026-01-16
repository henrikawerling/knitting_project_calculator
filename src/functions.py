"""Functions for the Knitting Project Calculator.

This module contains all user interface messages, input helpers,
validation functions, and calculation utilities used by the main program.
"""

# Message printing functions

def print_welcome_msg():
    print("""
-------------------------------------------
Welcome to the Knitting Project Calculator
-------------------------------------------

This calculator helps you count the amount of yarn and money you have 
spent on your knitting projects.

- Add a knitting project to see how much yarn you used for it and how much it 
  cost you.

- List all your knitting projects to see how much yarn you have used in total 
  and how much the projects have cost you in total.

- Hit enter at any time to go back to the main menu.
""")


def print_farewell_msg():
    print("Bye, see you next time!")
    print()


def print_invalid_input_msg():
    print()
    print("Invalid input, please try again!")


def print_not_available_msg():
    print()
    print("Sorry, this feature is not available yet!")


def print_not_integer_error_msg():
    print()
    print("Please give a whole number!")


# Input validation functions

def is_empty(user_input):
    """Check if the input is empty or contains only whitespace."""
    if not user_input.strip():
        return True
    return False


def is_valid_int(user_input):
    """Validate that the input is a non-negative integer.

    Returns the integer value if valid, otherwise None.
    """
    try:
        user_input = int(user_input)
        if user_input < 0:
            print_invalid_input_msg()  # move printing of messages to main?
            return None
        else:
            return user_input
    except ValueError:
        if "," in user_input or "." in user_input:
            print_not_integer_error_msg()
        else:
            print_invalid_input_msg()
        return None


def is_valid_float(user_input):
    """Validate that the input is a non-negative floating-point number.

    Returns the float value if valid, otherwise None.
    """
    try:
        user_input = float(user_input)
        if user_input < 0:
            print_invalid_input_msg()  # move printing of messages to main?
            return None
        else:
            return user_input
    except ValueError:
        print_invalid_input_msg()
        return None


# Main menu functions

def print_main_menu():
    print("""
Main menu (hit enter to quit)

1. Add new project

2. List all projects
""")


def get_user_input():
    return input("")


def is_valid_main_menu_selection(main_menu_selection):
    """Convert a valid menu selection into a readable command."""
    if main_menu_selection not in ["1", "2"]:
        return None
    if main_menu_selection == "1":
        return "add new project"
    elif main_menu_selection == "2":
        return "list all projects"


# Add new project input and calculation functions

def get_project_name():
    print()
    return input("Project name: ")


def get_yarn_name():
    print()
    return input("Yarn name: ")


def get_grams_per_skein():
    print()
    return input("Grams per skein: ")


def get_number_of_skeins():
    print()
    return input("Number of skeins used: ")


def get_price_per_skein():
    print()
    return input("Price per skein: ")


def calculate_project_yarn_amount(skein_weight, skein_amount):
    return skein_weight * skein_amount


def calculate_project_yarn_price(skein_price, skein_amount):
    return skein_price * skein_amount


def show_result(project_name, project_yarn_amount, yarn_name, project_yarn_price):
    """Display a summary of the project including yarn usage and cost."""
    print()
    print(
        f"For {project_name} you used {project_yarn_amount} grams of "
        f"{yarn_name} and it cost you {project_yarn_price:.2f} euros."
    )
    print()


# List all projects functions

def show_list_of_projects(projects):
    print()
    print("Here's a list of all your projects:")
    print()
    for project in projects:
        print(project)


def show_number_of_projects(projects):
    print(f"You have a total of {len(projects)} knitting projects.")


def show_total_yarn_usage(total_yarn_amount):
    print(f"In total you have used {total_yarn_amount} grams of yarn for your projects.")


def show_total_yarn_price(total_yarn_price):
    print(f"The total cost of your projects is {total_yarn_price:.2f} euros.")