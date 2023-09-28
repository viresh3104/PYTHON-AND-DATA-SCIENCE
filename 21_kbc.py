import random

questions = [
    {
        "question" : "who is india's first prime minister?",
        "options"  : ["1.neheru", "2.modi","3.rajiv gandi","4.none"],
        "correct_answer" : "1"
    },

    {
        "question" : "what is rank of india in population ranking?",
        "options"  : ["1.first","2.second","3.third","4.foruth"],
        "correct_answer" : "1"
    },

    {
        "question": "which country has the highest number of total area?",
        "options":["1.india","2.pakistan","3.bangladesh","4.china"],
        "correct_answer":"1"
    },
    
    {
        "question": "how many states are there in india?",
        "options":["1.27","2.28","3.29","4.30"],
        "correct_answer":"2"
    },

    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["1.Earth", "2.Mars", "3.Jupiter", "4.Venus"],
        "correct_answer": "2"
    },

    {
        "question": "What is the largest mammal in the world?",
        "options": ["1.Elephant", "2.Blue Whale", "3.Giraffe", "4.Kangaroo"],
        "correct_answer": "2"
    },

    {
        "question": "What is the currency of Japan?",
        "options": ["1.Dollar", "2.Euro", "3.Yen", "4.Rupee"],
        "correct_answer": "3"     
    },

    {
        "question": "What is the capital of France?",
        "options": ["1.London", "2.Berlin", "3.Paris", "4.Madrid"],
        "correct_answer": "3"
    },

    {
        "question": "who handles ministry of external affiars?",
        "options" : ["1.piyush goyal","2.jay shankar","3.arjun munda","4.krishna"],
        "correct_answer" : "2"
    },

    {
        "question" : "who is finance minister of india?",
        "options" : ["1.nirmala sitaraman","2.yogi","3.kejriwal","4.nitin gaadkari"],
        "correct_answer" : "1"
    },

    {
        "question" : "who is defence minister of inidia?",
        "options"  : ["1.pankaj singh", "2.j.p nadda","3.rajnath singh","4.smriti irani"],
        "correct_answer" : "3"
    }
]

z = input("enter your name to play the game:")
print(z)
print(f"{z} chaliye shuru krte hai")
def ask_question(questions_dict):
    print(f"{z} here`s your question")
    print(questions_dict["question"])
    for option in questions_dict["options"]:
        print(option)
    user_answer = input(f"enter your answer {z}: ")   
    if user_answer == questions_dict["correct_answer"]:
        print("Correct!\n")
        return True
    else:
        print(f"Sorry, the correct answer was {questions_dict['correct_answer']}.\n")
        return False
    

def play_game():
    print("Welcome to Kaun Banega Crorepati!")
    print("You need to answer 11 questions to win the game.")
    
    money_won = 0

    for i in range(11):
        print(f"\nQuestion {i+1}:")
        if ask_question(random.choice(questions)):
            money_won += 1000000

    print(f"\ndeviyo aur sajjano {z} mahoday ne jeet liye hai {money_won} rupay. \ntoh kya karenge {z} sahab is dhanrashi ka?")
    print(f"Thank you {z} for playing KBC")

if __name__ == "__main__":
    play_game()


