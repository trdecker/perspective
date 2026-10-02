import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, CheckButtons

i = np.zeros(4)
j = np.zeros(4)
k = np.zeros(4)

fig, ax = plt.subplots()
fig.subplots_adjust(right=0.75)

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')

ax.axis('off')

# Sliders

x_range = np.array([-10, 10])
y_range = np.array([-10, 10])
z_range = np.array([-10, 10])

i_start = np.array([-5, 0])
j_start = np.array([5, 0])
k_start = np.array([0, -10])
a_start = np.array([0, -5])

u_v_w_range = np.array([0, 1])

def make_slider(row, label, vrange, start, step=0.1):
  ax_s = fig.add_axes([0.80, row, 0.12, 0.04])
  return Slider(ax_s, label, vrange[0], vrange[1], valinit=start, valstep=step)

slider_i_x = make_slider(0.90, "i_x ", x_range, i_start[0])
slider_i_y = make_slider(0.85, "i_y ", y_range, i_start[1])

slider_j_x = make_slider(0.68, "j_x ", x_range, j_start[0])
slider_j_y = make_slider(0.63, "j_y ", y_range, j_start[1])

slider_k_x = make_slider(0.46, "k_x ", x_range, k_start[0])
slider_k_y = make_slider(0.41, "k_y ", y_range, k_start[1])

slider_a_x = make_slider(0.24, "a_x ", x_range, a_start[0])
slider_a_y = make_slider(0.19, "a_y ", y_range, a_start[1])

slider_u = make_slider(0.13, "u", u_v_w_range, 0.5, step=0.02)
slider_v = make_slider(0.6, "v", u_v_w_range, 0.5, step=0.02)
slider_w = make_slider(0, "w", u_v_w_range, 0.5, step=0.02)

# Check boxes
def make_check(row):
  ax_c = fig.add_axes([0.94, row, 0.05, 0.04], frameon=False)
  return CheckButtons(ax_c, ['inf'], [False])

check_i = make_check(0.90)
check_j = make_check(0.68)
check_k = make_check(0.46)

# Dots
i_dot = ax.scatter(0, 0, color='red', zorder=3)
j_dot = ax.scatter(0, 0, color='green', zorder=3)
k_dot = ax.scatter(0, 0, color='blue', zorder=3)

a_dot = ax.scatter(0, 0, color='black', zorder=2)

u_dot = ax.scatter(0, 0, color='black', zorder=4)
v_dot = ax.scatter(0, 0, color='black', zorder=4)
w_dot = ax.scatter(0, 0, color='black', zorder=4)

# Lines
i_line, = ax.plot([0, i_start[0]], [0, i_start[1]], color='red', linewidth=2, zorder=3)
j_line, = ax.plot([0, j_start[0]], [0, j_start[1]], color='green', linewidth=2, zorder=3)
k_line, = ax.plot([0, k_start[0]], [0, k_start[1]], color='blue', linewidth=2, zorder=4)

horizon, = ax.plot([i_start[0], j_start[0]], [i_start[1], j_start[1]], color='black', linestyle='dashed')

i_v, = ax.plot([0, 0], [0, 0], color='black', linewidth=2, zorder=3)
i_w, = ax.plot([], [], color='black', linewidth=2, zorder=3)

j_u, = ax.plot([], [], color='black', linewidth=2, zorder=3)
j_w, = ax.plot([], [], color='black', linewidth=2, zorder=3)

k_u, = ax.plot([], [], color='black', linewidth=2, zorder=3)
k_v, = ax.plot([], [], color='black', linewidth=2, zorder=3)

iv_ju_dot = ax.scatter(0, 0, color='black', zorder=3)
iw_ku_dot = ax.scatter(0, 0, color='black', zorder=3)
kv_jw_dot = ax.scatter(0, 0, color='black', zorder=3)

iv_ju_k, = ax.plot([], [], color='black', zorder=3)
iw_ku_j, = ax.plot([], [], color='black', zorder=3)
kv_jw_i, = ax.plot([], [], color='black', zorder=3)

# line, = ax.plot([0, 0, 0, 0, 0], [0, 0, 0, 0, 0], color='black', linewidth=2)

def intersect(p1, p2, p3, p4):
  """Where line_one crosses line_two, or None if parallel"""
  (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
  denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
  if abs(denom) < 1e-12:
    return None
  a = x1 * y2 - y1 * x2
  b = x3 * y4 - y3 * x4
  return ((a * (x3 - x4) - (x1 - x2) * b) / denom,
    (a * (y3 - y4) - (y1 - y2) * b) / denom)
 
def update(_):
  # Update dot values
  i[:2] = [slider_i_x.val, slider_i_y.val]
  j[:2] = [slider_j_x.val, slider_j_y.val]
  k[:2] = [slider_k_x.val, slider_k_y.val]

  # Get i slider values
  i_x = slider_i_x.val
  i_y = slider_i_y.val
  # i_z = slider_i_z.val

  # Get j slider values
  j_x = slider_j_x.val
  j_y = slider_j_y.val
  # j_z = slider_j_z.val
  
  # Get k slider values
  k_x = slider_k_x.val
  k_y = slider_k_y.val
  # k_z = slider_z_z.val

  # Get a slider values
  a_x = slider_a_x.val
  a_y = slider_a_y.val

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
  a_dot.set_offsets([a_x, a_y])

  u_pos = slider_u.val
  u_x = a_x + u_pos * (i_x - a_x)
  u_y =  a_y + u_pos * (i_y - a_y)
  u_dot.set_offsets([u_x, u_y])

  v_pos = slider_v.val
  v_x = a_x + v_pos * (j_x - a_x)
  v_y =  a_y + v_pos * (j_y - a_y)
  v_dot.set_offsets([v_x, v_y])

  w_pos = slider_w.val
  w_x = a_x + w_pos * (k_x - a_x)
  w_y =  a_y + w_pos * (k_y - a_y)
  w_dot.set_offsets([w_x, w_y])

  # Find interesects and draw lines to vanishing points
  i_p, j_p, k_p = (i_x, i_y), (j_x, j_y), (k_x, k_y)
  u_p, v_p, w_p = (u_x, u_y), (v_x, v_y), (w_x, w_y)

  for dot, line, pts, target in [
      (iv_ju_dot, iv_ju_k, (i_p, v_p, j_p, u_p), k_p),
      (iw_ku_dot, iw_ku_j, (i_p, w_p, k_p, u_p), j_p),
      (kv_jw_dot, kv_jw_i, (k_p, v_p, j_p, w_p), i_p)]:
    p = intersect(*pts)
    dot.set_visible(p is not None)
    line.set_visible(p is not None)
    if p is not None:
      dot.set_offsets([p])
      line.set_data([p[0], target[0]], [p[1], target[1]])

  # Update lines
  i_line.set_data([a_x, i_x], [a_y, i_y])
  j_line.set_data([a_x, j_x], [a_y, j_y])
  k_line.set_data([a_x, k_x], [a_y, k_y])

  i_v.set_data([i_x, v_x], [i_y, v_y])
  i_w.set_data([i_x, w_x], [i_y, w_y])

  j_u.set_data([j_x, u_x], [j_y, u_y])
  j_w.set_data([j_x, w_x], [j_y, w_y])

  k_u.set_data([k_x, u_x], [k_y, u_y])
  k_v.set_data([k_x, v_x], [k_y, v_y])

  # Update horizon
  d = np.array([j_x - i_x, j_y - i_y])
  length = np.hypot(*d)
  if length == 0:
    horizon.set_data([i_x], [i_y]) # Direction less
  else:
    d = d / length * 1e6
    horizon.set_data([i_x - d[0], j_x + d[0]], [i_y - d[1], j_y + d[1]])

  # Draw canvas
  fig.canvas.draw_idle()

def toggle(check, sliders):
  checked = check.get_status()[0]
  for slider in sliders:
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

slider_a_x.on_changed(update)
slider_a_y.on_changed(update)

slider_u.on_changed(update)
slider_v.on_changed(update)
slider_w.on_changed(update)

# Check boxes
# check_i.on_clicked(lambda _: toggle(check_i, [slider_i_x, slider_i_y]))
# check_j.on_clicked(lambda _: toggle(check_j, [slider_j_x, slider_j_y]))
# check_k.on_clicked(lambda _: toggle(check_k, [slider_k_x, slider_k_y]))

# slider_z.on_submit(lambda val:
#                    x_1.set_offsets([]))
update(None)
plt.show()