import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------------------------
# Load dataset
# ---------------------------------------
df = pd.read_csv('customer_support_response_times.csv')

# ---------------------------------------
# Styling
# ---------------------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

plt.figure(figsize=(8, 8))

# ---------------------------------------
# Violin Plot
# ---------------------------------------
sns.violinplot(
    data=df,
    x='channel',
    y='response_time_minutes',
    palette='Set2',
    inner='box',
    cut=0
)

# ---------------------------------------
# Titles and Labels
# ---------------------------------------
plt.title("Distribution of Customer Support Response Times by Channel")
plt.xlabel("Support Channel")
plt.ylabel("Response Time (minutes)")

# ---------------------------------------
# Save Output
# ---------------------------------------
plt.savefig('chart.png', dpi=64)

plt.close()
