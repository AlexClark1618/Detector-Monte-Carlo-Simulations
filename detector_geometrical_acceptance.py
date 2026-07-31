import numpy as np

r = 2.54   # cm
h = 2 * r  # vertical separation (using h to avoid confusion with distance d)

def sample_entry_points(N):
    """Uniform points on a disk. Radius needs sqrt to avoid centre clustering."""
    u   = np.random.uniform(0, 1, N)
    phi = np.random.uniform(0, 2 * np.pi, N)
    rho = r * np.sqrt(u)                    # ✅ not r * u
    x0  = rho * np.cos(phi)
    y0  = rho * np.sin(phi)
    return x0, y0                           # ✅ return arrays directly

def sample_directions(N):
    """
    Sample zenith from cos^3(theta)*sin(theta) distribution.
    cos^2 from muon flux, cos from Lambert projection on D1.

    Inverse transform: CDF(cos theta) = cos^4(theta)
    Invert: cos(theta) = u^(1/4), u ~ Uniform(0,1)
    """
    u         = np.random.uniform(0, 1, N)
    cos_theta = u ** (1/4)                  # ✅ exact sampling, no rejection loop
    sin_theta = np.sqrt(1 - cos_theta**2)
    azimuth   = np.random.uniform(0, 2 * np.pi, N)
    return cos_theta, sin_theta, azimuth

def calculate_acceptance(N):
    x0, y0                      = sample_entry_points(N)
    cos_theta, sin_theta, az    = sample_directions(N)

    # Propagate ray to D2 plane
    t     = h / cos_theta               # path length to reach D2
    x_hit = x0 + t * sin_theta * np.cos(az)
    y_hit = y0 + t * sin_theta * np.sin(az)

    hits = (x_hit**2 + y_hit**2) < r**2
    return hits.sum() / N

N          = 1_000_000
acceptance = calculate_acceptance(N)
print(f"Geometric acceptance: {acceptance:.4f}")