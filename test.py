from fila import Queue

class Test:
    if __name__ == '__main__':
        fila = Queue()

        fila.push(22)
        fila.push(60)
        fila.push(True)
        fila.push('Juliano')
        fila.push('Queiroz')
        fila.push(100)
        print(fila)
        fila.pop()
        print(fila)
        fila.peek()
        
        
        
       