class Symbol:
    """
    This is the place where all the card icon and the color tyoe are seprate.
    """
    
    def __init__(self, color, icon):
        
        self.color = "color"
        self.icon = "icon"


class Card(Symbol):
    """
    This is the class where the card are placed with its icon type
    """
    def __init__(self, values, icon):
        self.values = values
        self.icon = icon
        
        
    def __repr__(self):
        return '<{} {}>'.format(self.values, self.icon)
