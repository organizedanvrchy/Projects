print("\nYou wake up on a beach with nothing but "
      "the drenched clothes on your back.")
print("The sun overhead, beaming down at you. "
      "You're a little dazed but you stand up and look around.")
print("You notice some palm tree and walk towards them for some shade.")
print("As you approach, you notice some planks strewn together " 
      "with words etched into them that say: ")
print("\nWelcome to TRSR ISLAND\n")
print("'I made it! I finally made it!' you exclaim, "
      "an adventurer who has searched for this island for years.")
print("With great enthusiam, you continue to investigate the sign.")
print("You find that the sign also has arrows pointing right and left.")
print("Above the right arrow, there's a treasure-chest-like etching.")
print("While above the left arrow, you notice a boat-like etching.")

counter = 3

while(counter != 0):
    choice1 = input("\nDo you go right or left? "
                    "Type R or L: ").upper()
    if choice1 == "R":
        print("\nYou wander to the right of the sign and "
              "notice a trail between the trees,")
        print("You follow the trail and spot what seems like an "
              "obviously filled-up hole.")
        print("Thinking it holds treasure, you run over to dig it up. "
              "However...")
        print("As you approach, the ground beneath you caves in, "
              "and you fall into a pit with spikes.")
        print("Unfortunately, your short journey ends here...")
        counter = 0
    elif choice1 == "L":
        counter -= 1
        print("\nYou follow the path to the left and come to a small river.")
        print("The path seems to continue further but there "
              "appears to be another trail across the river.")

        choice2 = input("\nDo you want to continue along the "
                        "path or swim across the river? "
                        "Type C or S: ").upper()
        if choice2 == "S":
            counter -= 1
            print("\nYou decide to swim across the river to reach the other trail.")
            print("Halfway through, the current picks up speed.")
            print("You are swept away by the strong current "
                  "and end up at the entrance of a cavern!")
            print("Looking around, you realize that your only "
                  "remaining path is to enter the cavern.")
            print("As you wander along, the path suddenly splits in two.")
            print("On the left path, you hear the faint sound "
                  "of water dripping into a puddle, but it's very dark.")
            print("While on the right path, you notice a "
                  "dim light reflecting off the walls of the cave.")

            choice3 = input("\nDo you enter the right path or left path? "
                            "Type RP or LP: ").upper()
            if choice3 == "RP":
                print("\nYou enter the right path and continue walking for a few minutes.")
                print("The light gets brighter!")
                print("Eventually, you exit the cave and end up on another beach.")
                print("You notice a small boat in the distance and run toward it.")
                print("Without hesitation, you jump into the boat and find the oars.")
                print("You set sail from the island, empty-handed "
                      "and with no idea where you're going.")
                print("As you aimlessly drift at sea, the blistering sun beats down upon you, "
                      "starvation and dehydration set it.")
                print("Exhausted, you pass out. Suddenly, you hear a loud blaring horn.")
                print("You quickly awake to see a giant ship infront of you, "
                      "with crewmembers throwing down a life raft.")
                print("You are pulled aboard the ship. "
                      "The crew members give you food and water. You're saved!")
            elif choice3 == "LP":
                print("\nYou enter the dark cave to the left and trace your fingers "
                      "along the walls to guide yourself through the darkness.")
                print("As you continue walking, the dripping sound becomes louder and louder.")
                print("Eventually, you feel water dripping onto your head.")
                print("You continue walking and feel water against your feet.")
                print("The walk a bit further and suddenly slip into deep water.")
                print("You try to swim but the water seems to have a strong " 
                      "vortexing current that pulls you down under.")
                print("You try to forcibly swim up to the surface but are unable to. " 
                      "You eventually run out of air and pulled deep down below.")
                print("Never to be found again.")
                counter = 0
            else:
                print("\nInvalid Selection.")
                counter = 0
                break
        
        elif choice2 == "C":
            print("\nYou continue along the path and find what "
                  "seems like an obviously filled-up hole.")
            print("You find an old rusty shovel poorly hidden by a nearby tree. "
                  "Excited by the thought of treasure, you run over to try and dig up the hole.")
            print("You dig for an hour and suddenly gear a loud 'clunk' sound. " 
                  "You found a buried treasure chest!")
            print("You haul the chest back to the beach where "
                  "you first arrived and spot an old boat.")
            print("You throw the chest into the boat and push off from the island " 
                  "with no idea where you're going.")
            print("As you aimlessly drift at sea, the blistering sun beats down upon you, " 
                  "starvation and dehydration set it.")
            print("Exhausted, you pass out. Suddenly, you hear a loud blaring horn.")
            print("You quickly awake to see a giant ship infront of you, with crewmembers " 
                  "throwing down a life raft.")
            print("You are pulled aboard the ship while clinging to the chest. " 
                  "The crew members give you food and water.")
            print("You eventually gather your strength and enter a room prepared for you. " 
                  "You open the chest to find large ancient gold coins and jewels!")
            counter += 1
        else:
            print("\nInvalid Selection.")
            counter = 0
            break
    else:
        print("\nInvalid Selection.")
        counter = 0
        break

    if counter == 0:
        print("\nGame Over...\n")
        break
    elif counter == 3:
        print("\nCongratulations! You found the treasure!\n")
        break
    else:
        print("\nCongratulations! You Survived!\n")
        break
