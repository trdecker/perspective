import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, CheckButtons
          #  x  y  z  theta
i = np.array([0, 0, 0, 0])
j = np.array([0, 0, 0, 0])
k = np.array([0, 0, 0, 0])

start_x = 5
start_y = 5
start_theta = 0

fig, ax = plt.subplots()
fig.subplots_adjust(right=0.75)

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')

ax.axis('off')
# ticks = np.arange(-10, 11, 2)
# ax.set_xticks(ticks)
# ax.set_yticks(ticks)

# ax.spines['left'].set_position('zero')
# ax.spines['bottom'].set_position('zero')
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)

# Slider axes: [left, bottom, width, height]
box_ax_i_x = fig.add_axes([0.80, 0.90, 0.12, 0.04])
box_ax_i_y = fig.add_axes([0.80, 0.85, 0.12, 0.04])
box_ax_i_theta = fig.add_axes([0.80, 0.80, 0.12, 0.04])

box_ax_j_x = fig.add_axes([0.80, 0.68, 0.12, 0.04])
box_ax_j_y = fig.add_axes([0.80, 0.63, 0.12, 0.04])
box_ax_j_theta = fig.add_axes([0.80, 0.58, 0.12, 0.04])

box_ax_k_x = fig.add_axes([0.80, 0.46, 0.12, 0.04])
box_ax_k_y = fig.add_axes([0.80, 0.41, 0.12, 0.04])
box_ax_k_z = fig.add_axes([0.80, 0.36, 0.12, 0.04])

check_ax_i = fig.add_axes([0.94, 0.8, 0.05, 0.06], frameon=False)
check_ax_j = fig.add_axes([0.94, 0.7, 0.05, 0.06], frameon=False)
check_ax_k = fig.add_axes([0.94, 0.6, 0.05, 0.06], frameon=False)

# Sliders

x_range = np.array([-10, 10])
y_range = np.array([-10, 10])
z_range = np.array([-10, 10])

i_start = np.array([-5, 0])
j_start = np.array([5, 0])
k_start = np.array([0, -5])

slider_i_x = Slider(box_ax_i_x, "i_x ± ", x_range[0], x_range[1], valinit=i_start[0], valstep=0.1)
slider_i_y = Slider(box_ax_i_y, "i_y ± ", y_range[0], y_range[1], valinit=i_start[1], valstep=0.1)
slider_i_theta = Slider(box_ax_i_theta, "i_θ ± ", 0, 10, valinit=0, valstep=0.1)

slider_j_x = Slider(box_ax_j_x, "j_x ± ", x_range[0], x_range[1], valinit=j_start[0], valstep=0.1)
slider_j_y = Slider(box_ax_j_y, "j_y ± ", y_range[0], y_range[1], valinit=j_start[1], valstep=0.1)
slider_j_theta = Slider(box_ax_j_theta, "j_θ ± ", 0, 10, valinit=0, valstep=0.1)

slider_k_x = Slider(box_ax_k_x, "k_x ± ", x_range[0], x_range[1], valinit=k_start[0], valstep=0.1)
slider_k_y = Slider(box_ax_k_y, "k_y ± ", y_range[0], y_range[1], valinit=k_start[1], valstep=0.1)

# One checkbox per group

check_i = CheckButtons(check_ax_i, ['inf'], [False])
check_j = CheckButtons(check_ax_j, ['inf'], [False])
check_k = CheckButtons(check_ax_k, ['inf'], [False])

# Dots
i_dot = ax.scatter(0, 0, color='red', zorder=3)
j_dot = ax.scatter(0, 0, color='green', zorder=3)
k_dot = ax.scatter(0, 0, color='blue', zorder=3)

u_dot = ax.scatter(0, 0, color='black', zorder=2)

# Lines
i_line, = ax.plot([0, i_start[0]], [0, i_start[1]], color='red', linewidth=2, zorder=3)
j_line, = ax.plot([0, j_start[0]], [0, j_start[1]], color='green', linewidth=2, zorder=3)
k_line, = ax.plot([0, k_start[0]], [0, k_start[1]], color='blue', linewidth=2, zorder=4)

horizon, = ax.plot([i_start[0], j_start[0]], [i_start[1], j_start[1]], color='black', linestyle='dashed')

# line, = ax.plot([0, 0, 0, 0, 0], [0, 0, 0, 0, 0], color='black', linewidth=2)
 
def update(_):
  # Get i values
  i_x = slider_i_x.val
  i_y = slider_i_y.val
  # i_z = slider_i_z.val

  # Get j valeus
  j_x = slider_j_x.val
  j_y = slider_j_y.val
  # j_z = slider_j_z.val
  
  k_x = slider_k_x.val
  k_y = slider_k_y.val
  # k_z = slider_z_z.val

  i_inf = check_i.get_status()[0]
  j_inf = check_j.get_status()[0]
  k_inf = check_k.get_status()[0]

  # Hide dots if needed
  i_dot.set_visible(not i_inf)
  j_dot.set_visible(not j_inf)
  k_dot.set_visible(not k_inf)

  # Update dots
  i_dot.set_offsets([i_x, i_y])
  j_dot.set_offsets([j_x, j_y])
  k_dot.set_offsets([k_x, k_y])

  # Update lines
  i_line.set_data([0, i_x], [0, i_y])
  j_line.set_data([0, j_x], [0, j_y])
  k_line.set_data([0, k_x], [0, k_y])

  horizon.set_data([i_x, j_x], [i_y, j_y])

  # Update x line
  # if not i_inf:
  #   i_line.set_data([x, -x], [0, 0])
  # else:
  #   i_line.set_data([-1e6, 1e6], [0, 0])

  # Update y line
  # if not j_inf:
  #   j_line.set_data([0, 0], [-y, y])
  # else:
  #   j_line.set_data([0, 0], [-1e6, 1e6])

  # Update perspective lines
  # line.set_data([-1e6 if i_inf else -x, 0, 1e6 if i_inf else x, 0, -1e6 if i_inf else -x],
  #               [0, 1e6 if j_inf else y, 0, -1e6 if j_inf else -y, 0])

  # Draw canvas
  fig.canvas.draw_idle()

def toggle(check, slider):
  checked = check.get_status()[0]
  slider.set_active(not checked)
  slider.poly.set_alpha(0.4 if checked else 1)
  update(None)
  fig.canvas.draw_idle()

# Sliders
slider_i_x.on_changed(update)
slider_i_y.on_changed(update)

slider_j_x.on_changed(update)
slider_j_y.on_changed(update)

slider_k_x.on_changed(update)
slider_k_y.on_changed(update)

# Check boxes
# check_i.on_clicked(lambda _: toggle(check_i, slider_i))
# check_j.on_clicked(lambda _: toggle(check_j, slider_j))
# check_z.on_clicked(lambda _: toggle(check_z, slider_z))

# slider_z.on_submit(lambda val:
#                    x_1.set_offsets([]))
update(None)
plt.show()