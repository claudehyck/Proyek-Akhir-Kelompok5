class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class ItinerarySLL: #Singly Linked List
    def __init__(self):
        self.head = None
    def add(self, data):
        new_node = Node(data)
        if not self.head: 
            self.head = new_node
        else:
            curr = self.head
            while curr.next: curr = curr.next
            curr.next = new_node
    def display(self):
        curr, res = self.head, []
        while curr:
            res.append(curr.data)
            curr = curr.next
        return " -> ".join(res) if res else "Kosong"


class PhotoDLL:# Double Linked List - Galeri Foto 
    def __init__(self):
        self.head = None
        self.current = None
    def add(self, img):
        new_node = Node(img)
        if not self.head: self.head = new_node
        else:
            curr = self.head
            while curr.next: curr = curr.next
            curr.next = new_node
            new_node.prev = curr
        if self.current is None:
            self.current = self.head

class SlideshowCLL:# Circular Linked List - Slideshow Rekomendasi 
    def __init__(self):
        self.head = None
    def add(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            curr = self.head
            while curr.next != self.head: curr = curr.next
            curr.next = new_node
            new_node.next = self.head
