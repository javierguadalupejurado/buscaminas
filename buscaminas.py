import pygame  # Importa la biblioteca pygame para crear la interfaz gráfica del juego
import random  # Importa la biblioteca random para generar números aleatorios

# Definición de colores usando tuplas RGB
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (192, 192, 192)
ROJO = (255, 0, 0)

# Dimensiones de la ventana y del tablero
ANCHO = 600
ALTO = 600
FILAS = 10
COLUMNAS = 10
TAMANO_CELDA = ANCHO // COLUMNAS  # Calcula el tamaño de cada celda del tablero

class Buscaminas:
    def _init_(self, bombas):
        """
        Constructor de la clase Buscaminas.
        Inicializa el tablero y coloca las bombas.
        """
        self.bombas = bombas  # Número de bombas en el tablero
        # Crea un tablero con dimensiones FILAS x COLUMNAS y lo llena con espacios en blanco
        self.tablero = [[' ' for _ in range(COLUMNAS)] for _ in range(FILAS)]
        # Crea una matriz de igual tamaño que el tablero para controlar qué bombas están ocultas
        self.bombas_ocultas = [[False for _ in range(COLUMNAS)] for _ in range(FILAS)]
        self.bombas_descubiertas = 0  # Contador de bombas descubiertas
        self.colocar_bombas()  # Coloca las bombas aleatoriamente en el tablero

    def colocar_bombas(self):
        """
        Coloca aleatoriamente las bombas en el tablero.
        """
        bombas_colocadas = 0
        while bombas_colocadas < self.bombas:  # Repite hasta colocar todas las bombas
            fila, columna = random.randint(0, FILAS - 1), random.randint(0, COLUMNAS - 1)
            # Verifica si la posición seleccionada no tiene ya una bomba colocada
            if self.tablero[fila][columna] != '*':
                # Coloca una bomba en la posición seleccionada
                self.tablero[fila][columna] = '*'
                bombas_colocadas += 1  # Incrementa el contador de bombas colocadas

    def contar_bombas_adyacentes(self, fila, columna):
        """
        Cuenta las bombas adyacentes a la celda especificada.
        """
        contador = 0
        # Itera sobre las celdas adyacentes a la celda especificada
        for i in range(max(0, fila - 1), min(FILAS, fila + 2)):
            for j in range(max(0, columna - 1), min(COLUMNAS, columna + 2)):
                # Si la celda es una bomba, se incrementa el contador
                if self.tablero[i][j] == '*':
                    contador += 1
        return contador

    def revelar_celda(self, fila, columna):
        """
        Revela el contenido de una celda.
        """
        if self.tablero[fila][columna] == ' ':
            # Cuenta las bombas adyacentes y actualiza la celda con el número de bombas encontradas
            bombas_adyacentes = self.contar_bombas_adyacentes(fila, columna)
            self.tablero[fila][columna] = bombas_adyacentes if bombas_adyacentes > 0 else '-'
            return True
        elif self.tablero[fila][columna] == '*' and not self.bombas_ocultas[fila][columna]:
            # Marca la bomba como descubierta y actualiza el contador de bombas descubiertas
            self.bombas_ocultas[fila][columna] = True
            self.bombas_descubiertas += 1
            # Si se han descubierto suficientes bombas, el juego termina y se pierde
            if self.bombas_descubiertas >= 6:
                return 'perdiste'
            return True
        return False

    def juego_ganado(self):
        """
        Verifica si todas las celdas seguras han sido reveladas.
        """
        for fila in self.tablero:
            for celda in fila:
                if celda == ' ':
                    return False
        return True

# Inicialización de Pygame
pygame.init()  # Inicializa pygame
ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea una ventana para el juego
pygame.display.set_caption('Buscaminas')  # Establece el título de la ventana

reloj = pygame.time.Clock()  # Crea un objeto para controlar la velocidad de fotogramas
buscaminas = Buscaminas(bombas=10)  # Crea una instancia de la clase Buscaminas con 10 bombas

# Función para dibujar el tablero
def dibujar_tablero():
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            celda = buscaminas.tablero[fila][columna]  # Obtiene el contenido de la celda
            rect = pygame.Rect(columna * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA)
            if buscaminas.bombas_ocultas[fila][columna]:
                # Dibuja un círculo rojo si la bomba está oculta
                pygame.draw.circle(ventana, ROJO, rect.center, TAMANO_CELDA // 4)
            else:
                # Dibuja un rectángulo gris para representar la celda del tablero
                pygame.draw.rect(ventana, GRIS, rect)
                pygame.draw.rect(ventana, NEGRO, rect, 1)  # Borde negro para cada celda
                if celda != ' ' and celda != '*':
                    # Dibuja el número de bombas adyacentes en la celda si es seguro
                    font = pygame.font.Font(None, 30)
                    text = font.render(str(celda), True, NEGRO)
                    ventana.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))

# Bucle principal del juego
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False  # Si el usuario cierra la ventana, se termina el bucle
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()  # Obtiene las coordenadas del clic del mouse
            fila = y // TAMANO_CELDA  # Calcula la fila del tablero según la posición del clic
            columna = x // TAMANO_CELDA  # Calcula la columna del tablero según la posición del clic
            resultado = buscaminas.revelar_celda(fila, columna)  # Intenta revelar la celda clicada
            if resultado == 'perdiste':
                print("¡Has perdido!")  # Si se han descubierto suficientes bombas, se muestra un mensaje de derrota
                jugando = False  # Se termina el juego
            elif buscaminas.juego_ganado():
                print("¡Felicidades! Has ganado.")  # Si se revelan todas las celdas seguras, se muestra un mensaje de victoria
                jugando = False  # Se termina el juego

    ventana.fill(BLANCO)  # Limpia la pantalla con el color blanco
    dibujar_tablero()  # Dibuja el tablero en la ventana
    pygame.display.flip()  # Actualiza la pantalla
    reloj.tick(30)  # Controla la velocidad de fotogramas a 30 FPS

pygame.quit()  # Cierra pygame al salir del bucle principal