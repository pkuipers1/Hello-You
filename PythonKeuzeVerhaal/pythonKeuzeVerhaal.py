import os
import time
import getpass
import sys
from datetime import date

# Dit is het keuzeverhaal over een Nieuwkomer  voor BWP.
# Het verhaal moet uit 21 stukjes bestaan.

# Mijn idee:
# Afhankelijk van de keuzes die je maakt, krijg je een bepaald aantal punten
# Erbij of eraf. Dit bepaald je volgende vragen en uiteindelijk je uitkomst.
# Alles staat in een text-based user interface, die steeds verandert dmv. CLS.

def pythonKeuzeVerhaal():

    # BASE INTERFACE DESIGN
    interfaceRow1 = "             ________________________________________________"
    interfaceRow2 = "            /                                                \ "
    interfaceRow3 = "           |    _________________________________________     |"
    interfaceRow4 = "           |   |                                         |    |"
    interfaceRowQuestion = "           |   |  Question #:                            |    |"
    interfaceRow6 = "           |   |                                         |    |"
    interfaceRowA = "           |   |  A.                                     |    |"
    interfaceRowB = "           |   |  B.                                     |    |"
    interfaceRowC = "           |   |  C.                                     |    |"
    interfaceRow10 = "           |   |                                         |    |"
    interfaceRow11 = "           |   |                                         |    |"
    interfaceRow12 = "           |   |                                         |    |"
    interfaceRow13 = "           |   |                                         |    |"
    interfaceRow14 = "           |   |                                         |    |"
    interfaceRow15 = "           |   |                                         |    |"
    interfaceRow16 = "           |   |_________________________________________|    |"
    interfaceRow17 = "           |                                                  |"
    interfaceRow18 = "            \_________________________________________________/"
    interfaceRow19 = "                   \___________________________________/"
    interfaceRow20 = "                ___________________________________________"
    interfaceRow21 = "             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_"
    interfaceRow22 = "          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_"
    interfaceRow23 = "       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_"
    interfaceRow24 = "    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_"
    interfaceRow25 = " _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_"
    interfaceRow26 = ":-------------------------------------------------------------------------:"
    interfaceRow27 = "`---._.-------------------------------------------------------------._.---'"

    # INTERFACE DESIGN LIST
    interfaceRows = [interfaceRow1, interfaceRow2, interfaceRow3, interfaceRow4, interfaceRowQuestion, interfaceRow6, interfaceRowA, interfaceRowB, interfaceRowC, interfaceRow10, interfaceRow11, interfaceRow12, interfaceRow13, interfaceRow14, interfaceRow15, interfaceRow16, interfaceRow17, interfaceRow18, interfaceRow19, interfaceRow20, interfaceRow21, interfaceRow22, interfaceRow23, interfaceRow24, interfaceRow25, interfaceRow26, interfaceRow27]

    dateToday = date.today()

    def wannaRestart():
        print("\n")
        restartText = "Do you want to restart? Y/N...\n\n"
        for l in restartText:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.05)

        restart2 = input()

        if (restart2 == "Y" or restart2 == "y"):
            pythonKeuzeVerhaal()
        elif (restart2 == "N" or restart2 == "n"):
            print("Goodbye!")
        else:
            print("\nInvalid input! Please type Y or N and press Enter.")
            wannaRestart()

    def clearRows():
        interfaceRows[2] = "           |    _________________________________________     |"
        interfaceRows[3] = "           |   |                                         |    |"
        interfaceRows[4] = "           |   |                                         |    |"
        interfaceRows[5] = "           |   |                                         |    |"
        interfaceRows[6] = "           |   |                                         |    |"
        interfaceRows[7] = "           |   |                                         |    |"
        interfaceRows[8] = "           |   |                                         |    |"
        interfaceRows[9] = "           |   |                                         |    |"
        interfaceRows[10] = "           |   |                                         |    |"
        interfaceRows[11] = "           |   |                                         |    |"
        interfaceRows[12] = "           |   |                                         |    |"
        interfaceRows[13] = "           |   |                                         |    |"
        interfaceRows[14] = "           |   |                                         |    |"
        interfaceRows[15] = "           |   |_________________________________________|    |"

    def ending5():
        os.system("cls")
        print("You are renting a house in the Netherlands, don't speak Dutch and have a low-income job.\nIs this really what you wanted?")

        wannaRestart()

    def ending4():
        os.system("cls")
        print("Congratz, you got the best ending. You live on a farm in the Netherlands,\nhave lots of opportunities like extra pets, or even starting your\nown business here in the future. Anyways,")
        wannaRestart()

    def ending3():
        os.system("cls")
        print("You are a housewife, have a husband in the Netherlands and financially an okay situation,\n albeit not enough to afford things like a house. Still, Congratz!")
        wannaRestart()

    def ending2():
        os.system("cls")
        print("Congratz, you've got a modern house and a job in the Netherlands. Pets aren't allowed here sadly, but perhaps you wanna give\nit another try. This is the end of your journey. Or perhaps a new beginning?")
        wannaRestart()

    def ending1():
        print("Congratz, you own a nice little apartment in Amsterdam and live a happy life in the Netherlands.")
        wannaRestart()

    def petHorses():
        os.system("cls")

        print("       _ ____")
        print("     /( ) _   \ ")
        print("    / //   /\` \,  ||--||--||-")
        print("      \|   |/  \|  ||--||--||-")
        print("~^~^~^~~^~~~^~~^^~^^^^^^^^^^^^")
        time.sleep(0.5)
        os.system("cls")
        print("       _ ____")
        print("     /( ) _    \ ")
        print("    / //   /\`  \,  ||--||--||-")
        print("      /\  ;  \  \|  ||--||--||-")
        print("~^~^~^~~^~~~^~~^^~^^^^^^^^^^^^")
        time.sleep(0.5)
        os.system("cls")
        print("       _ ____ _ ")
        print("     /( ) _   -^^\ ")
        print("    /  /.._/\` \./  ||--||--||-")
        print("      / \    \      ||--||--||-")
        print("~^~^~^~~^~~~^~~^^~^^^^^^^^^^^^")
        time.sleep(0.5)
        os.system("cls")
        print("                             ")
        print("              <^^               ")
        print("       _ ____< \ )               ")
        print("     /( ) _    )                ")
        print("    /  //   -  /     ||--||--||-")
        print("      | |   | |      ||--||--||-")
        print("~^~^~^~~^~~~^~~^^~^^^^^^^^^^^^")
        time.sleep(4)
        os.system("cls")
        print("YOU GOT HORSES!")
        time.sleep(3)
        os.system("cls")
        ending4()

    def petDog():

        os.system("cls")
        def runAnim():
            print("     _            ;~~,__")
            print("    | ^-.,-------'`-'._.'")
            print("     *-,,,  ,       ;'~~'")
            print("       ,'_,'~.__; '--.")
            print("      //'       ````(;")
            print("     `-'")
            time.sleep(0.3)
            os.system("cls")
            print("                .--~~,__")
            print("   :-....,-------`~~'._.'")
            print("    `-,,,  ,_      ;'~U'")
            print("     _,-' ,'`-__; '--.")
            print("    (_/'~~      ''''(")
            time.sleep(0.3)
            os.system("cls")
            print("     .--_        .--~~,__")
            print("      \  ^,-------`~~'._.'")
            print("       ^; ,'~.__;  ;"  )
            print("         ^, \`-__;,\  ")
            print("           \_;    '_")
            time.sleep(0.3)
            os.system("cls")
            print("      -^/        .--~~,__")
            print("      |  ^,-------`~~'._.'")
            print("       ^; ,'~.__;  ;"  )
            print("         ^, \`-__;,/  ")
            print("           \_;  /_'")
            time.sleep(0.3)
            os.system("cls")
        runAnim()
        runAnim()
        runAnim()
        runAnim()
        os.system("cls")
        print("YOU GOT A DOG!")
        time.sleep(3)
        os.system("cls")
        ending4()

    def smallApartmentChosen():
        os.system("cls")
        print("                                                           _")
        print("                                                          | |")
        print("                                                 .^.     /   \ ")
        print("                         ^              /\       | |   _/ [ ] \_")
        print("         O            *__=__*          /__\    O.' '.O|         |")
        print("        |=|          .(_____).         |  |    |                |")
        print("       _| |_        /         \       / [] \   | [][] [][] [][] |")
        print("     _|     |_     /    [][]   \     /  []  \  | [][] [][] [][] |")
        print("  __|         |__.' [][]    [][]'.o.'        '.|                |")
        print(" |               |  [][]    [][] | [][]   [][] | [][] [][] [][] |")
        print(" | .--. .-. .--. |  [][]    [][] | [][]   [][] | [][] [][] [][] |")
        print(" | [][] [ ] [][] | _ _           |             | [][] [][] [][] |")
        print(" |               ||X|X|          |             |                |")
        print(" ================= ___           |  __         |     ___        |")
        print(" | [][]|+++|[][] |||_||[][] [][] | |()| [][][] |[][]|=|=| [][]  |")
        print(" | [][]|===|[][] || _ |[][] [][] | |--| [][][] |[][]|=|=| [][]  |")
        print(" | [][]| | |[][] |||_||[][] [][] | |  | [][][] |[][]|8|8_______ |")
        print("_|_____|_|_|_____||___|__________|_|__|________|____|_|<_4sale_>|")
        print("                                                          ^|^    ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~")
        time.sleep(5)
        os.system("cls")
        ending1()

    def modernConstructionChosen():
        os.system("cls")
        print("             )")
        print("            (")
        print("    ________[]")
        print("   /^=^-^-^=^-^\ ")
        print("  /^-^-^-^-^-^-^\ ")
        print(" /__^_^_^_^^_^_^_\ ")
        print("  |  .==.       | ")
        print("^^|  |LI|  [}{] |^^^^^ ")
        print("&&|__|__|_______|&&    ")
        print("     ====              ")
        print("      ====             ")

        time.sleep(5)
        os.system("cls")
        ending2()

    def farmHouseChosen():

        os.system("cls")

        print("           )                                           _.-^-._    .--.")
        print("         ( _   _._                                  .-'   _   '-. |__|")
        print("          |_|-'_~_`-._                             /     |_|     \|  |")
        print("       _.-'-_~_-~_-~-_`-._                        /               \  |")
        print("   _.-'_~-_~-_-~-_~_~-_~-_`-._                   /|     _____     |\ |")
        print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                   |    |==|==|    |  |")
        print("    |  []  []   []   []  [] |                     |--  |--|  |    |  |")
        print("    |           __    ___   | |---|---|---|---|---|    |==|==|    |  |")
        print("  |=|________()|__|()_______|=|=|=|=|=|=|=|=|=|=|=|_______________|  |")
        print("^^^^^^^^^^^^^^^ === ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("    _______      ===")
        print("   <_4sale_>       ===")
        print("      ^|^             ===")
        print("       |                 ===")

        time.sleep(5)
        clearRows()
        os.system("cls")

        interfaceRows[4] = "           |   |  You now own a farm! With this comes    |    |"
        interfaceRows[5] = "           |   |  the opportunity to have pets as well.  |    |"
        interfaceRows[6] = "           |   |  do you want a dog, horses, or leave it |    |"
        interfaceRows[7] = "           |   |  at this?                               |    |"
        interfaceRows[9] = "           |   |  A. Doggo!                              |    |"
        interfaceRows[10] = "           |   |  B. I'd like horses!                    |    |"
        interfaceRows[11] = "           |   |  C. I'll leave it as is.                |    |"
        interfaceRows[14] = "           |   |  Type A/B/C to continue.                |    |"

        for Row in interfaceRows:
            print(Row)

        def farmHouseFinal():
            farmFinalChoice = input()
            if (farmFinalChoice == "A" or farmFinalChoice == "a"):
                petDog()
            elif (farmFinalChoice == "B" or farmFinalChoice == "b"):
                petHorses()
            elif (farmFinalChoice == "C" or farmFinalChoice == "c"):
                ending4()
            else:
                print("Invalid input! Please type A/B/C and press Enter.")
                farmHouseFinal()
        farmHouseFinal()

    def moveHouseOptions():

        os.system("cls")
        clearRows()

        interfaceRows[4] = "           |   |  After a long time of renting a place,  |    |"
        interfaceRows[5] = "           |   |  the opportunity to buy a house has     |    |"
        interfaceRows[6] = "           |   |  finally presented itself! Your jobs    |    |"
        interfaceRows[7] = "           |   |  have made sure you're in a stabile     |    |"
        interfaceRows[8] = "           |   |  financial situation, and you're both   |    |"
        interfaceRows[9] = "           |   |  eager to have your own place!          |    |"
        interfaceRows[10] = "           |   |                                         |    |"
        interfaceRows[14] = "           |   |  Press Enter to continue.               |    |"

        for Row in interfaceRows:
            print(Row)

            def moveHouseOptions2():
                os.system("cls")
                clearRows()

                interfaceRows[4] = "           |   |  You've looked online and checked out   |    |"
                interfaceRows[5] = "           |   |  some houses that seemed appealing IRL, |    |"
                interfaceRows[6] = "           |   |  there's 3 you might concider buying.   |    |"
                interfaceRows[8] = "           |   |  A. Small Apartment in Amsterdam        |    |"
                interfaceRows[9] = "           |   |  B. Modern Construction Home            |    |"
                interfaceRows[10] = "           |   |  C. Farm w/ Land and possibilities      |    |"
                interfaceRows[14] = "           |   |  Type A/B/C to continue.                |    |"

                for Row in interfaceRows:
                    print(Row)

                def moveHouseChoosing():
                    moveHouseChoice = input()
                    if (moveHouseChoice == "A" or moveHouseChoice == "a"):
                        smallApartmentChosen()
                    elif (moveHouseChoice == "B" or moveHouseChoice == "b"):
                        modernConstructionChosen()
                    elif (moveHouseChoice == "C" or moveHouseChoice == "c"):
                        farmHouseChosen()
                    else:
                        print("Invalid input! Please type A/B/C and press Enter.")
                        moveHouseChoosing()
                moveHouseChoosing()

        continueMoveHouse = getpass.getpass("")

        if continueMoveHouse:
            moveHouseOptions2()
        else:
            moveHouseOptions2()

    def becomeHouseWife():
            os.system("cls")
            clearRows()

            interfaceRows[4] = "           |   |  You have decided to stay here as a     |    |"
            interfaceRows[5] = "           |   |  full-time housewife. You do tasks      |    |"
            interfaceRows[6] = "           |   |  around the house while your            |    |"
            interfaceRows[7] = "           |   |  now-husband works. You don't have      |    |"
            interfaceRows[8] = "           |   |  enough money to even think of buying a |    |"
            interfaceRows[9] = "           |   |  house, but who knows what the future   |    |"
            interfaceRows[10] = "           |   |  will bring.                            |    |"
            interfaceRows[14] = "           |   | Press Enter to continue.                |    |"

            for Row in interfaceRows:
                print(Row)

            continueBecomeHW = getpass.getpass("")

            if continueBecomeHW:
                ending3()
            else:
                ending3()

    def getMarried():
        os.system("cls")
        time.sleep(1)

        print("   _.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._")
        print(" ,'_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._`.")
        print("( (                       -Original-                        ) )")
        print(" ) )              *Certificate Of Marriage*                ( (")
        print("( (                                                         ) )")
        print(" ) )               Location: North Holland                 ( (")
        print("( (                                                         ) )")
        print(" ) )    I,_____________________, hereby certify that on    ( (")
        print("( (     ",dateToday,", at ______________________________     ) )")
        print(" ) )                                                       ( (")
        print("( (      ____________________ and ____________________      ) )")
        print(" ) )                                                       ( (")
        print("( (      Witnessed and Celebrated by _________________      ) )")
        print(" ) )                                                       ( (")
        print("( (_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._) )")
        print(" `._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._,'")
        time.sleep(8)

        os.system("cls")

        print("    ...     _M_")
        print("   /( )\    ( )")
        print("  / / \ \  / : \ ")
        print("  ~~\%/~~  \|:|/")
        print("   /   \    |||")
        print("  /,,,,,\   |||")
        print("CONGRATULATIONS,")
        print("YOU ARE NOW MARRIED!")

        time.sleep(5)
        os.system("cls")
        time.sleep(2)

        def getMarriedContinue():
            os.system("cls")
            clearRows()

            interfaceRows[4] = "           |   |  Your Wedding went great, and you now   |    |"
            interfaceRows[5] = "           |   |  feel like everything became a lot more |    |"
            interfaceRows[6] = "           |   |  definite. Your life goes on in the     |    |"
            interfaceRows[7] = "           |   |  Netherlands, and you're planning ahead |    |"
            interfaceRows[8] = "           |   |  for the far future. You can now move   |    |"
            interfaceRows[9] = "           |   |  house, but you could also stay here    |    |"
            interfaceRows[10] = "           |   |  and be a housewife.                    |    |"
            interfaceRows[12] = "           |   |  A. Move House.                         |    |"
            interfaceRows[13] = "           |   |  B. Stay here and be a housewife.       |    |"
            interfaceRows[14] = "           |   |  Type A/B to continue.                  |    |"

            for Row in interfaceRows:
                print(Row)

            continueAfterMarriage = input()

            if (continueAfterMarriage == "A" or continueAfterMarriage == "a"):
                moveHouseOptions()
            elif (continueAfterMarriage == "B" or continueAfterMarriage == "b"):
                becomeHouseWife()
            else:
                print("Invalid input! Please type A or B and press Enter.")
                getMarriedContinue()

        getMarriedContinue()

    def notaryJobHired():
        os.system("cls")
        print(" _____________________________")
        print("|  _________________________  |")
        print("| |    ~ Notary John's ~    | |")
        print("| |                         | |")
        print("| | You are now hired!      | |")
        print("| | Salary: 25K Anually     | |")
        print("| | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ | |")
        print("| |_________________________| |")
        print("|_____________________________|")
        time.sleep(4)
        os.system("cls")
        moveHouseOptions()

    def officeJobHired():
        os.system("cls")
        print("*---------------***---------------*")
        print("| The Modern Office B.V.          |")
        print("|                                 |")
        print("| You are now hired!              |")
        print("| Salary: 10K Anually             |")
        print("|                                 |")
        print("|                                 |")
        print("|                                 |")
        print("⋆---------------------------------⋆")
        time.sleep(4)
        os.system("cls")
        moveHouseOptions()

    def nurseJobHired():
        os.system("cls")
        print("Oo------------oOo------------oO")
        print("| -UMC Amsterdam-             |")
        print("|                             |")
        print("| You are now hired!          |")
        print("|                             |")
        print("| Salary: €55K Anually        |")
        print("|                             |")
        print("Oo---------------------------oO")
        time.sleep(4)
        os.system("cls")
        moveHouseOptions()

    def findJob2():

        os.system("cls")
        clearRows()


        interfaceRows[4] = "           |   |  You're looking at available jobs in    |    |"
        interfaceRows[5] = "           |   |  the area; some pay more than others.   |    |"
        interfaceRows[6] = "           |   |  There's one job offer that stands out, |    |"
        interfaceRows[7] = "           |   |  paying well with €55K/year. You are    |    |"
        interfaceRows[8] = "           |   |  qualified due to your high education!  |    |"
        interfaceRows[10] = "           |   |  A. Office Job (€10,000/year)           |    |"
        interfaceRows[11] = "           |   |  B. Notary Job (€25,000/year)           |    |"
        interfaceRows[12] = "           |   |  C. Assistance Nurse Job (€55,000/year) |    |"
        interfaceRows[14] = "           |   |  Type A/B/C to continue.                |    |"

        for Row in interfaceRows:
            print(Row)

        def continueFindJob2():

            findJobAnswer = input()

            if (findJobAnswer == "A" or findJobAnswer == "a"):
                officeJobHired()
            elif (findJobAnswer == "B" or findJobAnswer == "b"):
                notaryJobHired()
            elif (findJobAnswer == "C" or findJobAnswer == "c"):
                nurseJobHired()
            else:
                print("Invalid input! Please type A/B/C and press Enter.")
                continueFindJob2()
        continueFindJob2()

    def notQualified():
        os.system("cls")
        clearRows()
        interfaceRows[4] = "           |   |  You are not qualified for this         |    |"
        interfaceRows[5] = "           |   |  position; you can however go back to   |    |"
        interfaceRows[6] = "           |   |  school to get a higher education!      |    |"
        interfaceRows[8] = "           |   |  Would you like to?                     |    |"
        interfaceRows[9] = "           |   |                                         |    |"
        interfaceRows[14] = "           |   |  Please type Y/N                        |    |"

        for Row in interfaceRows:
            print(Row)

        def continueNotQualified():

            notQualifiedAnswer = input()

            if (notQualifiedAnswer == "Y" or notQualifiedAnswer == "y"):
                os.system("cls")
                print("You're getting higher education!")
                time.sleep(2)
                findJob2()
            elif (notQualifiedAnswer == "N" or notQualifiedAnswer == "n"):
                findJob()
            else:
                print("Invalid input! Please type A or B and press Enter.")
                continueNotQualified()
        continueNotQualified()

    def findJob():

        os.system("cls")
        clearRows()

        interfaceRows[4] = "           |   |  You're looking at available jobs in    |    |"
        interfaceRows[5] = "           |   |  the area; some pay more than others.   |    |"
        interfaceRows[6] = "           |   |  There's one job offer that stands out, |    |"
        interfaceRows[7] = "           |   |  paying well with €55K/year, but do you |    |"
        interfaceRows[8] = "           |   |  have what it takes?                    |    |"
        interfaceRows[10] = "           |   |  A. Office Job (€10,000/year)           |    |"
        interfaceRows[11] = "           |   |  B. Notary Job (€25,000/year)           |    |"
        interfaceRows[12] = "           |   |  C. Assistance Nurse Job (€55,000/year) |    |"
        interfaceRows[14] = "           |   |  Type A/B/C to continue.                |    |"

        for Row in interfaceRows:
            print(Row)

        def continueFindJob():

            findJobAnswer = input()

            if (findJobAnswer == "A" or findJobAnswer == "a"):
                officeJobHired()
            elif (findJobAnswer == "B" or findJobAnswer == "b"):
                notaryJobHired()
            elif (findJobAnswer == "C" or findJobAnswer == "c"):
                notQualified()
            else:
                print("Invalid input! Please type A/B/C and press Enter.")
                continueFindJob()
        continueFindJob()

    def findLowIncomeJob():

        def cartAnim():
            os.system("cls")
            print("")
            print("/")
            print("")
            time.sleep(0.1)
            os.system("cls")
            print("")
            print("#/")
            print("o")
            time.sleep(0.1)
            os.system("cls")
            print("")
            print("##/")
            print(" o")
            time.sleep(0.1)
            os.system("cls")
            print("")
            print("###/")
            print("o o")
            time.sleep(0.1)
            os.system("cls")
            print("")
            print("\###/")
            print(" o o")
            time.sleep(0.1)
            os.system("cls")
            print("_")
            print(" \###/")
            print("  o o")
            time.sleep(0.1)
            os.system("cls")
            print(" _")
            print("  \###/")
            print("   o o")
            time.sleep(0.1)
            os.system("cls")
            print("   _")
            print("    \###/")
            print("     o o")
            time.sleep(0.1)
            os.system("cls")
            print("      _")
            print("       \###/")
            print("        o o")
            time.sleep(0.1)
            os.system("cls")
            print("         _")
            print("          \###/")
            print("           o o")
            time.sleep(0.1)
            os.system("cls")
            print("            _")
            print("             \###/")
            print("              o o")
            time.sleep(0.1)
            os.system("cls")
            print("               _")
            print("                \###/")
            print("                 o o")
            time.sleep(0.1)
            os.system("cls")
            print("                  _")
            print("                   \###/")
            print("                    o o")
            time.sleep(0.1)
            os.system("cls")
            print("                    _")
            print("                     \###/")
            print("                      o o")
            time.sleep(0.1)
            os.system("cls")
            print("                        _")
            print("                         \###/")
            print("                          o o")
            time.sleep(0.1)
            os.system("cls")
            print("                          _")
            print("                           \##")
            print("                            o")
            time.sleep(0.1)
            os.system("cls")
            print("                            _")
            print("                             \ ")
            print("                            ")
            time.sleep(0.1)
            os.system("cls")
        cartAnim()
        print("YOU WORK IN RETAIL NOW!")
        time.sleep(3.5)
        ending5()

    def dutchFull():
        clearRows()
        os.system("cls")

        interfaceRows[4] = "           |   |  You are now fluent in Dutch! This      |    |"
        interfaceRows[5] = "           |   |  allows you to get better jobs.         |    |"
        interfaceRows[6] = "           |   |  However, you can also get married. One |    |"
        interfaceRows[7] = "           |   |  thing's for sure; you're happy with    |    |"
        interfaceRows[8] = "           |   |  your life choices so far, and you      |    |"
        interfaceRows[9] = "           |   |  feel ready for marriage.               |    |"
        interfaceRows[11] = "           |   |  A. Get Married!                        |    |"
        interfaceRows[12] = "           |   |  B. Find a job.                         |    |"
        interfaceRows[14] = "           |   |  Type A/B to continue.                  |    |"

        for Row in interfaceRows:
            print(Row)

        def dutchFullAnswer():

            dutchFullAns = input()

            if (dutchFullAns == "A" or dutchFullAns == "a"):
                getMarried()
            elif (dutchFullAns == "B" or dutchFullAns == "b"):
                findJob()
            else:
                print("Invalid input! Please type A or B and press Enter.")
                dutchFullAnswer()
        dutchFullAnswer()

    def dutchPartial():

        def tvAnim():
            os.system("cls")
            print("               o")
            print("          o    |")
            print("           \   |")
            print("            \  |")
            print("             \.|-.")
            print("             (\|  )")
            print("    .==================.")
            print("    | .--------------. |")
            print("    | |##############| |")
            print("    | |##############| |")
            print("    | |##############| |")
            print("    | |##############| |")
            print("    | '--------------'o|")
            print("    | LI LI ^^^^^^^^  o|")
            print("    '=================='")
            time.sleep(1.5)
            os.system("cls")
            print("               o")
            print("          o    |")
            print("           \   |")
            print("            \  |")
            print("             \.|-.")
            print("             (\|  )")
            print("    .==================.")
            print("    | .--------------. |")
            print("    | |--.__.--.__.--| |")
            print("    | |--.__.--.__.--| |")
            print("    | |--.__.--.__.--| |")
            print("    | |--.__.--.__.--| |")
            print("    | '--------------'o|")
            print("    | LI LI ^^^^^^^^  o|")
            print("    '=================='")
            time.sleep(0.4)
            os.system("cls")
            print("               o")
            print("          o    |")
            print("           \   |")
            print("            \  |")
            print("             \.|-.")
            print("             (\|  )")
            print("    .==================.")
            print("    | .--------------. |")
            print("    | |NPO1          | |")
            print("    | |--.__.--.__.--| |")
            print("    | |--.__.--.__.--| |")
            print("    | |--.__.--.__.--| |")
            print("    | '--------------'o|")
            print("    | LI LI ^^^^^^^^  o|")
            print("    '=================='")
            time.sleep(1)
            os.system("cls")
            print("               o")
            print("          o    |")
            print("           \   |")
            print("            \  |")
            print("             \.|-.")
            print("             (\|  )")
            print("    .==================.")
            print("    | .--------------. |")
            print("    | |RTL7          | |")
            print("    | |--.__.--.__.--| |")
            print("    | |--.__.--.__.--| |")
            print("    | |--.__.--.__.--| |")
            print("    | '--------------'o|")
            print("    | LI LI ^^^^^^^^  o|")
            print("    '=================='")
            time.sleep(1)
            os.system("cls")
            print("               o")
            print("          o    |")
            print("           \   |")
            print("            \  |")
            print("             \.|-.")
            print("             (\|  )")
            print("    .==================.")
            print("    | .--------------. |")
            print("    | |Veronica      | |")
            print("    | |--.__.--.__.--| |")
            print("    | |--.__.--.__.--| |")
            print("    | |--.__.--.__.--| |")
            print("    | '--------------'o|")
            print("    | LI LI ^^^^^^^^  o|")
            print("    '=================='")
            time.sleep(1)
            os.system("cls")
            print("               o")
            print("          o    |")
            print("           \   |")
            print("            \  |")
            print("             \.|-.")
            print("             (\|  )")
            print("    .==================.")
            print("    | .--------------. |")
            print("    | |SBS6          | |")
            print("    | |--.__.--.__.--| |")
            print("    | |--.__.--.__.--| |")
            print("    | |--.__.--.__.--| |")
            print("    | '--------------'o|")
            print("    | LI LI ^^^^^^^^  o|")
            print("    '=================='")
            time.sleep(1)
            os.system("cls")
            print("               o")
            print("          o    |")
            print("           \   |")
            print("            \  |")
            print("             \.|-.")
            print("             (\|  )")
            print("    .==================.")
            print("    | .--------------. |")
            print("    | |##############| |")
            print("    | |#-.__.--.__.-#| |")
            print("    | |#-.__.--.__.-#| |")
            print("    | |##############| |")
            print("    | '--------------'o|")
            print("    | LI LI ^^^^^^^^  o|")
            print("    '=================='")
            time.sleep(0.3)
            os.system("cls")
            print("               o")
            print("          o    |")
            print("           \   |")
            print("            \  |")
            print("             \.|-.")
            print("             (\|  )")
            print("    .==================.")
            print("    | .--------------. |")
            print("    | |##############| |")
            print("    | |####_.--._####| |")
            print("    | |####_.--._####| |")
            print("    | |##############| |")
            print("    | '--------------'o|")
            print("    | LI LI ^^^^^^^^  o|")
            print("    '=================='")
            time.sleep(0.3)
            os.system("cls")
            print("               o")
            print("          o    |")
            print("           \   |")
            print("            \  |")
            print("             \.|-.")
            print("             (\|  )")
            print("    .==================.")
            print("    | .--------------. |")
            print("    | |##############| |")
            print("    | |##############| |")
            print("    | |##############| |")
            print("    | |##############| |")
            print("    | '--------------'o|")
            print("    | LI LI ^^^^^^^^  o|")
            print("    '=================='")
            time.sleep(2)
        tvAnim()
        os.system("cls")
        print("You've learned a bit of Dutch!")
        time.sleep(2.5)
        findJob()

    def cantFindGoodJob():
        clearRows()
        os.system("cls")

        interfaceRows[4] = "           |   |  You've looked at available jobs.       |    |"
        interfaceRows[5] = "           |   |  It seems that every decent job         |    |"
        interfaceRows[6] = "           |   |  requires at least some knowledge of    |    |"
        interfaceRows[7] = "           |   |  the Dutch language. How would you like |    |"
        interfaceRows[8] = "           |   |  to proceed?                            |    |"
        interfaceRows[10] = "           |   |  A. I'll find a job anyways.            |    |"
        interfaceRows[11] = "           |   |  B. I'll go and learn Dutch first.      |    |"
        interfaceRows[14] = "           |   |  Type A/B to continue.                  |    |"

        for Row in interfaceRows:
            print(Row)


        def cantGoodJob():
            badJobChoice = input()

            if (badJobChoice == "A" or badJobChoice == "a"):
                findLowIncomeJob()
            elif (badJobChoice == "B" or badJobChoice == "b"):
                learnDutch()
            else:
                print("Invalid input! Please type A or B and press Enter.")
                cantGoodJob()
        cantGoodJob()

    def dutchCourse_Anim():

        os.system("cls")
        clearRows()
        interfaceRows[3] = "           |   |[YouT..][Chro..][Language Courses NL]_[X]|    |"
        interfaceRows[4] = "           |   |                                         |    |"
        interfaceRows[5] = "           |   | Dutch Language Course - 5 Months        |    |"
        interfaceRows[6] = "           |   |-----------------------------------------|    |"
        interfaceRows[7] = "           |   | o Course for absolute Beginners         |    |"
        interfaceRows[8] = "           |   | o 10 Hours / Week                       |    |"
        interfaceRows[9] = "           |   | o €55 Per Hour                          |    |"
        interfaceRows[10] = "           |   |                                /\       |    |"
        interfaceRows[11] = "           |   | (More Info)                             |    |"
        interfaceRows[12] = "           |   | (Contact)                               |    |"
        interfaceRows[13] = "           |   | (Sign In/Sign Up)                       |    |"
        interfaceRows[14] = "           |   |                                         |    |"

        for Row in interfaceRows:
            print(Row)
        time.sleep(5)

        os.system("cls")
        clearRows()
        interfaceRows[3] = "           |   |[YouT..][Chro..][Language Courses NL]_[X]|    |"
        interfaceRows[4] = "           |   |                                         |    |"
        interfaceRows[5] = "           |   | Dutch Language Course - 5 Months        |    |"
        interfaceRows[6] = "           |   |-----------------------------------------|    |"
        interfaceRows[7] = "           |   | o Course for absolute Beginners         |    |"
        interfaceRows[8] = "           |   | o 10 Hours / Week                       |    |"
        interfaceRows[9] = "           |   | o €55 Per Hour                          |    |"
        interfaceRows[10] = "           |   |                                         |    |"
        interfaceRows[11] = "           |   | (More Info)                 /\          |    |"
        interfaceRows[12] = "           |   | (Contact)                               |    |"
        interfaceRows[13] = "           |   | (Sign In/Sign Up)                       |    |"
        interfaceRows[14] = "           |   |                                         |    |"
        for Row in interfaceRows:
            print(Row)
        time.sleep(1)
        os.system("cls")
        clearRows()
        interfaceRows[3] = "           |   |[YouT..][Chro..][Language Courses NL]_[X]|    |"
        interfaceRows[4] = "           |   |                                         |    |"
        interfaceRows[5] = "           |   | Dutch Language Course - 5 Months        |    |"
        interfaceRows[6] = "           |   |-----------------------------------------|    |"
        interfaceRows[7] = "           |   | o Course for absolute Beginners         |    |"
        interfaceRows[8] = "           |   | o 10 Hours / Week                       |    |"
        interfaceRows[9] = "           |   | o €55 Per Hour                          |    |"
        interfaceRows[10] = "           |   |                                         |    |"
        interfaceRows[11] = "           |   | (More Info)                             |    |"
        interfaceRows[12] = "           |   | (Contact)              /\               |    |"
        interfaceRows[13] = "           |   | (Sign In/Sign Up)                       |    |"
        interfaceRows[14] = "           |   |                                         |    |"
        for Row in interfaceRows:
            print(Row)
        time.sleep(1)
        os.system("cls")
        clearRows()
        interfaceRows[3] = "           |   |[YouT..][Chro..][Language Courses NL]_[X]|    |"
        interfaceRows[4] = "           |   |                                         |    |"
        interfaceRows[5] = "           |   | Dutch Language Course - 5 Months        |    |"
        interfaceRows[6] = "           |   |-----------------------------------------|    |"
        interfaceRows[7] = "           |   | o Course for absolute Beginners         |    |"
        interfaceRows[8] = "           |   | o 10 Hours / Week                       |    |"
        interfaceRows[9] = "           |   | o €55 Per Hour                          |    |"
        interfaceRows[10] = "           |   |                                         |    |"
        interfaceRows[11] = "           |   | (More Info)                             |    |"
        interfaceRows[12] = "           |   | (Contact)                               |    |"
        interfaceRows[13] = "           |   | (Sign In/Sign Up) /\                    |    |"
        interfaceRows[14] = "           |   |                                         |    |"
        for Row in interfaceRows:
            print(Row)
        time.sleep(1)
        os.system("cls")
        clearRows()
        interfaceRows[3] = "           |   |[YouT..][Chro..][Language Courses NL]_[X]|    |"
        interfaceRows[4] = "           |   |                                         |    |"
        interfaceRows[5] = "           |   | Dutch Language Course - 5 Months        |    |"
        interfaceRows[6] = "           |   |-----------------------------------------|    |"
        interfaceRows[7] = "           |   | o Course for absolute Beginners         |    |"
        interfaceRows[8] = "           |   | o 10 Hours / Week                       |    |"
        interfaceRows[9] = "           |   | o €55 Per Hour                          |    |"
        interfaceRows[10] = "           |   |                                         |    |"
        interfaceRows[11] = "           |   | (More Info)                             |    |"
        interfaceRows[12] = "           |   | (Contact)                               |    |"
        interfaceRows[13] = "           |   | (SIGN IN/SIGN/\P)                       |    |"
        interfaceRows[14] = "           |   |                                         |    |"
        for Row in interfaceRows:
            print(Row)
        time.sleep(1)
        os.system("cls")
        clearRows()
        interfaceRows[3] = "           |   |[YouT..][Chro..][Language Courses NL]_[X]|    |"
        interfaceRows[4] = "           |   |                                         |    |"
        interfaceRows[5] = "           |   | Dutch Language Course - 5 Months        |    |"
        interfaceRows[6] = "           |   |-----------------------------------------|    |"
        interfaceRows[7] = "           |   | Name: _____________________             |    |"
        interfaceRows[8] = "           |   | Address: __________________             |    |"
        interfaceRows[9] = "           |   | Phone: ____________________             |    |"
        interfaceRows[10] = "           |   |                                         |    |"
        interfaceRows[11] = "           |   |                                         |    |"
        interfaceRows[12] = "           |   |             /\                          |    |"
        interfaceRows[13] = "           |   | (Confirm)                               |    |"
        interfaceRows[14] = "           |   |                                         |    |"
        for Row in interfaceRows:
            print(Row)
        time.sleep(5)
        os.system("cls")
        clearRows()
        interfaceRows[3] = "           |   |[YouT..][Chro..][Language Courses NL]_[X]|    |"
        interfaceRows[4] = "           |   |                                         |    |"
        interfaceRows[5] = "           |   | Dutch Language Course - 5 Months        |    |"
        interfaceRows[6] = "           |   |-----------------------------------------|    |"
        interfaceRows[7] = "           |   | Name: ___..........________             |    |"
        interfaceRows[8] = "           |   | Address: __....__..__....._             |    |"
        interfaceRows[9] = "           |   | Phone: __.._........_______             |    |"
        interfaceRows[10] = "           |   |                                         |    |"
        interfaceRows[11] = "           |   |                                         |    |"
        interfaceRows[12] = "           |   |                                         |    |"
        interfaceRows[13] = "           |   | (CON/\RM)                               |    |"
        interfaceRows[14] = "           |   |                                         |    |"
        for Row in interfaceRows:
            print(Row)
        time.sleep(2)
        os.system("cls")
        clearRows()
        interfaceRows[3] = "           |   |[YouT..][Chro..][Language Courses NL]_[X]|    |"
        interfaceRows[4] = "           |   |                                         |    |"
        interfaceRows[5] = "           |   | Dutch Language Course - 5 Months        |    |"
        interfaceRows[6] = "           |   |-----------------------------------------|    |"
        interfaceRows[7] = "           |   | You have signed up for this course!     |    |"
        interfaceRows[8] = "           |   | Please check your inbox for a           |    |"
        interfaceRows[9] = "           |   | confirmation E-mail.                    |    |"
        interfaceRows[10] = "           |   |                                         |    |"
        interfaceRows[11] = "           |   |                                         |    |"
        interfaceRows[12] = "           |   |                                         |    |"
        interfaceRows[13] = "           |   |                                         |    |"
        interfaceRows[14] = "           |   |                                         |    |"
        for Row in interfaceRows:
            print(Row)
        time.sleep(4)
        os.system("cls")
        dutchFull()

    def learnDutch():
        clearRows()
        os.system("cls")

        interfaceRows[4] = "           |   |  You think it's best to start by        |    |"
        interfaceRows[5] = "           |   |  learning the language, and damn right  |    |"
        interfaceRows[6] = "           |   |  you are! How would you like to learn   |    |"
        interfaceRows[7] = "           |   |  Dutch?                                 |    |"
        interfaceRows[9] = "           |   |  A. I'll sign up to follow a course.    |    |"
        interfaceRows[10] = "           |   |  B. I'll watch TV and read the News.    |    |"
        interfaceRows[14] = "           |   |  Type A/B to continue.                  |    |"

        for Row in interfaceRows:
            print(Row)

        def continueLearnDutch():

            continueLearnDutchAns = input()

            if (continueLearnDutchAns == "A" or continueLearnDutchAns == "a"):
                dutchCourse_Anim()
            elif (continueLearnDutchAns == "B" or continueLearnDutchAns == "b"):
                dutchPartial()
            else:
                print("Invalid input! Please type A or B and press Enter.")
                continueLearnDutch()
        continueLearnDutch()

    def findJobNoDutch():
        clearRows()
        os.system("cls")

        interfaceRows[4] = "           |   |  You are trying to find a job, but      |    |"
        interfaceRows[5] = "           |   |  you don't know any Dutch. Your English |    |"
        interfaceRows[6] = "           |   |  could use a touch-up as well.          |    |"
        interfaceRows[8] = "           |   |                                         |    |"
        interfaceRows[14] = "           |   |  Press Enter to continue.               |    |"

        for Row in interfaceRows:
            print(Row)

        def continueFindJobNoDutch():

            continueFindJobNoDutch = getpass.getpass("")

            if continueFindJobNoDutch:
                cantFindGoodJob()
            else:
                cantFindGoodJob()
        continueFindJobNoDutch()

    def NL_Anim():
        os.system("cls")

        print("          ")
        print("      @@@@")
        print("   %@@@@@@")
        print(" ,%@@@@   ")
        print("          ")

        time.sleep(1)
        os.system("cls")

        print("                    ")
        print("        *  *@@@@@@@ ")
        print("       .   @@@@@@@@@")
        print("       @@@  @@@@@@@ ")
        print("      @@@@@@@@@@@@@ ")
        print("     @@@@@@@@@@@@@  ")
        print("   @#@@@@@@@@@      ")
        print(" @@@ @@ @@@@@@@     ")
        print("             @@     ")
        print("            @@      ")

        time.sleep(1)
        os.system("cls")

        print("                              ")
        print("              %    @@@@@@@@.  ")
        print("           (    @@@@@@@@@@@@@@")
        print("             .  @@@@@@@@@@@@@@")
        print("          @@@@,  %@@@@@@@@@@@ ")
        print("          @@@   .@@@@@@@@@    ")
        print("         @@@@ @@@@@@@@@@@@@@@ ")
        print("        @@@@@@@@@@@@@@@@@@@   ")
        print("     @@@@@@@@@@@@&@@@@@@@@@   ")
        print("   ,@@@%@@@@@@&@@@@@          ")
        print(" @@%# @@@@@@@@@@@@@@@@        ")
        print("/@@@@@@       @@@@@@@@        ")
        print("                   @@         ")
        print("                  %@@         ")

        time.sleep(1)
        os.system("cls")

        print("          WELCOME TO THE NETHERLANDS!             ")
        print("                                                  ")
        print("                           @ @*#         *@@@     ")
        print("                             .@@@@@@@&@@@@@@@@    ")
        print("                           @@@@@@@@@@@@@@@@@@@@@@(")
        print("                  @@      @@@@@@@@@@@@@@@@@@@@@@@ ")
        print("                / .   *   &@@@@@@@@@@@@@@@@@@@@@@ ")
        print("                 @@@@@&   ,(&*@@@@@&@@@@@@@@@@@@  ")
        print("                ,@@@@@@@@    @@@@@@@@@@@@@@@@@@#  ")
        print("                @@@@@/       @@&@@@@@@@@@@@       ")
        print("                @@@@@@    @@@@@@@@@@@@@@@@@       ")
        print("               @@@@@@  @@@@@@&@@@@@@@@@@@@@@@@@@  ")
        print("              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/  ")
        print("            @@@@@@&@@@@@@@@@@@@@@@@@@@@@@@&@&     ")
        print("          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      ")
        print("         @@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@         ")
        print("      #@&@@ @@@@@@@@@@@@@@@@@@@@@&                ")
        print("    .  @@*@&@@@@@@@@@@@@@@@@@@@@@@@               ")
        print(" %@@#@@@% ,@@@@@@@@@@@@@@@@@@@@@@@@@@             ")
        print(" #@   # @  %@@        @@@@@@@@@@@@@@@             ")
        print(" @   %@@@@              %%% @@@@@@@*              ")
        print("                                @@@#              ")
        print("                               @,                 ")
        print("                              @@@@@               ")
        print("                              @@%@                ")

        time.sleep(4)
        os.system("cls")

    def moved():

        NL_Anim()

        def movedContinued():
            clearRows()
            os.system("cls")

            interfaceRows[4] = "           |   |  After traveling in the car for 6       |    |"
            interfaceRows[5] = "           |   |  long hours, you have arrived in the    |    |"
            interfaceRows[6] = "           |   |  Netherlands. You are moving in with    |    |"
            interfaceRows[7] = "           |   |  your boyfriend! What's the next big    |    |"
            interfaceRows[8] = "           |   |  step?                                  |    |"
            interfaceRows[10] = "           |   |  A. Learn Dutch!                        |    |"
            interfaceRows[11] = "           |   |  B. Search for a job.                   |    |"
            interfaceRows[14] = "           |   |  Type A/B to continue.                  |    |"

            for Row in interfaceRows:
                print(Row)

            def movedFN():

                movedAnswer = input()

                if (movedAnswer == "A" or movedAnswer == "a"):
                    learnDutch()
                elif (movedAnswer == "B" or movedAnswer == "b"):
                    findJobNoDutch()
                else:
                    print("\nInvalid input! Please type A or B and press Enter.")
                    time.sleep(2)

                    movedContinued()
            movedFN()
        movedContinued()

    def intro():


        def blackScreen():

            os.system("cls")
            interfaceRows[3] = "           |   |#########################################|    |"
            interfaceRows[4] = "           |   |#########################################|    |"
            interfaceRows[5] = "           |   |#########################################|    |"
            interfaceRows[6] = "           |   |#########################################|    |"
            interfaceRows[7] = "           |   |#########################################|    |"
            interfaceRows[8] = "           |   |#########################################|    |"
            interfaceRows[9] = "           |   |#########################################|    |"
            interfaceRows[10] = "           |   |#########################################|    |"
            interfaceRows[11] = "           |   |#########################################|    |"
            interfaceRows[12] = "           |   |#########################################|    |"
            interfaceRows[13] = "           |   |#########################################|    |"
            interfaceRows[14] = "           |   |#########################################|    |"
            for Row in interfaceRows:
                print(Row)

        def alienwareText():

            os.system("cls")
            interfaceRows[3] = "           |   |#########################################|    |"
            interfaceRows[4] = "           |   |#########################################|    |"
            interfaceRows[5] = "           |   |#########################################|    |"
            interfaceRows[6] = "           |   |#########################################|    |"
            interfaceRows[7] = "           |   |#########################################|    |"
            interfaceRows[8] = "           |   |  /_\ | |(_)__ _ _ __ __ __ __ _ _ _ ___ |    |"
            interfaceRows[9] = "           |   | / _ \| | | -_) ' | V  V // _` || '_| -_)|    |"
            interfaceRows[10] = "           |   |/_/ \_\_|_|___|_||_\_/\_/ \__,_||_| \___ |    |"
            interfaceRows[11] = "           |   |#########################################|    |"
            interfaceRows[12] = "           |   |#########################################|    |"
            interfaceRows[13] = "           |   |#########################################|    |"
            interfaceRows[14] = "           |   |#########################################|    |"
            for Row in interfaceRows:
                print(Row)

        def alienwareTextSmaller():

            os.system("cls")
            interfaceRows[3] = "           |   |#########################################|    |"
            interfaceRows[4] = "           |   |#########################################|    |"
            interfaceRows[5] = "           |   |#########################################|    |"
            interfaceRows[6] = "           |   |#########################################|    |"
            interfaceRows[7] = "           |   |#########################################|    |"
            interfaceRows[8] = "           |   |#########################################|    |"
            interfaceRows[9] = "           |   | / _ \| | | -_) ' | V  V // _` || '_| -_)|    |"
            interfaceRows[10] = "           |   |#########################################|    |"
            interfaceRows[11] = "           |   |#########################################|    |"
            interfaceRows[12] = "           |   |#########################################|    |"
            interfaceRows[13] = "           |   |#########################################|    |"
            interfaceRows[14] = "           |   |#########################################|    |"
            for Row in interfaceRows:
                print(Row)

        def alienLogo():

            os.system("cls")
            interfaceRows[3] = "           |   |@@@@@@@@@@@@@@@@@@@@,,@@@@@@@@@@@@@@@@@@@|    |"
            interfaceRows[4] = "           |   |@@@@@@@@@@@@@@@            @@@@@@@@@@@@@@|    |"
            interfaceRows[5] = "           |   |@@@@@@@@@@@@@                @@@@@@@@@@@@|    |"
            interfaceRows[6] = "           |   |@@@@@@@@@@@@                  @@@@@@@@@@@|    |"
            interfaceRows[7] = "           |   |@@@@@@@@@@@@                  @@@@@@@@@@@|    |"
            interfaceRows[8] = "           |   |@@@@@@@@@@@(                  @@@@@@@@@@@|    |"
            interfaceRows[9] = "           |   |@@@@@@@@@@@@ @@@          @@@ @@@@@@@@@@@|    |"
            interfaceRows[10] = "           |   |@@@@@@@@@@@@ @@@@@     .@@@@@ @@@@@@@@@@@|    |"
            interfaceRows[11] = "           |   |@@@@@@@@@@@@@% @@@@@  @@@@@ @@@@@@@@@@@@@|    |"
            interfaceRows[12] = "           |   |@@@@@@@@@@@@@@@            @@@@@@@@@@@@@@|    |"
            interfaceRows[13] = "           |   |@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@|    |"
            interfaceRows[14] = "           |   |@@@@@@@@@@@@@@@@@@@**&@@@@@@@@@@@@@@@@@@@|    |"

            for Row in interfaceRows:
                print(Row)

        def alienGlitch_1():

            os.system("cls")
            interfaceRows[3] = "           |   |  @@@@@@@@@@@@@@@@@@,,@@@@@@@@@@@@@@@@@@ |    |"
            interfaceRows[4] = "           |   |  @@@@@@@@@@@@@            @@@@@@@@@@@@@ |    |"
            interfaceRows[5] = "           |   |  @@@@@@@@@@@                @@@@@@@@@@@ |    |"
            interfaceRows[6] = "           |   |  @@@@@,(*,,****..*,*,,,,,,,  @@@@@@@@@@ |    |"
            interfaceRows[7] = "           |   |  @@@@@@,,,,,,.,,**           @@@@@@@@@@ |    |"
            interfaceRows[8] = "           |   |  @@,@@@@@@(   ,              @@@@@@@@@@ |    |"
            interfaceRows[9] = "           |   |  @@@@@@@@@@ @@@          @@@ @@@@@@@@@@ |    |"
            interfaceRows[10] = "           |   |  @@@@@@@@@@ @@@@@     .@@@@@ @@@@@@@@@@ |    |"
            interfaceRows[11] = "           |   |  @@@@@,..,..,.@**/@  /***@ @@@@@@@@@@@@ |    |"
            interfaceRows[12] = "           |   |  @@@@@@@@@@@@@          , @@@@@@@@@@@@@ |    |"
            interfaceRows[13] = "           |   |  @@@@@#%#%%%&&@@        @@@@@@@@@@@@@@@ |    |"
            interfaceRows[14] = "           |   |@@@@@@@@@@@@@@@@@@**\..@@@@@@@@@@@@@@@@@@|    |"
            for Row in interfaceRows:
                print(Row)

        def alienGlitch_2():

            os.system("cls")
            interfaceRows[3] = "           |   |(#%#%&&&%@@@(@@&##@@,,@@@@@@@&&&%%&%%%@@@|    |"
            interfaceRows[4] = "           |   |@@@/////@@@*(/@            @@######%##@@@|    |"
            interfaceRows[5] = "           |   |@@@@@@((##&*(,,,,,,,,,,,,,,,,%%%%%%%%%%@@|    |"
            interfaceRows[6] = "           |   |@@@(( .    .  .  *.,.,,,,.......@@@@@@@@@|    |"
            interfaceRows[7] = "           |   |@&@@@@,,*%%%                  &@@&&&&&&&&|    |"
            interfaceRows[8] = "           |   |@&@@&@&@&&@(.....             &&@&&&&&&&&|    |"
            interfaceRows[9] = "           |   |@@%#%%@@&&%& &&&(/*       @@@ @@@@@@@@@@@|    |"
            interfaceRows[10] = "           |   |@@%%@@@&@@@# %#(#@     .@@&&& &@@@@@@@@@@|    |"
            interfaceRows[11] = "           |   |@@@@@@@@@@@@@% @@@@@  @&%%% &@@@@@@@%&&%&|    |"
            interfaceRows[12] = "           |   |@@@@@@@@@@@@@@@            %%%@@@@#%#%@@@|    |"
            interfaceRows[13] = "           |   |@@@@@(#%%%%%#%#@&**,**   /@&@&@@@@/&@@@@@|    |"
            interfaceRows[14] = "           |   |@@@@@@@@@@@@@@@@@**%*)##@@@@@@@@@@@@@@@@@|    |"
            for Row in interfaceRows:
                print(Row)

        blackScreen()
        time.sleep(2)
        alienLogo()
        time.sleep(2)
        alienGlitch_1()
        time.sleep(0.1)
        alienLogo()
        time.sleep(1)
        alienGlitch_1()
        time.sleep(0.1)
        alienGlitch_2()
        time.sleep(0.1)
        alienLogo()
        time.sleep(1)
        alienwareText()
        time.sleep(2)
        alienwareTextSmaller()
        time.sleep(0.6)
        blackScreen()
        time.sleep(0.6)

        os.system("cls")
        clearRows()

        interfaceRows[4] = "           |   |  Welcome to my Game! Here, you will go  |    |"
        interfaceRows[5] = "           |   |  on a journey, make choices and follow  |    |"
        interfaceRows[6] = "           |   |  a story. This game based on a true     |    |"
        interfaceRows[7] = "           |   |  series of events.                      |    |"
        interfaceRows[9] = "           |   |  Remember, your choices will decide the |    |"
        interfaceRows[10] = "           |   |  final outcome of the story!            |    |"
        interfaceRows[14] = "           |   |  Press Enter to continue.               |    |"

        for Row in interfaceRows:
            print(Row)

        def continueIntro():

            continueIntroAnswer = getpass.getpass("")

            if continueIntroAnswer:
                os.system("cls")
                clearRows()

                interfaceRows[4] = "           |   |  You're a 26 y/o girl, who met the love |    |"
                interfaceRows[5] = "           |   |  of her life during a vacation to       |    |"
                interfaceRows[6] = "           |   |  Scotland. He lives in the Netherlands, |    |"
                interfaceRows[7] = "           |   |  and you'd very much like to move there |    |"
                interfaceRows[8] = "           |   |  to spend your lives together...        |    |"
                interfaceRows[14] = "           |   |  Press Enter to start your Journey!     |    |"

                for Row in interfaceRows:
                    print(Row)

                continueIntroAnswer2 = getpass.getpass("")

                if continueIntroAnswer2:
                    moved()
                else:
                    moved()

            else:
                os.system("cls")
                clearRows()

                interfaceRows[4] = "           |   |  You're a 26 y/o girl, who met the love |    |"
                interfaceRows[5] = "           |   |  of her life during a vacation to       |    |"
                interfaceRows[6] = "           |   |  Scotland. He lives in the Netherlands, |    |"
                interfaceRows[7] = "           |   |  and you'd very much like to move there |    |"
                interfaceRows[8] = "           |   |  to spend your lives together...        |    |"
                interfaceRows[14] = "           |   |  Press Enter to start your Journey!     |    |"

                for Row in interfaceRows:
                    print(Row)

                continueIntroAnswer3 = getpass.getpass("")
                if continueIntroAnswer3:
                    moved()
                else:
                    moved()

        continueIntro()

    # PROGRAM STARTS HERE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    intro()

pythonKeuzeVerhaal()
