class Tree:
    def __init__(self, name):
        self.name = name
        self.children = []
    def add_children (self, child):
        self.children.append(child)
        
