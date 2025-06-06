import os
import time
os.system("cls || clear")
from dataclasses import dataclass

@dataclass
class Biblioteca: # classe.
    livro: str
    autor: str
    data_publicado: str
    tema: str
    
    def mostrar_dados(self): # mostra os dados do livro.
        print(f"Nome do Livro: {self.livro}")
        print(f"Nome do Autor: {self.autor}")
        print(f"Data públicada do livro: {self.data_publicado}")
        print(f"Tema do livro: {self.tema}")

def cadastrar_livro(lista): # cadastra os livros.
    print("|/| Biblioteca |/|\n")
    biblioteca = Biblioteca(
        livro = input("Digite o nome do livro desejado: "),
        autor = input("Digite o nome do autor do livro: "),
        data_publicado = input("Digite a data que o livro foi publicado: "),
        tema = input("Digite o tema do livro: ")
    )
    lista.append(biblioteca)
    
def verificar_lista_vazia(lista): # verificando se a lista está vazia.
    if not lista:
        print("A lista está vazia.")
        return True
    return False

def mostrar_livros(lista): # mostra apenas os a variável dos livros.
    if verificar_lista_vazia(lista):
        return
    print("Lista de Livros\n")
    for livro in lista:
        print(f"- {livro.livro}")
       
def buscar_livro(lista): # procura o livro por meio de uma lista.
    if verificar_lista_vazia(lista):
        return
    buscar_livro = input("Digite o nome do livro que deseja buscar: ") # digita o nome do livro que aparece na lista.
    for biblioteca in lista:
        if biblioteca.livro == buscar_livro:
            os.system("cls || clear")
            print("Livro encontrado!\n")
            biblioteca.mostrar_dados() # mostra todos os dados do livro.
            print()
            return
        os.system("cls || clear")
        print("Livro não encontrado")

def devolver_livro(lista): # função que devolve o livro.
    if verificar_lista_vazia(lista): # verifica se a lista está vazia.
        return

    mostrar_livros(lista) # mostra todos os livros da lista.

    devolv_livro = input("Digite o nome do livro que deseja devolver: ")
    for livro in lista:
        if livro.livro == devolv_livro: # devolve o livro que deseja.
            lista.remove(livro)
        os.system("cls || clear")
        print(f"O livro {devolv_livro} foi devolvido com sucesso!")
        return
    print(f"O livro com o nome ({devolv_livro}) não foi encontrado.")

lista = [] # lista

while True: # repete o menu.
    os.system("cls || clear")
    print("""
 1- Cadastrar livro
 2- Mostrar livros
 3- Buscar livro
 4- Devolver livro
 5- Sair
          """)

    opcao = int(input("Digite uma das opções acima: ")) # opção para escolher no menu.

    match opcao: # match case para o menu funcionar corretamente.
        case 1:
            os.system("cls || clear")
            cadastrar_livro(lista)
            input("\nPressione Enter para continuar...\n")
        case 2:
            os.system("cls || clear")
            mostrar_livros(lista)
            input("\nPressione Enter para continuar...\n")
        case 3:
            os.system("cls || clear")
            buscar_livro(lista)
            input("\nPressione Enter para continuar...\n")
        case 4:
            os.system("cls || clear")
            devolver_livro(lista)
            input("\nPressione Enter para continuar...\n")
        case 5:
            os.system("cls || clear")
            print("Saindo...")
            time.sleep(3) # temporizador de 3 segundos pra dar um charme.
            break
        case _:
            print("Opção Inválida, Tente novamente.")