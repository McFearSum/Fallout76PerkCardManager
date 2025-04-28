'''
Perk Card class
'''

class PerkCard:
    '''
    Represents a Perk Card in Fallout 76, either normal or legendary
    '''
    def __init__(self,name,stars,card_type,special=None,builds=None):
        '''
        Initialize a PerkCard instance.

        Args:
            name (str):     Name of the perk card.
            stars (int):    Number of stars (1-5 normal, 1-4 legendary).
            card_type(str): "normal" or "legendary".
            special (str, optional): S.P.E.C.I.A.L attribute associated. Defaults to None.
            builds (set, optional): Set of build name using this card. Defaults to empty set
        '''
        self.name = name
        self.stars = stars
        self.card_type = card_type
        self.special = special
        self.builds = builds if builds is not None else set()

    def __str__(self):
        '''
        Return a formatted string representing the PerkCard.
        '''

        return (
            f"Perk Card Name: {self.name}\n"
            f"Stars: {self.stars}\n"
            f"Type: {self.card_type}\n"
            f"SPECIAL: {self.special}\n"
            f"Used in Builds {', '.join(self.builds) if self.builds else 'None'}\n"
        )
