from flask import Flask, request, redirect, render_template
from princess import PrincessQuiz

app = Flask(__name__)

princess_quiz = PrincessQuiz(0, 0, 0, 0)

IMG_DIR = './static'

@app.route('/')
def hello_princess_world():
    """a simple HTTP print"""
    return 'hello princess world!'

@app.route('/image')
def serve_image():
    "a simple HTTP image"
    return render_template('image.html')

@app.route('/quiz')
def quiz():
    """prints the current values for princess quiz"""
    return list(princess_quiz.personalities.items())

@app.route('/reset')
def reset():
    """resets the current values of princess quiz"""
    princess_quiz.clear()
    return 'the princess quiz has been reset!'

@app.route('/question/1', methods = ['GET', 'POST'])
def first_question():
    """What quality do you think is most important in a princess?"""
    answers = ['adventure', 'kindness', 'wisdom', 'courage']

    if request.method == 'GET':
        return render_template('question_1.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            princess_quiz.add('Ariel')
        if selected == answers[1]:
            princess_quiz.add('Cinderella')
        if selected == answers[2]:
            princess_quiz.add('Belle')
        if selected == answers[3]:
            princess_quiz.add('Mulan')

        return redirect('/question/2')

@app.route('/question/2', methods = ['GET', 'POST'])
def second_question():
    """What place do you feel most at home in?"""
    answers = ['sea', 'forest', 'library', 'battlefield']

    if request.method == 'GET':
        return render_template('question_2.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            princess_quiz.add('Ariel')
        if selected == answers[1]:
            princess_quiz.add('Cinderella')
        if selected == answers[2]:
            princess_quiz.add('Belle')
        if selected == answers[3]:
            princess_quiz.add('Mulan')

        return redirect('/question/3')

@app.route('/question/3', methods = ['GET', 'POST'])
def third_question():
    """Which activity do you beleive you would enjoy the most?"""
    answers = ['singing', 'Cooking', 'reading', 'archery']

    if request.method == 'GET':
        return render_template('question_3.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            princess_quiz.add('Ariel')
        if selected == answers[1]:
            princess_quiz.add('Cinderella')
        if selected == answers[2]:
            princess_quiz.add('Belle')
        if selected == answers[3]:
            princess_quiz.add('Mulan')

        return redirect('/result')

@app.route('/result')
def get_result():
    """presents the princess quiz results"""
    if princess_quiz.get_personality() == 'Mulan':
        return render_template('mulan.html')
    return 'Congratulations! You have the personality of ' + princess_quiz.get_personality()

if __name__ == '__main__':
    app.run(host='localhost', port=7558)