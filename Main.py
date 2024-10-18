import sqlite3

conn = sqlite3.connect('quiz.db')

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, "
               "answer1 TEXT, answer2 TEXT, answer3 TEXT, answer4 TEXT)")

cursor.execute("INSERT INTO questions (question, answer1, answer2, answer3, answer4) "
               "VALUES ('Wer war der erste Kaiser Roms?', 'Augustus', 'Marcus Aurelius', 'Nero', 'Julius Caesar')")

conn.commit()

cursor.execute("SELECT * FROM questions")
questions = cursor.fetchall()

for question in questions:
    print(question)
