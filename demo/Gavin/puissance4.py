import tkinter as tk
from tkinter import messagebox

class Puissance4:
    def __init__(self, root):
        self.root = root
        self.root.title("Puissance 4")
        self.current_player = 1  # 1 pour le joueur 1 et 2 pour le joueur 2
        self.players = ["", ""]  # Liste pour stocker les noms des joueurs
        self.board = [[0] * 7 for _ in range(6)]  # Créer une grille 6x7

        self.create_widgets()

    def create_widgets(self):
        # Créer une frame pour les entrées des joueurs
        frame = tk.Frame(self.root)
        frame.grid(row=0, column=0, padx=10, pady=10, columnspan=7)

        self.label_j1 = tk.Label(frame, text="Prénom du Joueur 1:")
        self.label_j1.grid(row=0, column=0, padx=5, pady=5)

        self.entry_j1 = tk.Entry(frame)
        self.entry_j1.grid(row=0, column=1, padx=5, pady=5)

        self.label_j2 = tk.Label(frame, text="Prénom du Joueur 2:")
        self.label_j2.grid(row=1, column=0, padx=5, pady=5)

        self.entry_j2 = tk.Entry(frame)
        self.entry_j2.grid(row=1, column=1, padx=5, pady=5)

        self.start_button = tk.Button(frame, text="Commencer le jeu", command=self.start_game)
        self.start_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.turn_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.turn_label.grid(row=1, column=0, columnspan=7, padx=10, pady=10)

        # Créer une frame pour les boutons des colonnes
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=2, column=0, columnspan=7)

        self.buttons = []
        for col in range(7):
            button = tk.Button(button_frame, text=str(col + 1), width=10, command=lambda c=col: self.drop_token(c))
            button.grid(row=0, column=col, padx=5, pady=5)
            self.buttons.append(button)

        self.canvas = tk.Canvas(self.root, width=700, height=600, bg="blue")
        self.canvas.grid(row=3, column=0, columnspan=7)
        self.draw_board()

    def start_game(self):
        self.players[0] = self.entry_j1.get()
        self.players[1] = self.entry_j2.get()

        if not self.players[0] or not self.players[1]:
            messagebox.showwarning("Attention", "Veuillez entrer les prénoms des deux joueurs.")
            return

        self.current_player = 1
        self.update_turn_label()

    def update_turn_label(self):
        self.turn_label.config(text=f"C'est au tour de {self.players[self.current_player - 1]} (Joueur {self.current_player})")

    def draw_board(self):
        self.canvas.delete("all")
        for row in range(6):
            for col in range(7):
                x0 = col * 100
                y0 = row * 100
                x1 = x0 + 100
                y1 = y0 + 100
                if self.board[row][col] == 0:
                    self.canvas.create_oval(x0 + 10, y0 + 10, x1 - 10, y1 - 10, fill="white")
                elif self.board[row][col] == 1:
                    self.canvas.create_oval(x0 + 10, y0 + 10, x1 - 10, y1 - 10, fill="red")
                elif self.board[row][col] == 2:
                    self.canvas.create_oval(x0 + 10, y0 + 10, x1 - 10, y1 - 10, fill="yellow")

    def drop_token(self, col):
        for row in reversed(range(6)):
            if self.board[row][col] == 0:
                self.board[row][col] = self.current_player
                if self.check_win(row, col):
                    self.draw_board()
                    messagebox.showinfo("Fin de la partie", f"{self.players[self.current_player - 1]} (Joueur {self.current_player}) a gagné!")
                    self.reset_board()
                elif all(self.board[0][c] != 0 for c in range(7)):
                    self.draw_board()
                    messagebox.showinfo("Fin de la partie", "Match nul!")
                    self.reset_board()
                else:
                    self.current_player = 3 - self.current_player  # Changer de joueur
                    self.update_turn_label()
                self.draw_board()
                return

    def check_win(self, row, col):
        def check_direction(delta_row, delta_col):
            count = 1
            for delta in (1, -1):
                r, c = row, col
                while True:
                    r += delta * delta_row
                    c += delta * delta_col
                    if 0 <= r < 6 and 0 <= c < 7 and self.board[r][c] == self.board[row][col]:
                        count += 1
                    else:
                        break
            return count >= 4

        return (check_direction(0, 1) or  # Horizontal
                check_direction(1, 0) or  # Vertical
                check_direction(1, 1) or  # Diagonal /
                check_direction(1, -1))   # Diagonal \

    def reset_board(self):
        self.board = [[0] * 7 for _ in range(6)]
        self.current_player = 1
        self.update_turn_label()
        self.draw_board()

if __name__ == "__main__":
    root = tk.Tk()
    app = Puissance4(root)
    root.mainloop()

