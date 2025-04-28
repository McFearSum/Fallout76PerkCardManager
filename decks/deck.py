'''
Deck class to manage collections of PerkCards.
'''

import json
import os

class Deck:
    '''
    Represents a deck of PerkCards (normal or legendary)
    '''
    def __init__(self, deck_type='normal'):
        '''
        Initialize a Deck instance.

        Args:
            deck_type (str): 'normal' or 'legendary'. Defaults to 'normal'.
        '''
        self.deck_type = deck_type
        self.cards = {}  # key = (card_name, stars), value = quantity


    def add_card(self, card_name, stars=1):
        '''
        Add a card to the deck.

        Args:
            card_name (str): Name of the perk card.
            stars (int): Number of stars (defaults to 1)
        '''

        key = (card_name, stars)
        self.cards[key] = self.cards.get(key, 0) + 1


    def remove_card(self, card_name, stars=1):
        '''
        Remove a card from the deck.

        Args:
            card_name (str): Name of the perk card.
            stars (int): Number of stars.
        '''
        key = (card_name, stars)
        if self.cards.get(key,0) > 0:
            self.cards[key] -= 1
            if self.cards[key] == 0:
                del self.cards[key]
        else:
            raise ValueError(f"No {stars}-star {card_name} card to remove.")


    def find_card(self, card_name, stars):
        '''
        Find and return a card if it exists in the deck.

        Args:
            card_name (str): Name of the perk card.
            stars (int): Number of stars

        Returns:
            bool: True if found, False otherwise.
        '''

        return (card_name, stars) in self.cards


    def print_deck(self):
        """
        Pretty-print all cards currently in the deck.
        """
        if not self.cards:
            print("(Deck is empty.)")
            return

        print(f"\n{self.deck_type.capitalize()} Deck:")
        for (name, stars), qty in sorted(self.cards.items()):
            print(f"  - {qty}x {name} ({stars}-star)")


    def save_to_file(self, filepath):
        """
        Save the deck to a JSON file.

        Args:
            filepath (str): Path to the file to save.
        """
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump({
                'deck_type': self.deck_type,
                'cards': list(self.cards.items())
            }, f, indent=4)


    @classmethod
    def load_from_file(cls, filepath):
        """
        Load a deck from a JSON file.

        Args:
            filepath (str): Path to the file to load.

        Returns:
            Deck: The loaded Deck instance.
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"No such file: {filepath}")

        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        deck = cls(deck_type=data['deck_type'])
        deck.cards = {tuple(item[0]): item[1] for item in data['cards']}
        return deck
        