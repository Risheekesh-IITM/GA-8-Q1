"""
Employee Department Analysis
Email: 24f1001771@ds.study.iitm.ac.in
"""

import pandas as pd
import matplotlib.pyplot as plt
import mpld3

# ------------------------------------------------
# 1. Create a sample dataset (100 employees)
# ------------------------------------------------

data = {
    "employee_id": range(1, 101),
    "department": [
        "Finance", "HR", "Marketing", "Sales", "Engineering"
    ] * 20,  # repeated pattern
    "region": [
        "North", "South", "East", "West", "Central"
    ] * 20,
}

df = pd.DataFrame(data)

# ------------------------------------------------
# 2. Calculate frequency count for "Marketing"
# ------------------------------------------------

marketing_count = (df["department"] == "Marketing").sum()
print("Frequency of Marketing department:", marketing_count)

# ------------------------------------------------
# 3. Create histogram of department distribution
# ------------------------------------------------

plt.figure(figsize=(8, 5))
plt.hist(df["department"], bins=len(df["department"].unique()), edgecolor="black")
plt.title("Department Distribution of Employees")
plt.xlabel("Departments")
plt.ylabel("Frequency")

# ------------------------------------------------
# 4. Save HTML output (plot + code embedded)
# ------------------------------------------------

html_output = "employee_visualization.html"

# Generate interactive HTML plot
html_graph = mpld3.fig_to_html(plt.gcf())

with open(html_output, "w") as f:
    f.write("""
    <html>
    <head><title>Employee Data Visualization</title></head>
    <body>
    <h1>Employee Visualization Output</h1>
    <p><strong>Email Verification:</strong> 24f1001771@ds.study.iitm.ac.in</p>
    <h2>Python Output</h2>
    <p>Frequency of Marketing Department: {}</p>
    <h2>Histogram Visualization</h2>
    {}
    </body>
    </html>
    """.format(marketing_count, html_graph))

print(f"HTML file saved as {html_output}")
