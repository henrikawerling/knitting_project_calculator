"""Main entry point for the Knitting Project Calculator.

This module controls program flow, menu navigation, and user interaction.
"""

import sys
from functions import *  # (PEP 8 violation -> import functions -> functions.function_to_call())

def main():
    """Run the main program loop."""
    print_welcome_msg()

    while True:
        print_main_menu()
        selection_raw = get_user_input()  # (-> variable name: main_menu_selection?)

        if is_empty(selection_raw):
            sys.exit(print_farewell_msg())

        selection = is_valid_selection(selection_raw)
        if not selection:
            print_invalid_input_msg()
            continue
        
        # Add new project workflow
        if selection == "add new project":
            project_name = get_project_name()
            if is_empty(project_name):
                continue
            
            yarn_name = get_yarn_name()
            if is_empty(yarn_name):
                continue
            
            while True:
                skein_weight_raw = get_skein_weight()
                if is_empty(skein_weight_raw):
                    skein_weight = None
                    break

                skein_weight = is_valid_int(skein_weight_raw)
                if skein_weight:
                    break

            if not skein_weight:  # (fix this with a new function?)
                continue
            
            while True:
                skein_price_raw = get_skein_price()
                if is_empty(skein_price_raw):
                    skein_price = None
                    break

                skein_price = is_valid_float(skein_price_raw)
                if skein_price:
                    break

            if not skein_price:  # (fix this with a new function?)
                continue

            while True:
                skein_amount_raw = get_skein_amount()
                if is_empty(skein_amount_raw):
                    skein_price = None
                    break

                skein_amount = is_valid_int(skein_amount_raw)
                if skein_amount:
                    break

            if not skein_price:  # (fix this with a new function?)
                continue

            total_yarn_amount = calculate_total_yarn_amount(skein_weight, skein_amount)

            total_yarn_price = calculate_total_yarn_price(skein_price, skein_amount)

            show_result(project_name, total_yarn_amount, yarn_name, total_yarn_price)

        # List all projects (not yet implemented)
        elif selection == "list all projects":
            print_not_available_msg()

main()