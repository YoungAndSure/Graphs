#! python3

import numpy as np
import matplotlib.pyplot as plt

# Generate random data points
np.random.seed(42)
x = np.linspace(0, 30, 100)
y_true = 0.1 * x**2 - 2 * x + 10  # True function
noise = np.random.normal(0, 5, x.shape)  # Add noise
y_obs = y_true + noise  # Observed values

# Calculate overall mean
mean_y = np.mean(y_obs)  # Calculate mean of all observations[2,9](@ref)

# Calculate residuals relative to mean
residuals_mean = y_obs - mean_y  # Residuals from mean[3,10](@ref)
variance_residual_mean = np.var(residuals_mean)  # Variance of residuals from mean

# Calculate the original variance of observations
variance_origin = np.var(y_obs)

# Fit a quadratic function (Baseline prediction)
coeffs = np.polyfit(x, y_obs, 2)
y_pred = np.polyval(coeffs, x)

# Visualization
plt.figure(figsize=(14, 8))

# Scatter plot of observed values
plt.scatter(x, y_obs, alpha=0.6, label=f'Observed values (variance={variance_origin:.2f})')

# True function (removed as requested)
# plt.plot(x, y_true, 'r-', linewidth=3, label='True function: $y=0.1x^2 - 2x + 10$')

# Fitted quadratic function
plt.plot(x, y_pred, 'b--', linewidth=2, label=f'Fitted function: ${coeffs[0]:.2f}x^2 + {coeffs[1]:.2f}x + {coeffs[2]:.2f}$')

# Mean line (horizontal line at mean value)
plt.axhline(y=mean_y, color='m', linestyle='-', linewidth=2, label=f'Mean value: {mean_y:.2f}')

# Residuals from mean (vertical lines from mean to observed values)
plt.vlines(x, ymin=mean_y, ymax=y_obs, 
           colors='g', alpha=0.4, label='Residuals from mean')

# Add labels and title
plt.title(f"Variance Reduction Using Mean as Baseline\nOriginal variance ({variance_origin:.2f})")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig("baseline2.png")

# Print comparison results
print(f"Original observation variance: {variance_origin:.4f}")
print(f"Residual variance from mean: {variance_residual_mean:.4f}")
print(f"Variance reduction percentage: {(variance_origin - variance_residual_mean) / variance_origin * 100:.1f}%")