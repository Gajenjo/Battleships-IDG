# Battleships-IDG

# Hundir la Flota en Python


![Barco](https://upload.wikimedia.org/wikipedia/commons/5/5c/New_Jersey_Sails.jpg)

<br>

## **Introducción**
<br>

Bienvenido al juego clásico *"Hundir la Flota"!* En este juego de estrategia naval, tu objetivo es hundir la flota de tu oponente antes de que él hunda la tuya.

<br>
<br>

## **¿Cómo funciona el juego?**
<br>
El objetivo del juego es hundir la flota del oponente antes de que él hunda la tuya. Cada jugador coloca sus barcos en un tablero de juego, que es una cuadrícula de celdas. Los barcos pueden colocarse en cualquier posición, siempre y cuando no se superpongan y se mantengan dentro del tablero.

Hay dos jugadores: **tu y la maquina**

Un **tablero de 10 x 10** posiciones donde irán los barcos.

Lo primero que se hace es colocar los barcos. Para este juego los barcos se colocan de manera aleatoria. Ahora bien, puedes empezar colocando los barcos en unas posiciones fijas, que no cambien con cada partida, y después implementarlo aleatoriamente, ya que es más complejo. Los barcos son:
<br>
<br>

- 4 barcos de 1 posición de eslora
- 3 barcos de 2 posiciones de eslora
- 2 barcos de 3 posiciones de eslora
- 1 barco de 4 posiciones de eslora
<br>
<br>

Tanto tu, como la maquina tenéis un tablero con barcos, y se trata de ir "disparando" y hundiendo los del adversario hasta que un jugador se queda sin barcos, y por tanto, pierde.

Funciona por turnos y empiezas tu.

En cada turno disparas a una coordenada (X, Y) del tablero adversario. Si aciertas, te vuelve a tocar. En caso contrario, le toca a la maquina.

En los turnos de la maquina, si acierta, también le vuelve a tocar. ¿Dónde dispara la maquina? A un punto aleatorio en tu tablero.

Si se hunden todos los barcos de un jugador, el juego acaba y gana el otro.

<br>

## **¿Cómo se ejecuta el programa?**
<br>

Para ejecutar el programa, abre el archivo *main.py* en tu editor de Python preferido. Asegúrate de que todos los archivos necesarios estén en la misma carpeta.

Una vez que el programa esté abierto, sigue las instrucciones en pantalla para colocar tus barcos y jugar contra la computadora.

<br>


## **Funciones**
<br>
El programa utiliza las siguientes funciones:

<br>

- **Crear_tablero**: Crea un tablero de juego vacío de tamaño n x n.
- **mostrar_tablero**: Muestra el tablero de juego en la pantalla.
- **colocar_barco**: Coloca un barco en el tablero de juego.
- **atacar**: Realiza un ataque en el tablero de juego.
- **verificar_ataque**: Verifica si el ataque del jugador ha impactado en un barco enemigo.
- **verificar_victoria**: Verifica si un jugador ha hundido todos los barcos del oponente y ha ganado el juego.
- **jugar**: Controla el flujo del juego y las interacciones entre el jugador y la computadora.

<br>

## **Creadores del proyecto**
<br>
Este proyecto fue creado por: 

<br>

- Dustin
- Guillermo
- Ignacio
  














