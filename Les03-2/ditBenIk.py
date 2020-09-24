import time
from datetime import datetime

def mijnprogramma():

    # ALLE VRAGEN STAAN HIER MET VARIABELEN
    vraag1 = "1. Hoe nieuw ben ik bij het MA?\n\nA. Helemaal nieuw\nB. Ik kwam van een andere opleiding\nC. Ik heb het jaar over gedaan\n\n"
    vraag2 = "2. Welk van deze is wél mijn hobby?\n\nA. Paardrijden\nB. Tekenen\nC. Animaties maken\n\n"
    vraag3 = "3. Welke game speel ik het meest?\n\nA. Ark: Survival Evolved\nB. Minecraft\nC. Resident Evil 7\n\n"

    #datum en tijd
    datumentijd = datetime.now()

    #intro van het programma
    print('\n\nHello You!, Welkom bij de quiz over mezelf!')
    naam = input('\nWat is je naam?\n')

    print("Hallo",naam,"! Hier is de eerste vraag:\n")

    print(vraag1)

    def vraag1Juist():

        antwVraag1 = input()
        if antwVraag1 == "a" or antwVraag1 == "b" or antwVraag1 == "A" or antwVraag1 == "B":
            print('Het juiste antwoord was C, ik heb het jaar over gedaan.\n')
            print(vraag2)
        elif antwVraag1 == "c" or antwVraag1 == "C":
            print('Correct! Ik heb het jaar over gedaan.\n')
            print(vraag2)
        else:
            print('Invoer ongeldig! Vul A, B of C in.')
            vraag1Juist()
    vraag1Juist()

    def vraag2Juist():

        antwVraag2 = input()
        if antwVraag2 == "a" or antwVraag2 == "c" or antwVraag2 == "A" or antwVraag2 == "C":
            print('Het juiste antwoord was B, een van mijn favoriete hobbys is tekenen.\n')
            print(vraag3)
        elif antwVraag2 == "b" or antwVraag2 == "B":
            print('Correct! Een van mijn favoriete hobbys is tekenen.\n')
            print(vraag3)
        else:
            print('Invoer ongeldig! Vul A, B of C in.')
            vraag2Juist()
    vraag2Juist()

    def vraag3Juist():

        antwVraag3 = input()
        if antwVraag3 == "b" or antwVraag3 == "c" or antwVraag3 == "B" or antwVraag3 == "C":
            print('Het juiste antwoord was A, Ark is met 2700+ uur mijn meest gespeelde game.\n')
        elif antwVraag3 == "a" or antwVraag3 == "A":
            print('Correct! Ark is met 2700+ uur mijn meest gespeelde game.\n')
        else:
            print('Invoer ongeldig! Vul A, B of C in.')
            vraag3Juist()
    vraag3Juist()

    print('Wil je de quiz opnieuw doen? Type Y voor ja of N voor nee\n')

    def herstarten():
        restart = input()
        if restart == "y" or restart == "Y":
            time.sleep(1.5)
            print('\nAan het herstarten...')
            time.sleep(1.5)
            mijnprogramma()
        elif restart == "n" or restart == "N":
            time.sleep(1.5)
            print('\nDoei!\n')
        else:
            print('Ongeldige invoer, type Y voor ja of N voor nee\n')
            herstarten()
    herstarten()

mijnprogramma()
