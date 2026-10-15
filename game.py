room = 'starting'
keys = 0
game_running = True

while game_running == True:
    if room == 'starting':
        print("You find yourself in an empty, dark room. There's the distinct smell of damp wood emanating from the decaying floor. Moss climbs years-old cracks in the stone wall as you look around the dingy room.")
        print("Looking around, you notice a total of four doors, one on each wall. The door directly in front of you looks as though it's been installed more recently than the others, it's reddish mahogany wood shining slightly in comparison to the three other doors around you. The door before you has three keyholes.")
        print("You decide to explore the dilapidated building, where do you start?")
        print("Press 1 to attempt to enter the door on your left, 2 to try enter the door in front of you, 3 to try enter the door to your right, and 4 to try enter the door behind you.")

        answer = input("1-4: ")

        if answer == "1":
            room = "left"
        elif answer == "2":
            room = "forward"
        elif answer == "3":
            room = "right"
        elif answer == "4":
            room = "back"
        else:
            print("Invalid number.")

        if room == 'forward':
            if keys >= 3:
                print("Congrats! You escaped!")
                game_running = False
                
            else:
                print("You push the door but it won't budge, maybe you need one key for each of the three keyholes? You currently only have " + str(keys) + "!")
                room = 'starting'

        if room == 'left':
            print("The room is completely empty save for a small notebook on a coffee table right in the center of it. Getting closer, you see that the notebook has a question on it.")
            print("Enter 1 to answer the question, enter 2 to go back into the main room.")

            answer = input("1-2: ")

            if answer == "1":
                room = 'knowledge'

            if answer == "2":
                room = 'starting'

            else:
                print("Invalid number.")

        if room == 'knowledge':
            print("The beat-up notebook in front of you has only a simple question:")
            print("What is the chemical formula for salt?")
            print("Choose your answer below:")
            print("a: CO2")
            print("b: NaCl")
            print("c: H2O")
            print("d: C11H22O11")

            answer = input("a-d: ").lower()

            if answer == "a" or answer == "c" or answer == "d":
                print("You write it in the notebook, but nothing happens.")

            elif answer == "b":
                print("The ink on the paper begins to glow before exploding in a flurry of fine glitter. In the midst of all the glitter, you notice a golden key hovering above the notebook and snatch it out of the air.")
                keys += 1
                room = 'starting'

            else:
                print("Invalid number.")
        
        elif room == 'right':
            print("The room you step into has only a chalkboard hung on the wall. The ground is coated with a thin blanket of dust that's disturbed as you edge closer to the blackboard. You notice a small riddle scrawled in the top corner in white chalk:")
            print("If you have me, you will want to share me. If you share me, you will no longer have me. What am I?")
            print("Choose your answer:")
            print("a: food")
            print("b: niche games")
            print("c: a secret")
            print("d: your soul")

            answer = input("a-d: ")

            if answer == "a" or answer == "b" or answer == "d":
                print("You write your answer on the chalkboard, but nothing happens.")

            elif answer == "c":
                print("The blackboard seems to dissapear as you write the final letter of your answer on it, revealing a hole in the wall. Reaching into the hole, you feel the cold metal of a key and instinctively grab it, shoving it into your pocket.")
                keys += 1
                room = 'starting'

            else:
                print("Invalid number.")

        if room == 'back':
            print("You step into a dark room with shattered pieces of glass littered across the floor. There are two staircases in the small square-shaped room, one on your left, which goes up, and one on your right, which goes down.")
            print("What do you want to do?")
            print("Press 1 to go up the left stairway, 2 to return to the previous room, and 3 to go down the right stairway.")

            answer = input("1-4: ")

            if answer == "1":
                room = 'upstairs'

            if answer == "2":
                room = 'starting'

            if answer == "3":
                room = 'downstairs'

            else:
                print("Invalid number.")

        if room == 'upstairs':
            print("All that awaits you upstairs is a grotty attic with a single key laying atop a cardboard box. Being careful of the obviously weak floorboards, you make your way over to it and place the key into your pocket before cautiously making your way back downstairs.")
            print("Do you take the key?")
            print("Press 1 to take it, press 2 to turn back.")

            answer = input("1-2: ")

            if answer == "1":
                print("You grabbed the key and made your way back downstairs.")
                keys += 1
                room = 'back'

            if answer == "2":
                print("You made your way back downstairs without the key.")
                room = 'back'

            else:
                print("Invalid number.")

        if room == 'downstairs':
            print("You enter a dark cellar, coughing slightly as you inhale air that's likely been untouched for eons now. The floor is a solid concrete unlike the other rooms and it's far too cold. It feels almost as though it's a walk-in freezer. You shiver, and you can't quite tell if it's due to the temperature, or due to the distinct feeling of being watched.")
            print("What do you do?")
            print("Press 1 to go deeper, press 2 to go back.")

            answer = input("1-2: ")

            if answer == "1":
                room = 'downstairs2'

            if answer == "2":
                room = 'back'

            else:
                print("Invalid number.")

        if room == 'downstairs2':
            print("The feeling of impending doom only gets worse and worse the further you go. You feel as though the air has thickened to the point it's difficult to breathe. Each single breath feels as though it could alert some otherworldly being to your presence, as though you'd exhale your soul if you weren't careful. You think you see a shadow and turn to look at it, only to be met with nothing but darkness.")
            print("What do you do?")
            print("Press 1 to go deeper, press 2 to go back.")

            answer = input("1-2: ")

            if answer == "1":
                room = 'downstairs3'

            if answer == "2":
                room = 'back'

            else:
                print("Invalid number.")

        if room == 'downstairs3':
            print("A leather journal sits on the ground in front of you, a single torch on the ground next to it illuminating the worn paper.")
            print("What do you do?")
            print("Press 1 to read the journal, press 2 to go back.")

            if answer == "1":
                room = 'finaljournal'

            if answer == "2":
                room = 'back'

            else:
                print("Invalid number.")

        if room == 'finaljournal':
            print("You open the notebook to the middle page, where there are only three words written:")
            print("I see you.")
            print("You turn around swiftly, but you're too late, it's already caught you.")
            print("You got the bad ending.")
            game_running = False
        

        