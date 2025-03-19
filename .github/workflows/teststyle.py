import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# Configuration de l'affichage
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

# Création des lignes colorées
num_lines = 20  # Nombre de lignes animées
lines = [ax.plot([], [], lw=2, alpha=0.7)[0] for _ in range(num_lines)]
colors = [plt.cm.viridis(i / num_lines) for i in range(num_lines)]
for line, color in zip(lines, colors):
    line.set_color(color)

# Fonction d'initialisation
def init():
    for line in lines:
        line.set_data([], [])
    return lines

# Fonction d'animation
def update(frame):
    t = [i * (2 * math.pi / 100) for i in range(100)]
    for i, line in enumerate(lines):
        phase = frame / 10 + i * math.pi / num_lines
        x = [math.cos(val + phase) * (1 + 0.3 * math.sin(frame / 20)) for val in t]
        y = [math.sin(val + phase) * (1 + 0.3 * math.cos(frame / 20)) for val in t]
        line.set_data(x, y)
    return lines

# Création et lancement de l'animation
ani = animation.FuncAnimation(fig, update, frames=200, init_func=init, blit=True, interval=50)

plt.show()

