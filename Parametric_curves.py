import numpy as np
import matplotlib.pyplot as plt

# Dark Theme
plt.style.use('dark_background')

# Parameter range
t = np.linspace(0, 2 * np.pi, 1000)

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('Parametric Curves Visualization',
             fontsize=15, fontweight='bold')

# =========================
# Circle
# =========================
x_circle = np.cos(t)
y_circle = np.sin(t)

axes[0, 0].plot(x_circle, y_circle,
                color='cyan',
                linewidth=3,
                label='Circle')

axes[0, 0].scatter(x_circle[0], y_circle[0],
                   color='lime', s=80, label='Start')

axes[0, 0].scatter(x_circle[-1], y_circle[-1],
                   color='red', s=80, label='End')

axes[0, 0].set_title('Circle\n$x=cos(t), y=sin(t)$')
axes[0, 0].set_aspect('equal')
axes[0, 0].grid(True, alpha=0.3)
axes[0, 0].legend()

# =========================
# Ellipse
# =========================
a, b = 3, 2

x_ellipse = a*np.cos(t)
y_ellipse = b*np.sin(t)

axes[0, 1].plot(x_ellipse, y_ellipse,
                color='orange',
                linewidth=3,
                label='Ellipse')

axes[0, 1].scatter(a, 0, color='yellow', s=80)
axes[0, 1].scatter(-a, 0, color='yellow', s=80)

axes[0, 1].set_title(f'Ellipse\nx={a}cos(t), y={b}sin(t)')
axes[0, 1].set_aspect('equal')
axes[0, 1].grid(True, alpha=0.3)
axes[0, 1].legend()

# =========================
# Lissajous Curve
# =========================
x_liss = np.sin(3*t)
y_liss = np.sin(2*t)

axes[0, 2].plot(x_liss, y_liss,
                color='lime',
                linewidth=3)

axes[0, 2].set_title('Lissajous\nx=sin(3t), y=sin(2t)')
axes[0, 2].set_aspect('equal')
axes[0, 2].grid(True, alpha=0.3)

# =========================
# Cycloid
# =========================
r = 1

x_cycloid = r*(t - np.sin(t))
y_cycloid = r*(1 - np.cos(t))

axes[1, 0].plot(x_cycloid, y_cycloid,
                color='magenta',
                linewidth=3)

axes[1, 0].set_title('Cycloid')
axes[1, 0].grid(True, alpha=0.3)

# =========================
# Rose Curve
# =========================
k = 5

x_rose = np.cos(k*t) * np.cos(t)
y_rose = np.cos(k*t) * np.sin(t)

axes[1, 1].plot(x_rose, y_rose,
                color='red',
                linewidth=3)

axes[1, 1].set_title('Rose Curve')
axes[1, 1].set_aspect('equal')
axes[1, 1].grid(True, alpha=0.3)

# =========================
# Archimedean Spiral
# =========================
r_spiral = t

x_spiral = r_spiral*np.cos(t)
y_spiral = r_spiral*np.sin(t)

axes[1, 2].plot(x_spiral, y_spiral,
                color='gold',
                linewidth=3)

axes[1, 2].set_title('Archimedean Spiral')
axes[1, 2].set_aspect('equal')
axes[1, 2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()