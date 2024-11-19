from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initialize the board and game status
board = [[' ' for _ in range(3)] for _ in range(3)]
game_over = False

def print_board():
    """Prints the current state of the board."""
    return '\n'.join([' | '.join(row) for row in board])

def check_winner(player):
    """Checks if the given player has won."""
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def minimax(board, depth, is_maximizing_player):
    """Minimax algorithm to find the best move for the AI."""
    if check_winner('O'):
        return 10 - depth
    if check_winner('X'):
        return depth - 10
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return 0  # Draw
    
    if is_maximizing_player:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = ' '
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = ' '
        return best

def find_best_move():
    """Finds the best move for the AI based on the Minimax algorithm."""
    best_val = -float('inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'  # AI's move
                move_val = minimax(board, 0, False)
                board[i][j] = ' '  # Undo move
                
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
                    
    return best_move

@app.route('/')
def index():
    return render_template('index.html', board=board, game_over=game_over)

@app.route('/play', methods=['POST'])
def play():
    global game_over
    row = int(request.form['row'])
    col = int(request.form['col'])
    
    if board[row][col] == ' ' and not game_over:
        # Human's move
        board[row][col] = 'X'
        
        if check_winner('X'):
            game_over = True
            return jsonify({'message': 'You win!', 'board': board, 'game_over': game_over})
        
        # AI's move
        ai_move = find_best_move()
        board[ai_move[0]][ai_move[1]] = 'O'
        
        if check_winner('O'):
            game_over = True
            return jsonify({'message': 'AI wins!', 'board': board, 'game_over': game_over})
        
        # Check for draw
        if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            game_over = True
            return jsonify({'message': 'It\'s a draw!', 'board': board, 'game_over': game_over})
    
    return jsonify({'message': '', 'board': board, 'game_over': game_over})

@app.route('/restart', methods=['POST'])
def restart():
    """Resets the game."""
    global board, game_over
    board = [[' ' for _ in range(3)] for _ in range(3)]
    game_over = False
    return jsonify({'message': 'Game restarted!', 'board': board, 'game_over': game_over})

if __name__ == "__main__":
    app.run(debug=True)
