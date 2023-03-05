
**Autores:**  Monserrath Aguilar Driggs, Carlos Arguedas

**Nombre del proyecto:** BlackJack Game

---

## Descripción del proyecto

El proyecto consiste en un juego de blackjack. Cuenta con uno o dos jugadores, y el dealer que sería la computadora. 
Contiene las opciones de ingresar un usuario nuevo o seleccionar uno existente, ver las estadisticas del usuario seleccionado e iniciar un nuevo juego. Además, todos los datos del usuario como nombre, partidas ganadas y perdidas se almacenan en un archivo de texto.

## Diseño de la solución

Para comenzar con el proyecto se realizó el siguiente planeamiento de las funcionalidades del juego.
```
uno o dos jugadores, dealer (computadora)
deck 52, con AS valiendo 1/11, y JQK valiendo 10
DEALER:
debe tener una carta escondida (se debe guardar el valor de esta carta en una varibale)
el resto de cartas abiertas
debe saber pedir cartas o quedarse (si tiene menos de 16-17 pide)
PLAYER:
cartas abiertas
ESTADO PLAYER:
mostrar si sigue en juego, perdio o gano
ESTADO JUEGO:
en juego, terminado
MENU: opciones
-player:
	input de un usuario o elegir uno existente
-nuevo juego:
	inicia el juego con el player seleccionado
		reparte cartas
		players piden o se quedan
		dealer juega
-stats:
	estadisiticas del player seleccionado, de las ultimas 5 plays
-salir
ARCHIVOS:
stats de los players (ganadas - perdidas)
CLASES QUE HACER:
Card, Deck, Hand, Game
```

Se crearon 4 clases, que son las siguientes:
<ul>
<li><em><strong>Card</strong></em>, en donde se define que cada carta tiene un palo y un rango asociado.</li>
<li><em><strong>Deck</strong></em>, crea el mazo del juego, en esta clase se encuentran los valores de los palos y los rangos. Contiene funciones que trabajan para la creación del mazo, como deal() que resparte, y shuffle() que mezcla las cartas.</li>
<li><em><strong>Hand</strong></em>, la clase contiene los valores de las cartas. Cuenta con dos funciones, una que se encarga de agregar cartas a la mano de los jugadores o del Dealer, llamada add_card(). La otra, encargada de mostrar la mano de los jugadores o del Dealer, de este ultimo muestra una carta escondida cuando se le indica, llamada show_hand().</li>
<li><em><strong>Game</strong></em>, la ultima clase contiene la mayor parte de la logica del juego respecto a la creacion del mazo, repartir las cartas a la cantidad de jugadores ingresados. Esto lo logra invocando las funciones de las clases Deck y Hand. Tiene una función print_players_hands(), que imprime la mano de los jugador y del Dealer, llamando a la funcion show_hand(), de la clase Hand. Además, esta clase cuenta con funciones que indican el estado del jugador, si está en juego player_in_game(), si perdió player_loses() o si ganó player_wins().</li>
</ul>
Cada clase se encuentra en un archivo separado, llamado con el nombre de la respectiva clase: <em>Card.py</em>, <em>deck.py</em>, <em>Hand.py</em>, <em>Game.py</em>.

Se creó un archivo llamado <em>agregar_archivo.py</em>, en donde se hace el manejo de los archivos para guardar los datos de los jugadores. Contiene la función get_player() la cual agrega el jugador a un archivo, en un formato de lista. La función add_player_stats(), agrega las estadisticas con la fecha, nombre y resultado a un archivo. Y por ultimo la función print_stats(), que imprime las lineas del archivo donde se encuentran las estadísticas.

Por otro lado, se realizó un archivo llamado <em>funtions_game.py</em>, el cual contiene varias de las funciones necesarias para que se lleve acabo el juego. 
<ul>
<li>Funciones relacionadas a la seleccion de los jugadores como create_player(), que crea el jugador con el input ingresado por el usuario, llama a la función get_player() y lo guarda en el archivo. select_player(), muestra al usuario una lista de jugadores registrados y el usuario debe seleccionar el que desea utilizar, si no hay usuarios disponibles llama a la función anterior. handle_player_select(), pide al usuario elegir entre crear un nuevo jugador o seleccionar uno existente, según lo ingresado por el usuario invoca a las dos funciones anteriores.</li>
<li>Funciones relacionadas al estado de la partida. Imprimen si sigue en juego in_game(), o si el juego ha terminado game_over().</li>
<li>Función que muestra las estadisticas de un jugador, el usuario debe elegir el jugador de una lista.</li>
<li>Funciones relacionadas a pedir más cartas o quedarse. La función hit() agrega más cartas, invocando a la función add_card() y deal() para repartirlas. La función hit_stand() le pregunta al usuario si desea quedarse o pedir más cartas, si la opcion que elige el usuario es pedir más entonces invoca a la función anterior.</li>
</ul>

El archivo <em>main_game.py</em> continene la función principal que corre todo el juego de blackjack. En este archivo se deben importar los módulos de los demás archivos. Se define la función game(), la cual imprime un mensaje de bienvenida y muestra el menú de opciones, donde el usuario debe eligir cuál desea. En las respectivas opciones, que se mencionan más adelante en este documento, se invocan las diferentes funciones creadas anteriormente por medio de sus módulos.

Asimismo, se encuentran archivos de texto los cuales contienen los nombres de los jugadores ingresados, <em>players.txt</em>. Las estadísticas de todas las partidas, con fecha y el resultado (si el jugador ganó o perdió),<em>-stats.txt</em>. Y un archivo para cada jugador, con sus respectivas estadísticas, <em>nombre del jugador-stats.txt</em>. 


## Manual de usuario

El juego incia con un mensaje de bienvenida, seguido del menú donde el usuario puede eligir entre las opciones.

La <em>Opción 1</em> es sobre seleccionar el usuario. Se debe indicar la cantidad de jugadores, 1 o 2. Luego elige si agregar un nuevo jugador o seleccionar uno existente. 

En la <em>Opción 2</em> se inicia una nueva partida donde el usuario debe elegir ,según la mano de cartas, si se queda o pide más cartas. Esto hasta que pierda o gane.

La <em>Opción 3</em> muestra las estadísticas de un jugador. El usuario debe seleccionar un jugador de los existentes para poder ver las estadísticas del mismo.

Por último, la <em>Opción 4</em> es para salir del juego.


## Consideraciones especiales

Cualquier consideración o comentario adicional sobre la aplicación. Por ejemplo:

<ul>
<li>Como correr la aplicación</li>
<li>Cosas que no se lograron realizar</li>
<li>Siguientes pasos para mejorar la aplicación</li>
<li>Etc.</li>
</ul>
---

