# Mini Project: Day Planner

day = input("What day is it? ").strip().lower()
time = input("What time of day? ").strip().lower()

if day == "monday":
    if time == "morning":
        print("Suggestion: Review your goals for the week.")
    elif time == "afternoon":
        print("Suggestion: Finish your homework.")
    elif time == "evening":
        print("Suggestion: Read a book.")
    else:
        print("Sorry, I don't recognize that time. Try: morning, afternoon, or evening.")

elif day == "tuesday":
    if time == "morning":
        print("Suggestion: Practice Python.")
    elif time == "afternoon":
        print("Suggestion: Take a short walk.")
    elif time == "evening":
        print("Suggestion: Watch a coding video.")
    else:
        print("Sorry, I don't recognize that time. Try: morning, afternoon, or evening.")

elif day == "wednesday":
    if time == "morning":
        print("Suggestion: Study for your classes.")
    elif time == "afternoon":
        print("Suggestion: Work on a small project.")
    elif time == "evening":
        print("Suggestion: Relax with a movie.")
    else:
        print("Sorry, I don't recognize that time. Try: morning, afternoon, or evening.")

else:
    print("Sorry, I don't recognize that day. Try: Monday, Tuesday, or Wednesday.")
