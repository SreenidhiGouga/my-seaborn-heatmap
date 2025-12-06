# chart.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate synthetic customer engagement data
np.random.seed(42)
data = pd.DataFrame({
    'Visits': np.random.randint(1, 50, 50),
    'Clicks': np.random.randint(1, 80, 50),
    'Time_Spent': np.random.randint(10, 300, 50),
    'Purchase_Amount': np.random.randint(0, 5000, 50),
    'Retention_Score': np.random.randint(1, 100, 50)
})

# Compute correlation matrix
corr_matrix = data.corr()

# Set Seaborn styling
sns.set_style("white")
sns.set_context("talk")

# Create figure sized for 512x512 output with dpi=64
plt.figure(figsize=(8, 8))

# Create heatmap
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5,
    square=True
)

plt.title("Customer Engagement Correlation Heatmap")

# Save EXACTLY as 512x512 px
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
