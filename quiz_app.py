import tkinter as tk
import random

questions = [

    # EASY
    {"question": "Capital of Pakistan?", "options": ["Karachi", "Lahore", "Islamabad", "Quetta"], "answer": "Islamabad", "difficulty": "easy"},
    {"question": "5 + 3 = ?", "options": ["6", "7", "8", "9"], "answer": "8", "difficulty": "easy"},
    {"question": "Which planet is known as Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars", "difficulty": "easy"},
    {"question": "Which keyword is used for loop in Python?", "options": ["while", "loop", "repeat", "iterate"], "answer": "while", "difficulty": "easy"},
    {"question": "HTML stands for?", "options": ["Hyper Text Markup Language", "High Text Machine Language", "None", "Hyper Tool"], "answer": "Hyper Text Markup Language", "difficulty": "easy"},
    {"question": "Which symbol is used for comments in Python?", "options": ["//", "#", "<!-- -->", "**"], "answer": "#", "difficulty": "easy"},
    {"question": "10 - 4 = ?", "options": ["5", "6", "7", "8"], "answer": "6", "difficulty": "easy"},
    {"question": "Which device is used to input data?", "options": ["Monitor", "Keyboard", "Printer", "Speaker"], "answer": "Keyboard", "difficulty": "easy"},
    {"question": "Which language is used for web pages?", "options": ["HTML", "Python", "C++", "Java"], "answer": "HTML", "difficulty": "easy"},
    {"question": "2 * 3 = ?", "options": ["5", "6", "7", "8"], "answer": "6", "difficulty": "easy"},

    # MEDIUM
    {"question": "Python is ___ language?", "options": ["Low-level", "High-level", "Machine", "Assembly"], "answer": "High-level", "difficulty": "medium"},
    {"question": "Which data type is mutable?", "options": ["Tuple", "String", "List", "Integer"], "answer": "List", "difficulty": "medium"},
    {"question": "FIFO used in?", "options": ["Stack", "Queue", "Tree", "Graph"], "answer": "Queue", "difficulty": "medium"},
    {"question": "Which operator is used for power?", "options": ["^", "**", "*", "//"], "answer": "**", "difficulty": "medium"},
    {"question": "len('Hello') = ?", "options": ["4", "5", "6", "Error"], "answer": "5", "difficulty": "medium"},
    {"question": "Which keyword is used for condition?", "options": ["if", "loop", "switch", "case"], "answer": "if", "difficulty": "medium"},
    {"question": "Which data structure allows duplicates?", "options": ["Set", "List", "Dictionary", "None"], "answer": "List", "difficulty": "medium"},
    {"question": "Which loop runs until condition false?", "options": ["for", "while", "loop", "repeat"], "answer": "while", "difficulty": "medium"},
    {"question": "Which function prints output?", "options": ["echo()", "print()", "show()", "display()"], "answer": "print()", "difficulty": "medium"},
    {"question": "15 / 3 = ?", "options": ["3", "4", "5", "6"], "answer": "5", "difficulty": "medium"},

    # HARD
    {"question": "Binary Search Complexity?", "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"], "answer": "O(log n)", "difficulty": "hard"},
    {"question": "Linear Search Complexity?", "options": ["O(1)", "O(log n)", "O(n)", "O(n^2)"], "answer": "O(n)", "difficulty": "hard"},
    {"question": "Which sorting is fastest (avg)?", "options": ["Bubble", "Selection", "Quick Sort", "Insertion"], "answer": "Quick Sort", "difficulty": "hard"},
    {"question": "Access array element time?", "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], "answer": "O(1)", "difficulty": "hard"},
    {"question": "Which is not programming language?", "options": ["Python", "HTML", "Java", "C++"], "answer": "HTML", "difficulty": "hard"},
    {"question": "Stack follows?", "options": ["FIFO", "LIFO", "Both", "None"], "answer": "LIFO", "difficulty": "hard"},
    {"question": "Queue follows?", "options": ["LIFO", "FIFO", "Both", "None"], "answer": "FIFO", "difficulty": "hard"},
    {"question": "Which is dynamic structure?", "options": ["Array", "List", "Tuple", "String"], "answer": "List", "difficulty": "hard"},
    {"question": "Which operator gives remainder?", "options": ["/", "//", "%", "**"], "answer": "%", "difficulty": "hard"},
    {"question": "Recursion uses?", "options": ["Loop", "Function calling itself", "Array", "Condition"], "answer": "Function calling itself", "difficulty": "hard"}
]
# global variables
score = 0
q_index = 0
selected_questions = []
attempts = []

#GUI
root = tk.Tk()
root.title("Smart Quiz System")
root.geometry("550x450")

question_var = tk.StringVar()   #question show karny ka liya
selected_option = tk.StringVar()   #user ka selected answer
difficulty_var = tk.StringVar(value="easy")  #selected level (easy/medium/hard)

#POPUP
def show_popup(title, message):   #Messages show karta hai (result, warning, analysis)
    popup = tk.Toplevel(root)
    popup.title(title)
    popup.geometry("550x450")

    tk.Label(popup, text=title, font=("Arial", 18, "bold")).pack(pady=20)
    tk.Label(popup, text=message, font=("Arial", 12), wraplength=500, justify="center").pack(pady=20)
    tk.Button(popup, text="Close", command=popup.destroy, bg="red", fg="white").pack(pady=20)

# LOGIC
def start_quiz():
    global selected_questions, q_index, score

    score = 0
    q_index = 0

    level = difficulty_var.get()

    selected_questions = [q for q in questions if q["difficulty"] == level]  # Sirf selected level ke questions filter hote hain
    random.shuffle(selected_questions)

    show_question()

def show_question():
    global q_index

    if q_index < len(selected_questions):
        q = selected_questions[q_index]
        question_var.set(f"Q{q_index+1}: {q['question']}")  #Current question pick hota hai
        selected_option.set("")  #Question label update hota hai

        for i, opt in enumerate(q["options"]):
            radio_buttons[i].config(text=opt, value=opt) # Options buttons update hote hain
    else:
        finish_quiz()

def next_question():
    global q_index, score

    if selected_option.get() == "":
        show_popup("Warning", "Please select an answer")
        return

    current_q = selected_questions[q_index]

    if selected_option.get() == current_q["answer"]:
        score += 2
    else:
        score -= 1

    q_index += 1
    show_question()

def finish_quiz():
    attempts.append(score)
    show_popup("Quiz Finished", f"Your Score: {score}")

def show_analysis():
    if not attempts:
        show_popup("Info", "No attempts yet!")
        return

    last_score = attempts[-1]

    if last_score >= 15:
        level = "Advanced"
        feedback = "Excellent "
    elif last_score >= 8:
        level = "Intermediate"
        feedback = "Good "
    else:
        level = "Beginner"
        feedback = "Needs improvement "

    avg = sum(attempts)/len(attempts)

    msg = f"Last Score: {last_score}\n\nLevel: {level}\nFeedback: {feedback}\n\nAttempts: {len(attempts)}\nAverage Score: {round(avg,2)}"
    show_popup("Performance Analysis", msg)

def show_leaderboard():
    if not attempts:
        show_popup("Leaderboard", "No data yet!")
        return

    top_scores = sorted(attempts, reverse=True)[:5]

    text = " Top Scores:\n\n"
    for i, s in enumerate(top_scores, 1):
        text += f"{i}. {s}\n"

    show_popup("Leaderboard", text)

#  UI 
tk.Label(root, text="Smart Quiz System", font=("Arial", 18, "bold")).pack(pady=10)

tk.Label(root, text="Select Difficulty").pack()
tk.OptionMenu(root, difficulty_var, "easy", "medium", "hard").pack()

tk.Button(root, text="Start Quiz", command=start_quiz, bg="green", fg="white").pack(pady=10)

tk.Label(root, textvariable=question_var, wraplength=450, font=("Arial", 12)).pack(pady=10)

radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=selected_option, value="")
    rb.pack(anchor="w")
    radio_buttons.append(rb)

tk.Button(root, text="Next", command=next_question, bg="blue", fg="white").pack(pady=10)

tk.Button(root, text="Performance Analysis", command=show_analysis, bg="orange").pack(pady=5)
tk.Button(root, text="Leaderboard", command=show_leaderboard, bg="purple", fg="white").pack(pady=5)

root.mainloop()