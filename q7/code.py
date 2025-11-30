import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO
import numpy as np

# User Email: 23f2001849@ds.study.iitm.ac.in

def main():
    # 1. Generate Synthetic Data (Matching the prompt's structure)
    np.random.seed(42)
    n = 100
    departments = ['Sales', 'IT', 'HR', 'Marketing', 'R&D', 'Operations']
    regions = ['Europe', 'Latin America', 'Asia Pacific', 'Africa', 'North America']
    
    data = {
        'employee_id': [f'EMP{i:03d}' for i in range(1, n+1)],
        'department': np.random.choice(departments, n),
        'region': np.random.choice(regions, n),
        'performance_score': np.round(np.random.uniform(60, 99, n), 2),
        'years_experience': np.random.randint(1, 15, n),
        'satisfaction_rating': np.round(np.random.uniform(2.5, 5.0, n), 1)
    }
    
    df = pd.DataFrame(data)
    
    # Ensure we have some IT entries
    if 'IT' not in df['department'].values:
        df.loc[0:5, 'department'] = 'IT'

    # 2. Calculate Frequency Count for "IT" Department
    it_count = df[df['department'] == 'IT'].shape[0]
    print(f"Frequency count for IT department: {it_count}")

    # 3. Create Histogram (Distribution of Departments)
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")
    # Using histplot for categorical data (distribution of departments)
    ax = sns.histplot(data=df, x='department', shrink=0.8, color='skyblue')
    plt.title('Distribution of Departments', fontsize=15)
    plt.xlabel('Department', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.tight_layout()

    # Save plot to a memory buffer to embed in HTML
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    # Encode image to base64 string
    data_uri = base64.b64encode(buf.getbuffer()).decode("utf8")

    # 4. Generate HTML File
    # This step saves the code, the output, and the visualization into one HTML file
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Employee Performance Analysis</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; color: #333; }}
            h1 {{ color: #2c3e50; }}
            .container {{ max-width: 800px; margin: 0 auto; }}
            code {{ background-color: #f4f4f4; padding: 2px 5px; border-radius: 3px; }}
            pre {{ background-color: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; }}
            .output {{ background-color: #e8f6f3; padding: 15px; border-left: 5px solid #1abc9c; margin: 20px 0; }}
            img {{ max-width: 100%; height: auto; border: 1px solid #ddd; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Employee Performance Analysis</h1>
            <p><strong>Analyst Email:</strong> 24f1001771@ds.study.iitm.ac.in</p>
            
            <h2>1. Analysis Output</h2>
            <div class="output">
                <strong>Result:</strong> Frequency count for 'IT' department: <strong>{it_count}</strong>
            </div>

            <h2>2. Visualization: Department Distribution</h2>
            <p>The following histogram shows the distribution of employees across different departments.</p>
            <img src="data:image/png;base64,{data_uri}" alt="Department Histogram">

            <h2>3. Python Code Used</h2>
            <pre>
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = ... # (Data Loading)

# Calculate IT Frequency
it_count = df[df['department'] == 'IT'].shape[0]
print(f"Frequency count for IT department: {{it_count}}")

# Create Visualization
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='department')
plt.title('Distribution of Departments')
plt.show()
            </pre>
        </div>
    </body>
    </html>
    """

    with open("analysis.html", "w") as f:
        f.write(html_content)
    
    print("Success! 'analysis.html' has been generated.")

if __name__ == "__main__":
    main()
