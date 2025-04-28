'''
Builds class
'''
import json
from colorama import init, Fore, Style
from cards.perk_cards import PerkCard

# Initialize colorama
init(autoreset=True)

class Build:
    '''
    Represents a Build in Fallout 76, containing Normal and Legendary PerkCards.
    '''
    def __init__(self, name):
        '''
        Initialize a build instance.

        Args:
            name (str): The name of the build (e.g., "Bloodied Build", "Merchant Build").
        '''
        self.name = name
        self.normal_perk_cards = []  # List of normal PerkCards
        self.legendary_perk_cards = []  # List of legendary PerkCards
        self.special_points = {letter: 0 for letter in "SPECIAL"}  # Dictionary for S.P.E.C.I.A.L.

    def add_normal_card(self, card):
        '''
        Add a normal PerkCard to the build and update SPECIAL points.

        Args:
            card (PerkCard): The normal perk card to add.
        '''
        self.normal_perk_cards.append(card)
        if card.special:
            special_letter = card.special[0].upper()
            if special_letter in self.special_points:
                self.special_points[special_letter] += card.stars

    def add_legendary_card(self, card):
        '''
        Add a legendary PerkCard to the build.

        Args:
            card (PerkCard): The legendary PerkCard to add.
        '''
        self.legendary_perk_cards.append(card)

    def print_build_summary(self):
        '''
        Print a summary of the Build details.
        '''
        print(f"\nBuild Name: {self.name}")

        print("\nSPECIAL Points:")

        color_map = {
            'S': Fore.RED,
            'P': Fore.CYAN,
            'E': Fore.GREEN,
            'C': Fore.MAGENTA,
            'I': Fore.YELLOW,
            'A': Fore.WHITE,
            'L': Fore.LIGHTMAGENTA_EX
        }

        special_to_cards = {letter: [] for letter in "SPECIAL"}

        for card in self.normal_perk_cards:
            if card.special and card.special[0].upper() in special_to_cards:
                special_letter = card.special[0].upper()
                special_to_cards[special_letter].append(card)

        for special in "SPECIAL":
            color = color_map.get(special, Fore.WHITE)
            points = self.special_points.get(special, 0)
            print(f"  {color}{special}: {points}{Style.RESET_ALL}")

            for card in special_to_cards[special]:
                print(f"    {color}({card.stars}) {card.name}{Style.RESET_ALL}")

        print("\nLegendary Perk Cards:")
        if self.legendary_perk_cards:
            for card in self.legendary_perk_cards:
                print(f"  - {card.name} ({card.stars} stars)")
        else:
            print("  (None)")

    def save_to_file(self, filepath):
        '''
        Save the Build to a JSON file.

        Args:
            filepath (str): Path to the file to save.
        '''
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(
                {
                    'name': self.name,
                    'normal_perk_cards': [
                        {
                            'name': card.name,
                            'stars': card.stars,
                            'special': card.special
                        } for card in self.normal_perk_cards
                    ],
                    'legendary_perk_cards': [
                        {
                            'name': card.name,
                            'stars': card.stars,
                            'special': card.special
                        } for card in self.legendary_perk_cards
                    ],
                    'special_points': self.special_points
                },
                f,
                indent=4
            )

    @classmethod
    def load_from_file(cls, filepath):
        '''
        Load a Build from a JSON file.

        Args:
            filepath (str): Path to the file to load.

        Returns:
            Build: The loaded Build instance.
        '''
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        build = cls(name=data['name'])

        for card_data in data.get('normal_perk_cards', []):
            card = PerkCard(
                name=card_data['name'],
                stars=card_data['stars'],
                card_type='normal',
                special=card_data.get('special')
            )
            build.add_normal_card(card)

        for card_data in data.get('legendary_perk_cards', []):
            card = PerkCard(
                name=card_data['name'],
                stars=card_data['stars'],
                card_type='legendary',
                special=card_data.get('special')
            )
            build.add_legendary_card(card)

        build.special_points = data.get('special_points', {})
        return build
