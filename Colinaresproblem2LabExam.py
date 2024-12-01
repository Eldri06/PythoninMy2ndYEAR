'''
by eldrian gwapo:))
'''
question = []
answer = []

control = True

while control:
    print("----------------------------")
    print("EXAM SSYTEM PROGRAM")
    print("----------------------------")
    print("[A]. Add Question")
    print("[T]. Take The Exam")
    print("[E].End the Exam")
    option = input("Choice: ").strip().upper()

    if option == "A":
        inpQuestion = input("Question: ")
        inpAnswer = input("Answer: ")
        
        question.append(inpQuestion)
        answer.append(inpAnswer)
        input("Press any key or enter to go back to the menu...")
    
    elif option == "T":
        if not question:
            print("No questions available, add questions")
        else:
            print("\n--- Exam Starts Now ---")
            score = 0
            for i in range(len(question)):
                print(f"Question{i + 1}: {question[i]}")
                user_answer = input("Your Answer: ").strip()
                if user_answer.lower() == answer[i].lower():
                    print("\nCorrect!")
                    score += 1
                else:
                    print(f"Wrong. Correct answer: {answer[i]} ")
            print(f"\nToral score: {score}/{len(question)}")
        input("Press any key or enter to go back to the menu...")
    
    elif option == "E":
        print("Program Terminated")
        control = False
    else: 
        print("Invalid nto in the option")

  
        
  

              

    
    