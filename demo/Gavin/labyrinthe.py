import tkinter as tk
import random
import time
import json
import os

class MazeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de Labyrinthe")
        self.cell_size = 20
        self.maze_size = 30
        self.canvas_size = self.maze_size * self.cell_size
        self.maze = self.generate_maze(self.maze_size, self.maze_size)
        self.player_pos = [1, 1]
        self.start_time = None
        self.running = False
        self.high_scores = self.load_scores()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=self.canvas_size, height=self.canvas_size, bg="white")
        self.canvas.pack()

        self.timer_label = tk.Label(self.root, text="Temps: 0s", font=("Arial", 14))
        self.timer_label.pack()

        self.entry_label = tk.Label(self.root, text="Entrez votre nom:")
        self.entry_label.pack()
        
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()
        
        self.start_button = tk.Button(self.root, text="Commencer le jeu", command=self.start_game)
        self.start_button.pack()

        self.draw_maze()
        self.root.bind("<KeyPress>", self.on_key_press)

    def generate_maze(self, width, height):
        maze = [[1] * width for _ in range(height)]
        
        def carve_passages(x, y):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + dx*2, y + dy*2
                if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                    maze[ny][nx] = 0
                    maze[ny - dy][nx - dx] = 0
                    carve_passages(nx, ny)
        
        maze[1][1] = 0
        carve_passages(1, 1)
        
        return maze

    def draw_maze(self):
        self.canvas.delete("all")
        for y in range(self.maze_size):
            for x in range(self.maze_size):
                color = "black" if self.maze[y][x] == 1 else "white"
                self.canvas.create_rectangle(x*self.cell_size, y*self.cell_size, 
                                             (x+1)*self.cell_size, (y+1)*self.cell_size, 
                                             fill=color, outline=color)
        self.canvas.create_rectangle(self.player_pos[0]*self.cell_size, self.player_pos[1]*self.cell_size, 
                                     (self.player_pos[0]+1)*self.cell_size, (self.player_pos[1]+1)*self.cell_size, 
                                     fill="blue", outline="blue")
        self.canvas.create_rectangle((self.maze_size-2)*self.cell_size, (self.maze_size-2)*self.cell_size,
                                     (self.maze_size-1)*self.cell_size, (self.maze_size-1)*self.cell_size,#ici
                                     fill="red", outline="red")

    def start_game(self):
        self.player_name = self.name_entry.get().strip()
        if not self.player_name:
            tk.messagebox.showwarning("Attention", "Veuillez entrer votre nom.")
            return

        self.start_time = time.time()
        self.running = True
        self.update_timer()
        self.draw_maze()
        
    def update_timer(self):
        if self.running:
            elapsed_time = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Temps: {elapsed_time}s")
            self.root.after(1000, self.update_timer)

    def on_key_press(self, event):
        if not self.running:
            return

        x, y = self.player_pos
        if event.keysym == 'Up' and y > 0 and self.maze[y-1][x] == 0:
            y -= 1
        elif event.keysym == 'Down' and y < self.maze_size - 1 and self.maze[y+1][x] == 0:
            y += 1
        elif event.keysym == 'Left' and x > 0 and self.maze[y][x-1] == 0:
            x -= 1
        elif event.keysym == 'Right' and x < self.maze_size - 1 and self.maze[y][x+1] == 0:
            x += 1

        self.player_pos = [x, y]
        self.draw_maze()

        if self.player_pos == [self.maze_size-2, self.maze_size-2]:
            self.running = False
            elapsed_time = int(time.time() - self.start_time)
            self.save_score(elapsed_time)
            self.show_scores()
            tk.messagebox.showinfo("Félicitations", f"Vous avez gagné en {elapsed_time} secondes!")

    def save_score(self, time):
        self.high_scores.append((self.player_name, time))
        self.high_scores = sorted(self.high_scores, key=lambda x: x[1])[:10]
        with open("high_scores.txt", "w") as file:
            json.dump(self.high_scores, file)

    def load_scores(self):
        if os.path.exists("high_scores.txt"):
            with open("high_scores.txt", "r") as file:
                return json.load(file)
        return []

    def show_scores(self):
        scores = "\n".join([f"{name}: {time}s" for name, time in self.high_scores])
        tk.messagebox.showinfo("Meilleurs Scores", scores)

if __name__ == "__main__":
    root = tk.Tk()
    game = MazeGame(root)
    root.mainloop()

