#! python3

import numpy as np
import matplotlib.pyplot as plt
#from sklearn.metrics import mean_squared_error

# Generate random data points
np.random.seed(42)
x = np.linspace(0, 30, 100)
y_true = 0.1 * x**2 - 2 * x + 10  # True function
noise = np.random.normal(0, 5, x.shape)  # Add noise (simulating environmental randomness)
y_obs = y_true + noise  # Observed values (simulating rewards Q in reinforcement learning)

# Calculate the original variance of observations (without Baseline)
variance_origin = np.var(y_obs)  # Variance of the observations themselves

# Calculate residual variance (observation - true function) - simulating advantage function with Baseline
residuals = y_obs - y_true
variance_residual = np.var(residuals)  # Variance of residuals

# Fit a quadratic function (simulating Baseline prediction)
coeffs = np.polyfit(x, y_obs, 2)  # Quadratic polynomial fit
y_pred = np.polyval(coeffs, x)  # Predicted values

# Visualization
plt.figure(figsize=(12, 6))
plt.scatter(x, y_obs, alpha=0.6, label=f'Observed values (variance={variance_origin:.2f})')
#plt.plot(x, y_true, 'r-', linewidth=3, label='True function: $y=0.1x^2 - 2x + 10$')
plt.plot(x, y_pred, 'b--', linewidth=2, label=f'Fitted function: ${coeffs[0]:.2f}x^2 + {coeffs[1]:.2f}x + {coeffs[2]:.2f}$')
plt.vlines(x, ymin=np.minimum(y_obs, y_true), ymax=np.maximum(y_obs, y_true), 
           colors='gray', alpha=0.3, label='Residuals (observed - true value)')
plt.title(f"Baseline Method Variance Reduction Verification\nResidual variance ({variance_residual:.2f}) < Original observation variance ({variance_origin:.2f})")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig("baseline.png")

# Print comparison results
print(f"Original observation variance: {variance_origin:.4f}")
print(f"Residual variance after subtracting true function: {variance_residual:.4f}")
print(f"Variance reduction percentage: {(variance_origin - variance_residual) / variance_origin * 100:.1f}%")