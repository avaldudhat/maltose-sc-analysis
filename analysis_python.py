import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

# Set the style for all plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# 1. Maltose Standard Curve Analysis
# ---------------------------------
maltose_data = pd.read_csv("MALTOSE SC.csv")
print("\nMaltose Standard Curve Data:")
print(maltose_data.head())

plt.figure()
sns.scatterplot(data=maltose_data, 
                x='Concentration', 
                y='abs..control',
                color='blue',
                s=100)
sns.regplot(data=maltose_data, 
            x='Concentration', 
            y='abs..control',
            scatter=False,
            color='darkblue')
plt.title('Maltose Standard Curve')
plt.xlabel('Maltose Concentration')
plt.ylabel('Absorbance')
plt.show()

# 2. Michaelis-Menten Curve Analysis
# ---------------------------------
mm_data = pd.read_csv("MM CURVE.csv")
print("\nMichaelis-Menten Data:")
print(mm_data.head())

plt.figure()
sns.scatterplot(data=mm_data, 
                x='Conc.of.starch', 
                y='Enzyme.activity..mmol.ml.min.',
                color='red',
                s=100)
sns.regplot(data=mm_data, 
            x='Conc.of.starch', 
            y='Enzyme.activity..mmol.ml.min.',
            scatter=False,
            color='darkred')
plt.title('Michaelis-Menten Curve')
plt.xlabel('Starch Concentration')
plt.ylabel('Enzyme Activity (mmol/ml/min)')
plt.show()

# 3. Lineweaver-Burke Plot Analysis
# --------------------------------
lb_data = pd.read_csv("LW CURVE.csv")
print("\nLineweaver-Burke Data:")
print(lb_data.head())

plt.figure()
sns.scatterplot(data=lb_data, 
                x='X1..s.', 
                y='X1.V',
                color='green',
                s=100)
sns.regplot(data=lb_data, 
            x='X1..s.', 
            y='X1.V',
            scatter=False,
            color='darkgreen')
plt.title('Lineweaver-Burke Plot')
plt.xlabel('1/[S]')
plt.ylabel('1/V')
plt.show()

# 4. pH Effect Analysis
# --------------------
ph_data = pd.read_csv("PH CURVE.csv")
print("\npH Effect Data:")
print(ph_data.head())

plt.figure()
sns.scatterplot(data=ph_data, 
                x='Buffer..different.pH....l.', 
                y='enzyme_activity',
                color='purple',
                s=100)
# Use polynomial regression for pH curve
sns.regplot(data=ph_data, 
            x='Buffer..different.pH....l.', 
            y='enzyme_activity',
            scatter=False,
            color='darkpurple',
            order=2)  # Polynomial fit
plt.title('Effect of pH on Enzyme Activity')
plt.xlabel('pH')
plt.ylabel('Enzyme Activity')
plt.show()

# 5. Temperature Effect Analysis
# ----------------------------
temp_data = pd.read_csv("TEMP CURVE.csv")
print("\nTemperature Effect Data:")
print(temp_data.head())

plt.figure()
sns.scatterplot(data=temp_data, 
                x='Incubation_temperature_C', 
                y='EA',
                color='orange',
                s=100)
# Use polynomial regression for temperature curve
sns.regplot(data=temp_data, 
            x='Incubation_temperature_C', 
            y='EA',
            scatter=False,
            color='darkorange',
            order=2)  # Polynomial fit
plt.title('Effect of Temperature on Enzyme Activity')
plt.xlabel('Temperature (°C)')
plt.ylabel('Enzyme Activity')
plt.show()

# Optional: Add statistical analysis
# --------------------------------
def print_statistics(data, x_col, y_col, analysis_name):
    """Print basic statistical analysis for each dataset"""
    print(f"\nStatistics for {analysis_name}:")
    print(f"Number of observations: {len(data)}")
    print(f"\nDescriptive statistics for {x_col}:")
    print(data[x_col].describe())
    print(f"\nDescriptive statistics for {y_col}:")
    print(data[y_col].describe())

print_statistics(maltose_data, 'Concentration', 'abs..control', 'Maltose Standard Curve')
