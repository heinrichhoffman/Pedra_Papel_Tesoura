
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

while True:

  jogadas1 = ['pedra', 'papel', 'tesoura']
  jogadas2 = ['pedra', 'papel', 'tesoura']


  player_1 = getpass.getpass(f'Jogador 1: {jogadas1[0]}, {jogadas1[1]} ou {jogadas1[2]}' ).lower().strip()
  player_2 = getpass.getpass(f'Jogador 2: {jogadas2[0]}, {jogadas2[1]} ou {jogadas2[2]}' ).lower().strip()




  vence = {

          "pedra"  :    "tesoura",
          "tesoura":    "papel",
          "papel"  :    "pedra"


  }


  if player_1 in jogadas1 and player_2 in jogadas2:

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

  continuar = input("Jogar novamente: 1\nEncerrar: 2\n")

  if continuar ==  '2':

    print("------ JOGO ENCERRADO ------")
    print(f'      Placar final:         \n Jogador 1: {placar_p1} \n Jogador 2: {placar_p2}')



    break
