from flask import Flask, render_template, request
from db import save_attempt
from gemini import get_character, CHARACTER_IMAGES  # Import image mapping

app = Flask(__name__)

QUESTIONS = [
    "How do you react when something strange or dangerous happens?",
    "What motivates you the most?",
    "In a group of friends, what role do you naturally take?",
    "How do you usually solve problems?",
    "What is your biggest strength?",
    "How do you handle fear?",
    "If a friend is in serious trouble, what would you do?",
    "What kind of person are you under pressure?",
    "Which environment do you feel most comfortable in?",
    "If you had special abilities or skills, how would you use them?"
]

MCQ_OPTIONS = [
    [
        "I stay calm and try to protect everyone",
        "I immediately think of a plan",
        "I get scared but don’t abandon my friends",
        "I rush in without thinking twice"
    ],
    [
        "Protecting the people I care about",
        "Curiosity and discovering the truth",
        "Friendship and loyalty",
        "Doing what feels morally right"
    ],
    [
        "The leader who makes decisions",
        "The brain who figures things out",
        "The emotional support",
        "The comic relief"
    ],
    [
        "Logical thinking and planning",
        "Trusting instincts",
        "Asking for help and teamwork",
        "Trial and error"
    ],
    [
        "Courage",
        "Intelligence",
        "Loyalty",
        "Adaptability"
    ],
    [
        "Face it head-on",
        "Suppress it and stay focused",
        "Talk it out with someone I trust",
        "Use humor to cope"
    ],
    [
        "Risk myself to save them",
        "Carefully plan a rescue",
        "Stay with them no matter what",
        "Support them emotionally"
    ],
    [
        "Calm and protective",
        "Focused and analytical",
        "Emotional but determined",
        "Sarcastic but reliable"
    ],
    [
        "Somewhere safe with people I trust",
        "A place full of puzzles and mysteries",
        "Anywhere my friends are",
        "Somewhere I can be myself freely"
    ],
    [
        "To protect others",
        "To understand how things work",
        "To help my friends",
        "To fight injustice"
    ]
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        qa_pairs = []

        for i, q in enumerate(QUESTIONS, start=1):
            selected = request.form[f"q{i}"]
            qa_pairs.append((q, selected))

        # Call Gemini AI
        character = get_character(qa_pairs)

        # Get image path for the character
        character_image = CHARACTER_IMAGES.get(character, None)

        # Save to database
        save_attempt(name, str([a for _, a in qa_pairs]), character)

        return render_template(
            "result.html",
            name=name,
            character=character,
            character_image=character_image
        )

    return render_template("index.html", questions=QUESTIONS, mcq_options=MCQ_OPTIONS)

if __name__ == "__main__":
    app.run(debug=True)
