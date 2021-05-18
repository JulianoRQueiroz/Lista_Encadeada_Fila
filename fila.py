import queue
from node import Node

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0 
          
    def push(self, element):
        """ Insere um elemento na pilha"""
        node = Node(element)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
            
        if self.first is None:
            self.first = node
            
        self._size = self._size + 1
            
    def pop(self):
        """ Removendo o elemento do topo da pilha"""
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            self._size = self._size - 1
            return elem
        
        raise IndexError('The queue is empty! ')
          
    def peek(self):
        """ Retorna o topo da pilha sem remoção"""
        if self._size > 0:
            elem = self.first.data
            return elem
        
        raise IndexError('The queue is empty! ')
          
    def __len__(self):
        """ Retorna o tamanho da lista"""
        return self._size
    
    def __repr__(self) -> str:
        if self._size > 0:
            r = ''
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + ' '
                pointer = pointer.next
            return r
        return 'Empty Que'
        
    def __str__(self) -> str:
        return self.__repr__()
    