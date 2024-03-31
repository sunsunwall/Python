#Räkna ut avkastningen under 5år på en investering av 100 000kr vid olika räntenivåer.
#Skriven av Sunny Vanderwall 2024-03
#tabulate modulen importeras för att visualisera uträkningen som en tabell.
from tabulate import tabulate
#time modulen importeras för att skapa ett trevligare och dynamiskt avslut av programmet
import time

bank_emoji = "\U0001F3E6"
atm_emoji = "\U0001F3E7"
no_entry_emoji =  "\U0001F6AB"
hand_wave_emoji = "\U0001F44B"
bow_emoji = "\U0001F647"
hand_down_emoji = "\U0001F447"
chart_emoji = "\U0001F4C8"
hand_right_pointing_emoji = "\U0001F449"


print(f"{chart_emoji} Välkommen till investeringsräknaren!\n\n{bank_emoji} Du sätter in 100 000kr på banken. Hur mycket är den värd efter 5 år vid olika räntenivåer?")

#Nestat i en while loop for att kunna räkna flera olika räntenivåer
while True:
    #Detta program är endast avsett att räkna på en investering på 100 000kr
    investering = 100000
    #while true + try används för hantera om användaren matar in något som inte är ett flyttal
    while True:
        try:
            ranta = float(input(f"\n{hand_right_pointing_emoji} Ange årlig ränta: "))
            #Om användaren matar in ett flyttal så bryts denna loop.
            break
        #om användaren matar in något som inte är ett flyttal loopas användaren tillbaka för att ange korrekt värde.
        except ValueError:
            print(f"\n{no_entry_emoji} Felaktigt värde, skriv räntan som en siffra (tex: 3.25)")
    #En variable i form av en lista läggs in för att spara uträkningarna i for loopen nedan och sedan visualisera resultatet som en tabell.
    tabell = []
    #En for loop används för att räkna ut ränta på ränta effekten under 5 års tid. Varje iterations uträkning sparas i variabeln "tabell"
    for i in range(1,6):
        arlig_avkastning = investering * (ranta/100)
        investering += arlig_avkastning
        tabell.append([i,f"{ranta:.2f}%" ,f"{arlig_avkastning:.2f}kr", f"{investering:.2f}kr"])
    
    #Användaren behöver på ett enkelt sätt kunna se avkastning per år samt totalt värde på investeringen efter 5 år. Detta visualiseras med en tabell för att ge användaren en enkel överblick.
    headers = ["År","Ränta" ,"Årlig Avkastning", "Värde på investering"]
    
    print(f"\n{hand_down_emoji} Avkastning under en 5 års horisont:\n\n{tabulate(tabell, headers=headers, tablefmt="grid")}")
    
    print(f"\n{atm_emoji} Totalt värde efter 5 år: {investering:.2f}kr")
    print(f"\n{chart_emoji} Total avkastning efter 5 år: {(investering-100000):.2f}kr")

    #Användaren ges möjlighet att göra om uträkningen med en annan räntesats då hen kanske vill jämföra olika banker.
    igen = input(f"\n=================================================================\n\n{hand_right_pointing_emoji} Vill du räkna ut investeringen med en annan räntesats? (j/n): ")
    if igen != "j":
        print(f"\n\n{bow_emoji} Tack för att du använde investeringsräknaren.")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print(f"{hand_wave_emoji} Hej då!")
        time.sleep(0.5)
        print("...")
        break