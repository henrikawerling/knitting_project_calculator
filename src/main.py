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
        main_menu_selection = get_user_input()

        if is_empty(main_menu_selection):
            sys.exit(print_farewell_msg())

        main_menu_selection = is_valid_main_menu_selection(main_menu_selection)
        if not main_menu_selection:
            print_invalid_input_msg()
            continue

        # Add new project workflow
        if main_menu_selection == "add new project":
            project_name = get_project_name()
            if is_empty(project_name):
                continue
            
            yarn_name = get_yarn_name()
            if is_empty(yarn_name):
                continue
            
            while True:
                grams_per_skein = get_grams_per_skein()
                if is_empty(grams_per_skein):
                    grams_per_skein = None
                    break

                grams_per_skein = is_valid_int(grams_per_skein)
                if grams_per_skein:
                    break

            if not grams_per_skein:  # (fix this with a new function?)
                continue
            
            while True:
                price_per_skein = get_price_per_skein()
                if is_empty(price_per_skein):
                    price_per_skein = None
                    break

                price_per_skein = is_valid_float(price_per_skein)
                if price_per_skein:
                    break

            if not price_per_skein:  # (fix this with a new function?)
                continue

            while True:
                number_of_skeins = get_number_of_skeins()
                if is_empty(number_of_skeins):
                    price_per_skein = None
                    break

                number_of_skeins = is_valid_int(number_of_skeins)
                if number_of_skeins:
                    break

            if not price_per_skein:  # (fix this with a new function?)
                continue
            
            projects.append(project_name)

            project_yarn_amount = calculate_project_yarn_amount(grams_per_skein, number_of_skeins)

            project_yarn_price = calculate_project_yarn_price(price_per_skein, number_of_skeins)

            total_yarn_amount += project_yarn_amount

            total_yarn_price += project_yarn_price

            show_result(project_name, project_yarn_amount, yarn_name, project_yarn_price)

        # List all projects workflow
        elif main_menu_selection == "list all projects":
            show_list_of_projects(projects)
            print()
            show_number_of_projects(projects)
            show_total_yarn_usage(total_yarn_amount)
            show_total_yarn_price(total_yarn_price)

main()