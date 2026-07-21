# Mini Project: Day Planner

day = input("What day is it? ").strip().lower()
time = input("What time of day? ").strip().lower()

if day == "monday":
    if time == "morning":
        print("Suggestion: Review your weekly goals.")
    elif time == "afternoon":
        print("Suggestion: Finish your homework.")
    elif time == "evening":
        print("Suggestion: Read a book before bed.")
    else:
        print("Sorry, I don't recognize that time of day.")

elif day == "wednesday":
    if time == "morning":
        print("Suggestion: Practice Python for 30 minutes.")
    elif time == "afternoon":
        print("Suggestion: Take a short walk outside.")
    elif time == "evening":
        print("Suggestion: Watch a tutorial video.")
    else:
        print("Sorry, I don't recognize that time of day.")

elif day == "friday":
    if time == "morning":
        print("Suggestion: Finish your important tasks.")
    elif time == "afternoon":
        print("Suggestion: Meet with friends.")
    elif time == "evening":
        print("Suggestion: Relax and watch a movie.")
    else:
        print("Sorry, I don't recognize that time of day.")

else:
    print("Sorry, I don't recognize that day.")
