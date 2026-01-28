
import getpass

print("----------------------")
print("   Seja bem vindo     ")
print("----------------------")
print("Pedra vence a Tesoura")
print("Tesoura vence o Papel")
print("Papel vence a Pedra\n  ")

placar_p1 = 0
placar_p2 = 0
placar_empate = 0

jogadas = ['pedra', 'papel', 'tesoura']

vence = {
      
          "pedra"  :    "tesoura",
          "tesoura":    "papel",
          "papel"  :    "pedra"

}

while True:

  player_1 = getpass.getpass(f'Jogador 1: {jogadas[0]}, {jogadas[1]} ou {jogadas[2]}' ).lower().strip()
  player_2 = getpass.getpass(f'Jogador 2: {jogadas[0]}, {jogadas[1]} ou {jogadas[2]}' ).lower().strip()

  if player_1 and player_2 in jogadas:

    if player_1 == player_2:

      print('Empate')
      placar_empate += 1

    elif vence[player_1] ==player_2:

      print("----------------")
      print('Jogador 1 venceu')
      print("----------------")
      placar_p1 += 1 

    else:
      print("----------------") 
      print('Jogador 2 venceu')
      print("----------------")
      placar_p2 += 1

    print('Jogador 1:', player_1, '\nJogador 2:', player_2)

  else: 
    print('Alguém digitou uma opção que não existe')   

  continuar = input("Jogar novamente: Digite qualquer tecla \nEncerrar: 0\n")

  if continuar ==  '0':

    print("------ JOGO ENCERRADO ------")
    print(f'      Placar final:         \n Jogador 1: {placar_p1} \n Jogador 2: {placar_p2}\n Empate: {placar_empate}')

    break

