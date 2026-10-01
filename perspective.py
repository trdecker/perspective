import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, CheckButtons

start_x = 6.5
start_y = 6.5

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

box_ax_x = fig.add_axes([0.75, 0.8, 0.12, 0.06])
box_ax_y = fig.add_axes([0.75, 0.7, 0.12, 0.06])

check_ax_x = fig.add_axes([0.94, 0.8, 0.05, 0.06], frameon=False)
check_ax_y = fig.add_axes([0.94, 0.7, 0.05, 0.06], frameon=False)

slider_x = Slider(box_ax_x, "x ± ", 0, 10, valinit=start_x, valstep=0.1)
slider_y = Slider(box_ax_y, "y ± ", 0, 10, valinit=start_y, valstep=0.1)

check_x = CheckButtons(check_ax_x, ['inf'], [False])
check_y = CheckButtons(check_ax_y, ['inf'], [False])

# Dots
x_dots = ax.scatter([0, 0], [0, 0], color='red')
y_dots = ax.scatter([0, 0], [0, 0], color='green')

# Lines
x_line, = ax.plot([0, 0], [0, 0], color='red', linewidth=2, zorder=3)
y_line, = ax.plot([0, 0], [0, 0], color='green', linewidth=2, zorder=3)

line, = ax.plot([0, 0, 0, 0, 0], [0, 0, 0, 0, 0], color='black', linewidth=2)
 
def update(_):
  # Get values
  x = slider_x.val
  y = slider_y.val

  x_inf = check_x.get_status()[0]
  y_inf = check_y.get_status()[0]

  # Hide dots if needed
  x_dots.set_visible(not x_inf)
  y_dots.set_visible(not y_inf)

  # Update dots
  x_dots.set_offsets([[x, 0], [-x, 0]])
  y_dots.set_offsets([[0, y], [0, -y]])

  # Update x line
  if not x_inf:
    x_line.set_data([x, -x], [0, 0])
  else:
    x_line.set_data([-1e6, 1e6], [0, 0])

  # Update y line
  if not y_inf:
    y_line.set_data([0, 0], [-y, y])
  else:
    y_line.set_data([0, 0], [-1e6, 1e6])

  line.set_data([-1e6 if x_inf else -x, 0, 1e6 if x_inf else x, 0, -1e6 if x_inf else -x],
                [0, 1e6 if y_inf else y, 0, -1e6 if y_inf else -y, 0])

  # Draw canvas
  fig.canvas.draw_idle()

def toggle(check, slider):
  checked = check.get_status()[0]
  slider.set_active(not checked)
  slider.poly.set_alpha(0.4 if checked else 1)
  update(None)
  fig.canvas.draw_idle()

# Sliders
slider_x.on_changed(update)
slider_y.on_changed(update)

# Check boxes
check_x.on_clicked(lambda _: toggle(check_x, slider_x))
check_y.on_clicked(lambda _: toggle(check_y, slider_y))

# slider_z.on_submit(lambda val:
#                    x_1.set_offsets([]))
update(None)
plt.show()