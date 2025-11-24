class Cola:
    def __init__(self):
        self.datos = []  # aquí guardamos los elementos de la cola

    def encolar(self, x):
        # Agrega un elemento al FINAL de la cola
        self.datos.append(x)

    def desencolar(self):
        # Saca y devuelve el PRIMER elemento de la cola
        if self.esta_vacia():
            return None   # o podrías lanzar un error
        return self.datos.pop(0)

    def esta_vacia(self):
        return len(self.datos) == 0

    def ver_primero(self):
        if self.esta_vacia():
            return None
        return self.datos[0]


def main():
    # Imaginemos una cola en la caja de un supermercado
    cola = Cola()

    # Llegan clientes a la fila
    cola.encolar("Cliente A")
    cola.encolar("Cliente B")
    cola.encolar("Cliente C")

    print("Estado inicial de la cola:", cola.datos)

    # Atendemos al primer cliente
    atendido = cola.desencolar()
    print("Atendiendo a:", atendido)
    print("Cola ahora:", cola.datos)

    # Llega otro cliente
    cola.encolar("Cliente D")
    print("Llega Cliente D")
    print("Cola ahora:", cola.datos)

    # Atendemos dos más
    atendido = cola.desencolar()
    print("Atendiendo a:", atendido)
    print("Cola ahora:", cola.datos)

    atendido = cola.desencolar()
    print("Atendiendo a:", atendido)
    print("Cola ahora:", cola.datos)

    # ¿Quién queda al frente?
    print("Primero en la cola ahora:", cola.ver_primero())


if __name__ == "__main__":
    main()