import sqlite3

conn = sqlite3.connect('quiz.db')

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, "
               "answer1 TEXT, answer2 TEXT, answer3 TEXT, answer4 TEXT)")

conn.commit()

mode = input("Willkommen bei QuizPY! Schreib '1' für den Quiz-Modus, um direkt anzufangen mit dem Quiz oder '2' falls du zusätzliche Fragen hinzufügen möchtest!\n")

if mode == '1':
    print()
elif mode == '2':
    print()
elif mode == 'q':
    print()
else:
    print()

def quiz():
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()

    i = 0
    while i < 10:
        print()
