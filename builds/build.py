"""
builds class
"""
import json
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

class Build:
    """
    Represents a Build in Fallout 76, containing Normal and Legendary PerkCards. 
    """
    def __init__(self, name):
        """
        Initialize a build instance.

        Args:
            name (str): The name of the build (e.g., "Bloodied Build", "Merchant Build").
        """
        self.name = name
        self.normal_perk_cards = []  # List of normal PerkCards
        self.legendary_perk_cards = []  # List of legendary PerkCards
        self.special_points = {letter: 0 for letter in "SPECIAL"}  # Dictionary S.P.E.C.I.A.L


    def add_normal_card(self, card):
        """
        Add a normal PerkCard to the build and update SPECIAL points.

        Args:
            card (PerkCard): The normal perk card to add.
        """
        self.normal_perk_cards.append(card)
        if card.special:
            # Get first letter of SPECIAL attribute (e.g., Perception -> P)
            special_letter = card.special[0].upper()
            self.special_points[special_letter] += card.stars


    def add_legendary_card(self, card):
        """
        Add a legendary PerkCard to the build.

        Args:
            card (PerkCard): The legendary PerkCard to add.
        """
        self.legendary_perk_cards.append(card)


    def print_build_summary(self):
        """
        Print a summary of the build, its cards, and SPECIAL points.
        """
        print(f"\nBuild Name: {self.name}")

        print("\nNormal Perk Cards:")
        if self.normal_perk_cards:
            for card in self.normal_perk_cards:
                print(f"  - {card.name} ({card.stars} stars)")
        else:
            print("  (None)")

        print("\nLegendary Perk Cards:")
        if self.legendary_perk_cards:
            for card in self.legendary_perk_cards:
                print(f"  - {card.name} ({card.stars} stars)")
        else:
            print("  (None)")

        print("\nSPECIAL Points:")
        print(f"  {Fore.RED}S: {self.special_points['S']}{Style.RESET_ALL}")
        print(f"  {Fore.CYAN}P: {self.special_points['P']}{Style.RESET_ALL}")
        print(f"  {Fore.GREEN}E: {self.special_points['E']}{Style.RESET_ALL}")
        print(f"  {Fore.MAGENTA}C: {self.special_points['C']}{Style.RESET_ALL}")
        print(f"  {Fore.YELLOW}I: {self.special_points['I']}{Style.RESET_ALL}")
        print(f"  {Fore.WHITE}A: {self.special_points['A']}{Style.RESET_ALL}")
        print(f"  {Fore.LIGHTMAGENTA_EX}L: {self.special_points['L']}{Style.RESET_ALL}")


    def save_to_file(self, filepath):
        """
        Save the Build to a JSON file.

        Args:
            filepath (str): Path to the file to save.
        """
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump({
                'name': self.name,
                'normal_perk_cards': [(card.name, card.stars) for card in self.normal_perk_cards],
                'legendary_perk_cards': [(card.name, card.stars) for card in self.legendary_perk_cards],
                'special_points': self.special_points
            }, f, indent=4)

    @classmethod
    def load_from_file(cls, filepath):
        """
        Load a Build from a JSON file.

        Args:
            filepath (str): Path to the file to load.

        Returns:
            Build: The loaded Build instance.
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"No such file: {filepath}")

        from cards.perk_cards import PerkCard  # Import here to avoid circular import
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        build = cls(name=data['name'])

        for name, stars in data['normal_perk_cards']:
            card = PerkCard(name=name, stars=stars, card_type="normal")
            build.normal_perk_cards.append(card)

        for name, stars in data['legendary_perk_cards']:
            card = PerkCard(name=name, stars=stars, card_type="legendary")
            build.legendary_perk_cards.append(card)

        build.special_points = data['special_points']

        return build


