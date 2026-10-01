import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
fig.subplots_adjust(right=0.75)

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')

ticks = np.arange(-10, 11, 2)
ax.set_xticks(ticks)
ax.set_yticks(ticks)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

box_ax_x = fig.add_axes([0.85, 0.8, 0.12, 0.06])
box_ax_y = fig.add_axes([0.85, 0.7, 0.12, 0.06])
# box_ax_z = fig.add_axes([0.85, 0.6, 0.12, 0.06])

slider_x = Slider(box_ax_x, "x ± ", 0, 10, valinit=0, valstep=0.1)
slider_y = Slider(box_ax_y, "y ± ", 0, 10, valinit=0, valstep=0.1)
# slider_z = Slider(box_ax_z, "z ± ", 0, 10, valinit=0, valstep=0.1)

points = np.zeros((4, 2))  # 6 points, each [x, y]
dots = ax.scatter(points[:, 0], points[:, 1],
                  color=['red', 'red', 'green', 'green'])

def update(_):
  x = slider_x.val
  y = slider_y.val
  # z, z_neg = read(text_box_z)

  dots.set_offsets([[x, 0], [-x, 0],
                    [0, y], [0, -y]])

  fig.canvas.draw_idle()


slider_x.on_changed(update)
slider_y.on_changed(update)
# slider_z.on_submit(lambda val:
#                    x_1.set_offsets([]))
plt.show()