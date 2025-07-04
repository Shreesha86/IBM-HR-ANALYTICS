import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("ibmHr.csv")

sns.set(style="whitegrid")

# 1. Attrition Distribution
sns.countplot(x='Attrition', hue='Attrition', data=df, palette='Set2', legend=False)
plt.title('Attrition Distribution')
plt.show()

# 2. Attrition by Department
sns.countplot(x='Department', hue='Attrition', data=df, palette='pastel')
plt.title('Attrition by Department')
plt.xticks(rotation=45)
plt.show()

# 3. Monthly Income by Job Role
plt.figure(figsize=(10, 6))
sns.boxplot(x='JobRole', y='MonthlyIncome', data=df)
plt.title('Monthly Income by Job Role')
plt.xticks(rotation=45)
plt.show()


