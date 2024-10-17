print("BIENVENIDO AL JUEGO PIEDRA, PAPEL O TIJERA")
print("JUGADOR 1 INGRESA TU NOMBRE")
player1_name = input()
print("JUGADOR 2 INGRESA TU NOMBRE")
player2_name = input()

print(player1_name, " ingresa que eliges: ¿piedra, papel o tijera?")
player1_move = input().lower()
print(player2_name, " ingresa que eliges: ¿piedra, papel o tijera?")
player2_move = input().lower()

valid_moves = ["piedra", "papel", "tijera"]

if player1_move not in valid_moves or player2_move not in valid_moves:
    print("uno o ambos jugadores hicieron una elección ncorrecta, por favor, elijan piedra, papel o tijera")
else:
    if player1_move == player2_move:
        print("empate")
    elif(player1_move == "piedra" and player2_move == "tijera") or (player1_move == "tijera" and player2_move == "papel") or (player1_move == "papel" and player2_move == "piedra") :
        print("Gana: ", player1_name)
    else:
        print("Gana: ", player2_name)
