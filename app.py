from flask import Flask
from flask import render_template
import game_of_life

app = Flask(__name__)

game_of_life.GameOfLife(25, 25).generate_universe()


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/live')
@app.route('/live/')
def live():
    game = game_of_life.GameOfLife()
    game.form_new_generation()
    game.count += 1
    return render_template('live.html', object=game, count=game.count)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
