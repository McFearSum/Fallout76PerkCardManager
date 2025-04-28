'''
Main entry point for the Fallout 76 Perk Manager project.
Handles initialization and user interaction loop.
'''

from builds.build import Build
from cards.perk_cards import PerkCard
from decks.deck import Deck


def show_main_menu():
    '''
    Display the main menu options.
    '''
    print("=" * 50)
    print(" Fallout 76 Perk Manager ".center(50, "="))
    print("=" * 50)
    print("\nWelcome, Vault Dweller!\n")
    print("What would you like to do?")
    print("\n1. Create New Deck")
    print("2. Load Existing Deck")
    print("3. Create New Build")
    print("4. Load Existing Build")
    print("5. Exit")


def create_new_build():
    '''
    Create a new Build interactively.
    '''
    build_name = input("\nEnter name for new Build: ").strip()

    build = Build(name=build_name)

    print(f"\nBuild '{build_name}' created successfully!")

    while True:
        add_card = input(
            "\nWould you like to add a Normal PerkCard to the Build now? (y/n): "
        ).strip().lower()

        if add_card == 'y':
            card_name = input("Enter PerkCard name: ").strip()

            try:
                stars = int(input("Enter number of stars (1-5): ").strip())
                if stars < 1 or stars > 5:
                    print("Invalid stars. Must be between 1 and 5.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            special = input("Enter SPECIAL category (S/P/E/C/I/A/L): ").strip().upper()
            if special not in "SPECIAL":
                print("Invalid SPECIAL category. Must be one of S, P, E, C, I, A, L.")
                continue

            perk_card = PerkCard(
                name=card_name,
                stars=stars,
                card_type="normal",
                special=special
            )
            build.add_normal_card(perk_card)
            print(f"Added {stars}-star '{card_name}' ({special}) to the Build.")
        elif add_card == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


    save = input("\nWould you like to save this Build to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = f"data/{build_name.lower().replace(' ', '_')}_build.json"
        build.save_to_file(filename)
        print(f"\nBuild saved to {filename}")
    else:
        print("\nBuild was not saved.")


def create_new_deck():
    '''
    Create a new Deck interactively.
    '''
    deck_name = input("\nEnter name for new Deck: ").strip()

    # We assume deck_type is normal for now
    deck = Deck(deck_type="normal")

    print(f"\nDeck '{deck_name}' created successfully!")

    while True:
        add_card = input("\nWould you like to add a PerkCard now? (y/n): ").strip().lower()
        if add_card == 'y':
            card_name = input("Enter PerkCard name: ").strip()
            try:
                stars = int(input("Enter number of stars (1-5): ").strip())
                if stars < 1 or stars > 5:
                    print("Invalid stars. Must be between 1 and 5.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            deck.add_card(card_name, stars)
            print(f"Added {stars}-star '{card_name}' to the Deck.")
        elif add_card == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    save = input("\nWould you like to save this Deck to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = f"data/{deck_name.lower().replace(' ', '_')}_deck.json"
        deck.save_to_file(filename)
        print(f"\nDeck saved to {filename}")
    else:
        print("\nDeck was not saved.")


def load_build():
    """
    Loads a build from filename (without .json).
    """
    filename = input("\nEnter the build filename to load (without .json): ").strip()
    filepath = f"data/{filename.lower().replace(' ', '_')}_build.json"

    try:
        build = Build.load_from_file(filepath)
        print(f"\nBuild '{filename}' loaded successfully!")
        build.print_build_summary()
    except FileNotFoundError:
        print(f"\nError: Build file '{filepath}' not found.")
    except Exception as e:
        print(f"\nUnexpected error occurred: {e.__class__.__name__}: {e}")


def load_deck():
    """
    Loads a deck from filename (without .json)
    """
    filename = input("\nEnter the deck filename to load (without .json): ").strip()
    filepath = f"data/{filename.lower().replace(' ', '_')}_deck.json"

    try:
        deck = Deck.load_from_file(filepath)
        print(f"\nDeck '{filename}' loaded successfully!")
        deck.print_deck()
    except FileNotFoundError:
        print(f"\nError: Deck file '{filepath}' not found.")
    except Exception as e:
        print(f"\nUnexpected error occurred: {e.__class__.__name__}: {e}")


def main():
    '''
    Main program loop.
    '''
    while True:
        show_main_menu()
        choice = input("\nEnter choice (1-5): ").strip()

        if choice == '1':
            create_new_deck()
        elif choice == '2':
            load_deck()
        elif choice == '3':
            create_new_build()
        elif choice == '4':
            load_build()
        elif choice == '5':
            print("\nExiting Fallout 76 Perk Manager. See you next time, Vault Dweller!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")



if __name__ == "__main__":
    main()
