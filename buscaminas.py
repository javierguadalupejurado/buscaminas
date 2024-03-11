import random

class Buscaminas:
    def __init__(self, filas, columnas, bombas):
        """
        Constructor de la clase Buscaminas.
        Inicializa el tablero y coloca las bombas.
        """
        self.filas = filas
        self.columnas = columnas
        self.bombas = bombas
        self.tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]
        self.colocar_bombas()

    def colocar_bombas(self):
        """
        Coloca aleatoriamente las bombas en el tablero.
        """
        bombas_colocadas = 0
        while bombas_colocadas < self.bombas:
            fila, columna = random.randint(0, self.filas - 1), random.randint(0, self.columnas - 1)

            if self.tablero[fila][columna] != '*':
                self.tablero[fila][columna] = '*'
                bombas_colocadas += 1

    def mostrar_tablero(self):
        """
        Muestra el tablero actual.
        """
        print("\n".join(" ".join(str(celda) for celda in fila) for fila in self.tablero))

    def jugar(self):
        """
        Inicia el juego y maneja la interacción con el jugador.
        """
        while True:
            self.mostrar_tablero()
            fila, columna = map(int, input("Ingrese fila y columna (separados por espacio): ").split())

            if not (0 <= fila < self.filas) or not (0 <= columna < self.columnas):
                print("Coordenadas fuera de rango. Inténtalo de nuevo.")
                continue

            if self.tablero[fila][columna] == '*':
                print("¡Has perdido! Bomba encontrada.")
                self.mostrar_tablero()
                break
            else:
                self.revelar_celda(fila, columna)

            if self.juego_ganado():
                print("¡Felicidades! Has ganado.")
                self.mostrar_tablero()
                break

    def revelar_celda(self, fila, columna):
        """
        Revela el contenido de una celda y muestra el número de bombas adyacentes.
        """
        if self.tablero[fila][columna] == ' ':
            bombas_adyacentes = sum(1 for i in range(fila-1, fila+2) for j in range(columna-1, columna+2) if
                                    0 <= i < self.filas and 0 <= j < self.columnas and self.tablero[i][j] == '*')
            self.tablero[fila][columna] = bombas_adyacentes if bombas_adyacentes > 0 else '-'

    def juego_ganado(self):
        """
        Verifica si todas las celdas seguras han sido reveladas.
        """
        for fila in self.tablero:
            for celda in fila:
                if celda == ' ':
                    return False
        return True

if __name__ == "__main__":
    filas, columnas, bombas = map(int, input("Ingrese filas, columnas y bombas (separados por espacio): ").split())
    juego = Buscaminas(filas, columnas, bombas)
    juego.jugar()