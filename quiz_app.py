name = input("Enter your name: ")
print(f"Welcome to the quiz, {name}")
score = 0
while True:
    print("1. Python")
    print("2. General Knowledge")
    print("3. Science")
    category = input("Choose a category(1/2/3): ")

    if category == '1':
        print("1. What keyword is used to define a function in Python?")
        print("a) func   b) def   c) function   d) define")
        answer = input("Your answer: ")
        if answer.lower() == 'b':
            print("Correct!")
            score += 1
        else:
            print("Wrong answer! The correct answer is 'def'.")
        
        print("2. Which data type stores text?")
        print("a) int   b) str   c) float   d) bool")
        answer = input("Your answer: ")
        if answer.lower() == 'b':
            print("Correct!")
            score += 1
        else:
            print("Wrong answer! The correct answer is 'str'.")
        
        print("3. What symbol is used for comments in Python?")
        print("a) //   b) #   c) /*   d) <!--")
        answer = input("Your answer: ")
        if answer.lower() == 'b':
            print("Correct!")
            score += 1
        else:
            print("Wrong answer! The correct answer is '#'.")

        print("4. What is the index of the first element in a list?")
        print("a) 0   b) 1   c) -1   d) 2")
        answer = input("Your answer: ")
        if answer.lower() == 'a':
            print("Correct!")
            score += 1
        else:
            print("Wrong answer! The correct answer is '0'.")

    elif category == '2':
        print("1. What is the capital of France?")
        print("a) Berlin   b) Madrid   c) Paris   d) Rome")
        answer = input("Your answer: ")
        if answer.lower() == 'c':
            print("Correct!")
            score += 1
        else:
            print("Wrong answer! The correct answer is 'Paris'.")
        
        print("2. Who is the current president of the United States?")
        print("a) Joe Biden   b) Donald Trump   c) Barack Obama   d) George Bush")
        answer = input("Your answer: ")
        if answer.lower() == 'a':
            print("Correct!")
            score += 1
        else:
            print("Wrong answer! The correct answer is 'Joe Biden'.")
        
        print("3. What is the largest ocean on Earth?")
        print("a) Atlantic Ocean   b) Indian Ocean   c) Arctic Ocean   d) Pacific Ocean")
        answer = input("Your answer: ")
        if answer.lower() == 'd':
            print("Correct!")
            score += 1
        else:
            print("Wrong answer! The correct answer is 'Pacific Ocean'.")
        
        print("4. Which country is known as the Land of the Rising Sun?")
        print("a) China   b) Japan   c) South Korea   d) Thailand")
        answer = input("Your answer: ")
        if answer.lower() == 'b':
            print("Correct!")
            score += 1
        else:
            print("Wrong answer! The correct answer is 'Japan'.")
        
    elif category == '3':
        print("1. What is the chemical symbol for water?")
        print("a) H2O   b) CO2   c) O2   d) NaCl")
        answer = input("Your answer: ")
        if answer.lower() == 'a':
            print("Correct!")
            score += 1
        else:
            print("Wrong answer! The correct answer is 'H2O'.")
        
        print("2. What planet is known as the Red Planet?")
        print("a) Venus   b) Mars   c) Jupiter   d) Saturn")
        answer = input("Your answer: ")
        if answer.lower() == 'b':
            print("Correct!")
            score += 1
        else:
            print("Wrong answer! The correct answer is 'Mars'.")
        
        print("3. What is the process by which plants make their food?")
        print("a) Photosynthesis   b) Respiration   c) Digestion   d) Fermentation")
        answer = input("Your answer: ")
        if answer.lower() == 'a':
            print("Correct!")
            score += 1
        else:
            print("Wrong answer! The correct answer is 'Photosynthesis'.")
        
        print("4. What is the largest organ in the human body?")
        print("a) Heart   b) Liver   c) Skin   d) Brain")
        answer = input("Your answer: ")
        if answer.lower() == 'c':
            print("Correct!")
            score += 1
        else:
            print("Wrong answer! The correct answer is 'Skin'.")

    else:
        print("Invalid category selected!")

    print(f"Your final score is: {score}/4")

    print("Do you want to play again? (yes/no)")
    play_again = input("Your answer: ")
    if play_again.lower() != 'yes':
        print("Thank you for playing the quiz!")
        break
    else:
        score = 0