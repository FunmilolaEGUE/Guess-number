from random import randint

def nombre(essais,limite):
    x = randint(0,limite)
    print("Vous devez trouver un nombre compris entre 0 et ",limite)
    print("Vous avez ",essais," essais")
    nbre = int(input())
    for i in range(1,essais):
        if nbre == x:
            print("Bravo")
            break
        if nbre < x:
            print("Trop petit")
            print("il vous reste", essais-i," essais")
        elif nbre>x:
            print("Trop grand")
            print("il vous reste", essais-i," essais")
        nbre = int(input())
    if nbre != x :
        print("Perdu")
        print("Le nombre à trouver était :",x)  


def jouer ():
    choices = 1
    while choices == 1 :
        print("Veuillez sélectionner le niveau de difficulté dans la liste ci-dessous")
        print("")
        print("1. Débutant")
        print("2. Intermédiaire")
        print("3. Senior")
        print("4. God Mode")
        choix =int(input("Niveau :"))
        if choix == 1 :
            print("Bienvenue dans le mode Débutant")
            print("Le nombre à chercher est compris entre 0 et 10")
            nombre(7,10)
        if choix == 2 :
            prin("Bienvenue dans le mode Intermédiaire")
            print("Le nombre à chercher est compris entre 0 et 100")
            nombre(5,100)
        if choix == 3 :
            print("Bienvenue dans le mode Débutant")
            print("Le nombre à chercher est compris entre 0 et 1000")
            nombre(3,1000)
        if choix == 4 :
            print("Bienvenue dans le GOD MODE")
            print("Le nombre à chercher est compris entre 0 et 10000")
            prix= int(input("Do you really want to do that man ? 1=yes"))
            if prix == 1 :
                nombre(1,10000)
            else :
                print("Good Choice bro")
        choices=int(input("Voulez vous recommencer ? 1=yes"))



def rules() :
    print("Les règles du jeu sont les suivantes :")
    print("...Vous devenez deviner en un certains nombre d'éssais le un nombre caché. ")
    print("...Ce nombre est tiré au hasard dans un intervalle.")
    print("...Cet intervalle est décrit au début de chaque niveau.")
    print("")
    menu()


def quitter():
    print("Bye Bye")

def menu():
    print("1.Jouer")
    print("2.Règles")
    print("3.Quitter")
    choice = int(input(":"))
    if choice == 1 :
        jouer()
    elif choice == 2 :
        rules()
    elif choice == 3 :
        quitter()
    else :
        menu()

#Mettre des exceptions pour les erreurs de type 
#Programme principal
print("")
print("")
print("Bienvenue dans le jeu DEVINE LE NOMBRE")
print("")
print("")
menu()
