from flask import Flask, jsonify, render_template
from minesweeper import Minesweeper

app = Flask(__name__)

# Global game instance
game = Minesweeper(8, 8, 10)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_grid', methods=['GET'])
def get_grid():
    grid = game.get_grid()
    return jsonify({"grid": grid})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
