"""Main entry point for the Knitting Project Calculator.

This module controls program flow, menu navigation, and user interaction.
"""

import sys
from functions import *

def main():
    """Run the main program loop."""
    print_welcome_msg()

    projects = []
    total_yarn_amount = 0
    total_yarn_price = 0

    while True:
        print_main_menu()
        main_menu_selection = input("")

        if is_empty(main_menu_selection):
            sys.exit("Bye, see you next time!\n")

        if not is_valid_main_menu_selection(main_menu_selection):
            print_invalid_input_msg()
            continue

        # Add new project workflow
        if main_menu_selection == "1":
            print()
            project_name = input("Project name: ")
            if is_empty(project_name):
                continue
            
            print()
            yarn_name = input("Yarn name: ")
            if is_empty(yarn_name):
                continue

            print()
            grams_per_skein = get_validated_input(
                "Grams per skein: ", is_valid_int
            )
            if grams_per_skein is None:
                continue

            print()
            price_per_skein = get_validated_input(
                "Price per skein: ", is_valid_float
            )
            if price_per_skein is None:
                continue

            print()        
            number_of_skeins = get_validated_input(
                "Number of skeins used: ", is_valid_int
            )
            if number_of_skeins is None:
                continue
            
            projects.append(project_name)

            project_yarn_amount = calculate_project_yarn_amount(
                grams_per_skein, number_of_skeins
            )
            project_yarn_price = calculate_project_yarn_price(
                price_per_skein, number_of_skeins
            )

            total_yarn_amount += project_yarn_amount
            total_yarn_price += project_yarn_price

            show_result(
                project_name, project_yarn_amount, yarn_name, 
                project_yarn_price
            )

        # List all projects workflow
        elif main_menu_selection == "2":
            if not projects:
                print()
                print("You do not have any projects.")
            else:
                show_list_of_projects(projects)
                print()
                show_number_of_projects(projects)
                show_total_yarn_usage(total_yarn_amount)
                show_total_yarn_price(total_yarn_price)

if __name__ == "__main__":
    main()