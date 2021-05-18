import random
import time

# Initial Steps to invite in the game:
print("\nBem-vindo ao jogo!\n")
name = input("Escreva seu nome: ")
print("Olá " + name + "! Boa sorte!")
time.sleep(2)
print("O jogo vai começar!\n Vamos jogar!")
time.sleep(3)


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["Janeiro", "borda", "imagem", "filme", "promeça", "criança", "pulmão", "boneca", "rima", "dano",
                      "plantas"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
