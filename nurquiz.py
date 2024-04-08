# Quiz App - Tutorial for Learn IT

# Questions and possible answers as well as the define for which answer is correct. Make note of the formatting and placement of symbols
questions = [
    {
        "question": "What does BMW stand for?",
         "options": ["A:Bavaria Motor Works", "B: Beautiful Mechanical Wonders", "C:Best Motorsport Weapon","D:Barbarian Motor Works " ],
         "answer": "A"
    },{
        "question": "How many cylinders does a V8 motor have?",
        "options": ["A:6", "B:14", "C:8", "D:4"],
        "answer": "C"
    }, {
        "question": "What does RPM stand for in cars?",
        "options": ["A: Revolutions Per Minute", "B: Rapid Power Mechanism", "C: Racing Performance Mode", "D: Roadway Power Management"],
        "answer": "A"
    },  {
        "question": "What does MPG stand for in cars?",
        "options": ["A: Miles Per Gallon", "B: Miles Per Hour", "C: Money and Gasoline Power", "D: Make and Produce Gas"],
        "answer": "B"
    },  {
        "question": "What does 4WD stand for in cars?",
        "options": ["A: Four Wheel Drive", "B: Forward Wheel Drive", "C: Four Window Design", "D: Forceful Wheel Drive"],
        "answer": "A"
    },  {
        "question": "What does GPS help you with while driving?",
        "options": ["A: Entertainment", "B: Fueling", "C: Navigation", "D: Cleaning"],
        "answer": "C"
    },  {
        "question": "What does AC do in a car?",
        "options": ["A: Heats the Engine", "B: Changes the Tire Pressure", "C: Fills the Gas Tank", "D: Cools the Interior"],
        "answer": "D"
    },  {
        "question": "What does Inline 6 refer to in cars?",
        "options": ["A: Gear Shift", "B: Suspension", "C: Fuel Type", "D: Engine Type"],
        "answer": "D"
    },  {
        "question": "What does EV stand for in cars?",
        "options": ["A: Electric Vehicle", "B: Efficient Vehicle", "C: Engine Vehicle", "D: Energy Vessel"],
        "answer": "A"
    },  {
        "question": "What does RWD stand for in cars?",
        "options": ["A: Rear Wheel Drive", "B: Remote Windscreen Defrost", "C: Rapid Wheel Displacement", "D: Race Winning Dynamics"],
        "answer": "A"
    },
    # You can remove this comment or move it down and add more questions. You should enclose each question in their own {} brackets.
]

# This function will define the quiz code on launch
def run_quiz(questions):
    score = 0  # Initialize score to 0 and create a variable "score" to store the value of correct answers

    # Loop through all the questions. This will follow all the questions above until finished
    for question in questions:
        print("\n" + question["question"])  # Print the question
        for option in question["options"]:
            print(option)  # Print all the answer options

        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print("Wrong answer.")

    # Print the final score from the stored variable
    print(f"\nYou got {score} out of {len(questions)} questions correct!")

# Run the quiz
run_quiz(questions)