# Minesweeper-Microservice
A Python-based microservice for the Minesweeper game


To create a Minesweeper game microservice that runs on Ubuntu and is accessible via a browser, you'll need to set up a web server using Python's Flask framework. Flask will serve as the backend, and you can use HTML and JavaScript to render the Minesweeper game in the browser.



#### Step 1: Install Flask on Ubuntu

1. **Install Flask**  
   First, make sure you have `pip` and `Flask` installed on your system:


   ```bash
   sudo apt-get install python3-pip
   pip3 install Flask
   
   ```

#### Step 2: Set Up the Minesweeper Game Logic

1. **Create a Python file for the game logic**  
   Create a file `minesweeper.py` where the core game logic will reside:

   ```bash
   touch minesweeper.py
   
   ```

3. **Implement the Game Logic**  
   In the `minesweeper.py` file, define the Minesweeper class. This logic will remain server-side.

```
nano minesweeper.py
```

```python
import random

class Minesweeper:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.mine_positions = []
        self._place_mines()
        self._calculate_numbers()

    def _place_mines(self):
        mines_left = self.mines
        while mines_left > 0:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if self.grid[row][col] != 'M':
                self.grid[row][col] = 'M'
                self.mine_positions.append((row, col))
                mines_left -= 1

    def _calculate_numbers(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 'M':
                    continue
                count = 0
                for r in range(row - 1, row + 2):
                    for c in range(col - 1, col + 2):
                        if 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == 'M':
                            count += 1
                self.grid[row][col] = str(count) if count > 0 else ' '

    def get_grid(self):
        return self.grid
```

#### Step 3: Set Up the Flask Web Application

1. **Create a Flask app file**  
   Create another file called `app.py` where Flask will serve as the web server.

```bash
touch app.py
```

2. **Build the Flask Server**  
   In `app.py`, integrate the Minesweeper class and set up routes to interact with the game via a web interface.

```
   nano app.py
```

```python
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
```
save and exit.


### Step 4: Create the HTML Frontend in `templates/index.html`

1. Open the `index.html` file:

```bash
nano templates/index.html
```

2. Paste the following HTML and JavaScript code:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Minesweeper</title>
    <style>
        table {
            border-collapse: collapse;
            margin: 20px;
        }
        td {
            width: 30px;
            height: 30px;
            text-align: center;
            vertical-align: middle;
            border: 1px solid black;
            font-size: 20px;
            cursor: pointer;
        }
        td.mine {
            background-color: red;
        }
        td.number {
            background-color: lightgray;
        }
    </style>
</head>
<body>
    <h1>Minesweeper</h1>
    <table id="minesweeper-grid"></table>

    <script>
        async function fetchGrid() {
            const response = await fetch('/get_grid');
            const data = await response.json();
            const grid = data.grid;
            const table = document.getElementById('minesweeper-grid');
            table.innerHTML = '';  // Clear previous grid

            grid.forEach((row, rowIndex) => {
                const tr = document.createElement('tr');
                row.forEach((cell, colIndex) => {
                    const td = document.createElement('td');
                    if (cell === 'M') {
                        td.classList.add('mine');
                    } else if (cell !== ' ') {
                        td.classList.add('number');
                        td.innerHTML = cell;
                    }
                    td.addEventListener('click', () => {
                        alert(`Clicked cell at row ${rowIndex + 1}, col ${colIndex + 1}`);
                    });
                    tr.appendChild(td);
                });
                table.appendChild(tr);
            });
        }

        // Fetch grid on page load
        fetchGrid();
    </script>
</body>
</html>
```

3. Save and exit the file.

- **Explanation**:
  - The table represents the Minesweeper grid.
  - The `fetchGrid` function sends a request to the Flask backend to get the grid data and populates the HTML table.
  - Clicking a cell currently shows an alert with its coordinates (you can later expand it to handle moves like revealing or flagging cells).

### Step 5: Run the Application

1. Make sure you’re in the `minesweeper_microservice` directory.
2. Run the Flask server by executing the following command:

```bash
python3 app.py
```
copy the URL reflected and paste it in the browser

### Step 6: View the Game in Your Browser

1. Open your browser.
2. Go to `http://localhost:5000` (or `http://<your-ip>:5000` if running on a remote server).

You should see the Minesweeper grid displayed in your browser. Each cell will be clickable, and the game grid will be displayed based on the backend logic.

### Step 7: Further Enhancements

You can now enhance this basic setup with more functionality:
- **Reveal Mines**: When a cell is clicked, you could reveal whether it is a mine or a number.
- **Flag Mines**: Add right-click functionality to flag a cell.
- **End Game**: Add logic to handle win/lose conditions and reset the game.


By following these steps, you should now have a functioning Minesweeper microservice that runs on Linux and can be accessed via a browser!

![Screenshot 2024-09-07 223025](https://github.com/user-attachments/assets/b4071d5e-4f4b-461b-b8c4-e83c9da23f69)


