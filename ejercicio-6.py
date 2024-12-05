"""
Pac-Man

1. Definir una función `eat_ghost()`, y recibirá dos parametros (si Pacman tiene el
poder activo y si pacman toco un fantasma), esta función deberá retornar si Pacman
puede comerse al fantasma.

eat_ghost(False, True)
False

2. Definir si Pacman puntuara este recibira dos parametros (si pacman ha tocado un poder
y si ha tocado un punto). Esta funcion debera retorna un booleano indicando si toco un
poder o un punto.

score(True, True)
True

3. Definir una funcion para cuando ha perdido, debera recibir dos parametros (si pacman
tiene el poder activo y otro para saber si toco un fantasma). Este deberá retornar un
boleano que retornara Verdadero si Pac-Man toco a un fantasma sin tener el poder activo.

lose(False, True)
True

4. Definir si Pac-Man ha ganado, esta funcion debera recibir 3 parametros (el primero
indicando si ya se comio todos los puntos, el segundo si tiene un poder activo y
el tercero si ha tocado un fantasma). La función debera retornar Verdadero si Pac-Man
ha consumido todos los puntos y no ha perdido basandonos en la funcion anterior.

win(False, True, False)
False
"""