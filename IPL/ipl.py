import random
status = True
teams = ["CSK", "SRH", "PBKS", "DC", "LSG", "KKR", "RR", "GT", "RCB", "MI"]

while status:

    teams = ["CSK", "SRH", "PBKS", "DC", "LSG", "KKR", "RR", "GT", "RCB", "MI"]
    myTeam = input("Enter your team : ").upper()

    if myTeam in teams:

        opponent = random.choice(teams)
        while myTeam == opponent:
            opponent = random.choice(teams)
        print("-------------------------------------------------------")
        print(f"{myTeam} VS {opponent}")
        print("-------------------------------------------------------")

        tossOptions = ['H', 'T']
        tossChoice = input("Enter H or T for Toss : ").upper()
        if tossChoice in tossOptions:
            tossResult = random.choice(tossOptions)
            choiceOptions = ['BAT', 'BALL']
            if tossChoice == tossResult:
                print(f"{myTeam} Won the Toss...")
                choice = input("Enter Bat or Ball : ").upper()
            else:
                print(f"{opponent} Won the Toss and Choose : {random.choice(choiceOptions)}")

            myScore = random.randint(49, 287)
            myWickets = random.randint(0, 10)
            opponentScore = random.randint(49, 287)
            opponentWickets = random.randint(0, 10)

            print("-------------------------------------------------------")

            print(f"{myTeam} : {myScore}/{myWickets}")
            print(f"{opponent} : {opponentScore}/{opponentWickets}")

            print("-------------------------------------------------------")
            if myScore > opponentScore:
                print(f"{myTeam} is Winner..!")
            elif myScore == opponentScore:
                print("Match Was Draw..!")
            else:
                print(f"{opponent} is Winner..!")
            print("-------------------------------------------------------")
        else:
            print("INVALID INPUT..! Choose only H | T")
            
    else:
        print(f"{myTeam} is not avilable in IPL")

    playMore = input("Are you want to play more??(Y | YES) : ").upper()
    if playMore == 'Y' or playMore == 'YES':
        status = True
    else:
        status = False
