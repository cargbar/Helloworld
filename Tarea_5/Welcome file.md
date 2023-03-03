
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
Card, Deck, Hand
```

Deben describir las clases que crearon y su funcionalidad, brevemente. También deben explicar brevemente la distribución de archivos de su programa (qué archivos hay y qué código va dentro de cada uno).

## Manual de usuario

El juego incia con un mensaje de bienvenida, seguido del menú donde el usuario puede eligir entre las opciones.

La <em>Opción 1</em> es sobre seleccionar el usuario. Se debe indicar la cantidad de jugadores, 1 o 2. Luego elige si agregar un nuevo jugador o seleccionar uno existente. 

En la <em>Opción 2</em> se inicia una nueva partida donde el usuario debe elegir ,según la mano de cartas, si se queda o pide más cartas. Esto hasta que pierda o gane.

La <em>Opción 3</em> muestra las estadisticas de un jugador. El usuario debe seleccionar un jugador de los existentes para poder ver las estadisticas del mismo.

Por último, la <em>Opción 4</em> es para salir del juego.


## Consideraciones especiales

Cualquier consideración o comentario adicional sobre la aplicación. Por ejemplo:

- Como correr la aplicación
- Cosas que no se lograron realizar
- Siguientes pasos para mejorar la aplicación
- Etc.

---

