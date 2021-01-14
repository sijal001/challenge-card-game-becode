class Symbol:
    
    def __init__(self, color, icon):
        
        self.color = "color"
        self.icon = "icon"


class Card(Symbol):
    
    def __init__(self, values, icon):
        self.values = values
        self.icon = icon
        
        
    def __repr__(self):
        return '<{} {}>'.format(self.values, self.icon)
