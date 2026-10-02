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
theta_range = np.array([0, 2*np.pi])

i_start = np.array([-5, 0, 0.75*np.pi])
j_start = np.array([5, 0, 0.25*np.pi])
k_start = np.array([0, -10, 1.5*np.pi])
a_start = np.array([0, -5])

u_v_w_range = np.array([0, 1])

def make_slider(row, label, vrange, start, step=0.1):
  ax_s = fig.add_axes([0.80, row, 0.12, 0.04])
  return Slider(ax_s, label, vrange[0], vrange[1], valinit=start, valstep=step)

slider_i_x = make_slider(0.90, "i_x ", x_range, i_start[0])
slider_i_y = make_slider(0.85, "i_y ", y_range, i_start[1])
slider_i_theta = make_slider(0.80, "i_θ ", theta_range, i_start[2])

slider_j_x = make_slider(0.68, "j_x ", x_range, j_start[0])
slider_j_y = make_slider(0.63, "j_y ", y_range, j_start[1])
slider_j_theta = make_slider(0.57, "j_θ ", theta_range, j_start[2])

slider_k_x = make_slider(0.46, "k_x ", x_range, k_start[0])
slider_k_y = make_slider(0.41, "k_y ", y_range, k_start[1])
slider_k_theta = make_slider(0.38, "k_θ ", theta_range, k_start[2])

slider_a_x = make_slider(0.24, "a_x ", x_range, a_start[0])
slider_a_y = make_slider(0.19, "a_y ", y_range, a_start[1])

slider_u = make_slider(0.13, "u", u_v_w_range, 0.5, step=0.02)
slider_v = make_slider(0.06, "v", u_v_w_range, 0.5, step=0.02)
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

iv_ju_k, = ax.plot([], [], color='gray', linestyle='dashed', zorder=3)
iw_ku_j, = ax.plot([], [], color='gray', linestyle='dashed', zorder=3)
kv_jw_i, = ax.plot([], [], color='gray', linestyle='dashed', zorder=3)

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
  i_theta = slider_i_theta.val

  # Get j slider values
  j_x = slider_j_x.val
  j_y = slider_j_y.val
  j_theta = slider_j_theta.val
  
  # Get k slider values
  k_x = slider_k_x.val
  k_y = slider_k_y.val
  k_theta = slider_k_theta.val

  # Get a slider values
  a_x = slider_a_x.val
  a_y = slider_a_y.val

  i_inf = check_i.get_status()[0]
  j_inf = check_j.get_status()[0]
  k_inf = check_k.get_status()[0]
  
  i_p, j_p, k_p = (i_x, i_y), (j_x, j_y), (k_x, k_y)

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
  if i_inf:
    u_x = a_x + u_pos * 10 * np.cos(i_theta)
    u_y = a_y + u_pos * 10 * np.sin(i_theta)
  else:
    u_x = a_x + u_pos * (i_x - a_x)
    u_y =  a_y + u_pos * (i_y - a_y)
  u_dot.set_offsets([u_x, u_y])

  v_pos = slider_v.val
  if j_inf:
    v_x = a_x + v_pos * 10 * np.cos(j_theta)
    v_y = a_y + v_pos * 10 * np.sin(j_theta)
  else:
    v_x = a_x + v_pos * (j_x - a_x)
    v_y =  a_y + v_pos * (j_y - a_y)
  v_dot.set_offsets([v_x, v_y])

  w_pos = slider_w.val
  if k_inf:
    w_x = a_x + w_pos * 10 * np.cos(k_theta)
    w_y = a_y + w_pos * 10 * np.sin(k_theta)
  else:
    w_x = a_x + w_pos * (k_x - a_x)
    w_y =  a_y + w_pos * (k_y - a_y)
  w_dot.set_offsets([w_x, w_y])

  # Update i lines
  if not i_inf:
    i_line.set_data([a_x, i_x], [a_y, i_y])
    i_v.set_data([v_x, i_x], [v_y, i_y])
    i_w.set_data([w_x, i_x], [w_y, i_y])
  else:
    i_dx = 1e6 * np.cos(i_theta)
    i_dy = 1e6 * np.sin(i_theta)
    i_line.set_data([a_x, a_x + i_dx], [a_y, a_y + i_dy])
    i_v.set_data([v_x, v_x + i_dx], [v_y, v_y + i_dy])
    i_w.set_data([w_x, w_x + i_dx], [w_y, w_y + i_dy])

  # Update j lines
  if not j_inf:
    j_line.set_data([a_x, j_x], [a_y, j_y])
    j_u.set_data([u_x, j_x], [u_y, j_y])
    j_w.set_data([w_x, j_x], [w_y, j_y])
  else:
    j_dx = 1e6 * np.cos(j_theta)
    j_dy = 1e6 * np.sin(j_theta)
    j_line.set_data([a_x, a_x + j_dx], [a_y, a_y + j_dy])
    j_u.set_data([u_x, u_x + j_dx], [u_y, u_y + j_dy])
    j_w.set_data([w_x, w_x + j_dx], [w_y, w_y + j_dy])

  # Update k lines
  if not k_inf:
    k_line.set_data([a_x, k_x], [a_y, k_y])
    k_u.set_data([u_x, k_x], [u_y, k_y])
    k_v.set_data([v_x, k_x], [v_y, k_y])
  else:
    k_dx = 1e6 * np.cos(k_theta)
    k_dy = 1e6 * np.sin(k_theta)
    k_line.set_data([a_x, a_x + k_dx], [a_y, a_y + k_dy])
    k_u.set_data([u_x, u_x + k_dx], [u_y, u_y + k_dy])
    k_v.set_data([v_x, v_x + k_dx], [v_y, v_y + k_dy])

  # Find intersects and draw lines to vanishing points
  for dot, line, line_1, line_2, target, inf, theta in [
      (iv_ju_dot, iv_ju_k, i_v, j_u, k_p, k_inf, k_theta),
      (iw_ku_dot, iw_ku_j, i_w, k_u, j_p, j_inf, j_theta),
      (kv_jw_dot, kv_jw_i, k_v, j_w, i_p, i_inf, i_theta)]:
    p = intersect(*line_1.get_xydata(), *line_2.get_xydata())
    dot.set_visible(p is not None)
    line.set_visible(p is not None)
    if p is not None:
      dot.set_offsets([p])
      if inf:
        line.set_data([p[0], p[0] + 1e6 * np.cos(theta)], [p[1], p[1] + 1e6 * np.sin(theta)])
      else:
        line.set_data([p[0], target[0]], [p[1], target[1]])

  # Update horizon
  if i_inf and j_inf:
    horizon.set_visible(False)
  else:
    horizon.set_visible(True)
    p1 = j_p if i_inf else i_p
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
slider_i_theta.on_changed(update)

slider_j_x.on_changed(update)
slider_j_y.on_changed(update)
slider_j_theta.on_changed(update)

slider_k_x.on_changed(update)
slider_k_y.on_changed(update)
slider_k_theta.on_changed(update)

slider_a_x.on_changed(update)
slider_a_y.on_changed(update)

slider_u.on_changed(update)
slider_v.on_changed(update)
slider_w.on_changed(update)

# Check boxes
check_i.on_clicked(lambda _: toggle(check_i, [slider_i_x, slider_i_y]))
check_j.on_clicked(lambda _: toggle(check_j, [slider_j_x, slider_j_y]))
check_k.on_clicked(lambda _: toggle(check_k, [slider_k_x, slider_k_y]))

update(None)
plt.show()