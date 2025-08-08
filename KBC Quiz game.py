questions = [
  ["What is the largest planet in our solar system?", "Earth", "Mars", "Jupiter Saturn", 3],
  ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", "Saturn", 3],
  ["What does CPU stand for?", "Central Power Unit", "Control Processing Unit", "Central Processing Unit", "Computer Personal Unit", "Core Processor Unit", 3],
  ["Who is the founder of Microsoft?", "Mark Zuckerberg", "Bill Gates", "Steve Jobs", "Elon Musk", "Larry Page", 2],
  ["What gas do humans breathe in to survive?", "Carbon Dioxide", "Hydrogen", "Oxygen", "Nitrogen", "Helium", 3],
  ["HTML is used for?", "Designing games", "Programming apps", "Structuring web pages", "Writing emails", "Designing logos", 3],
  ["Which animal is known as the King of the Jungle?", "Tiger", "Bear", "Elephant", "Lion", "Leopard", 4],
  ["How many days are there in a leap year?", "365", "366", "364", "360", "367", 2],
  ["What is H2O commonly known as?", "Salt", "Acid", "Water", "Oxygen", "Hydrogen", 3],
  ["Who invented the light bulb?", "Isaac Newton", "Albert Einstein", "Nikola Tesla", "Thomas Edison", "Galileo", 4],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

print("🎮 Welcome to KBC Quiz Game!")
print("📜 Rules: Choose the correct option (1-5) or enter 0 to quit at any point.\n")

for i in range(len(questions)):
    question = questions[i]
    print(f"\nQuestion {i+1} for $. {levels[i]}")
    print(f"{question[0]}")
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    try:
        reply = int(input("👉 Enter your answer (1-5) or 0 to quit: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number between 1 and 5.")
        continue

    if reply == 0:
        money = levels[i - 1] if i > 0 else 0
        print("\n🛑 You chose to quit the game.")
        break

    if reply == question[-1]:
        print(f"✅ Correct! You've won Rs. {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
    else:
        print("❌ Wrong answer!")
        print(f"The correct answer was: Option {question[-1]}")
        break

print(f"\n💰 Your total winnings: Rs. {money}")
print("🎉 Thanks for playing KBC Quiz Game!")
