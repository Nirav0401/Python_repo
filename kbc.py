questions = [
    ["The sum of 4 and 5", 9, 7, 4, 10, "None", 1],

    ["The mult of 4 and 5", 20, 2, 7, 10, "None", 1],

    ["The div of 40 and 5", 8, 7, 4, 10, "None", 1],

    ["The subtract of 14 and 5", 9, 7, 19, 52, "None", 1],

    ["The phone has how many keys?", 9, 7, 91, 10, "None", 1],

    ["How many letters does abcd have?", 26, 4, 25, 10, "None", 1]
]
levels = [10000, 20000, 50000, 100000, 120000, 150000]
money=0
for i in range(0, len(questions)):
    question = questions[i]
    
    print(f"\nQuestion for Rs. {levels[i]}")
    print(question[0])
    print(f"a. {question[1]}     b. {question[2]}")
    print(f"c. {question[3]}     d. {question[4]}")
    reply = int(input("Enter the answer between (1-4) or 0 for quit:\n"))
    if(reply==0):
        money = levels[i-1]
        break
    if(reply==question[6]):
        print(f"Correct answer! You won Rs. {levels[i]}")
        if(i==1):
            money = 20000   
        elif(i==3):
            money = 100000     
        elif(i==5):
            money = 150000   
    else:
        print("Wrong answer")
        break
print(f"Your take home Rs. {money}")        



