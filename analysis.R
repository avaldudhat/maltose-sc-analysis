# ===============================
# Enzyme Kinetics Data Analysis
# ===============================

# 1. Maltose Standard Curve Analysis
# ---------------------------------
maltose_data <- read.csv("MALTOSE SC.csv")
print(maltose_data)  # Display full dataset

# View concentration and absorbance values
maltose_conc <- maltose_data$Concentration
print("Maltose Concentrations:")
print(maltose_conc)

maltose_abs <- maltose_data$abs..control
print("Absorbance Values:")
print(maltose_abs)

# Create Maltose standard curve
plot(x = maltose_data$Concentration, 
     y = maltose_data$abs..control,
     main = "Maltose Standard Curve",
     xlab = "Maltose Concentration",
     ylab = "Absorbance",
     pch = 16,  # Solid circles for data points
     col = "blue")

# 2. Michaelis-Menten Curve Analysis
# ---------------------------------
mm_data <- read.csv("MM CURVE.csv")
print(mm_data)

# Extract kinetics data
starch_conc <- mm_data$Conc.of.starch
print("Starch Concentrations:")
print(starch_conc)

enzyme_activity <- mm_data$Enzyme.activity..mmol.ml.min.
print("Enzyme Activities:")
print(enzyme_activity)

# Plot Michaelis-Menten curve
plot(x = mm_data$Conc.of.starch,
     y = mm_data$Enzyme.activity..mmol.ml.min.,
     main = "Michaelis-Menten Curve",
     xlab = "Starch Concentration",
     ylab = "Enzyme Activity (mmol/ml/min)",
     pch = 16,
     col = "red")

# 3. Lineweaver-Burke Plot Analysis
# --------------------------------
lb_data <- read.csv("LW CURVE.csv")
print(lb_data)

# Extract reciprocal values
inverse_substrate <- lb_data$X1..s.
print("1/[S] Values:")
print(inverse_substrate)

inverse_velocity <- lb_data$X1.V
print("1/V Values:")
print(inverse_velocity)

# Create Lineweaver-Burke plot
plot(x = lb_data$X1..s.,
     y = lb_data$X1.V,
     main = "Lineweaver-Burke Plot",
     xlab = "1/[S]",
     ylab = "1/V",
     pch = 16,
     col = "green")

# 4. pH Effect Analysis
# --------------------
ph_data <- read.csv("PH CURVE.csv")
print(ph_data)

# Extract pH data
buffer_ph <- ph_data$Buffer..different.pH....l.
print("pH Values:")
print(buffer_ph)

ph_activity <- ph_data$enzyme_activity
print("Enzyme Activity at Different pH:")
print(ph_activity)

# Plot pH curve
plot(x = ph_data$Buffer..different.pH....l.,
     y = ph_data$enzyme_activity,
     main = "Effect of pH on Enzyme Activity",
     xlab = "pH",
     ylab = "Enzyme Activity",
     pch = 16,
     col = "purple")

# 5. Temperature Effect Analysis
# ----------------------------
temp_data <- read.csv("TEMP CURVE.csv")
print(temp_data)

# Extract temperature data
temperature <- temp_data$Incubation_temperature_C
print("Temperature Values (°C):")
print(temperature)

temp_activity <- temp_data$EA
print("Enzyme Activity at Different Temperatures:")
print(temp_activity)

# Plot temperature curve
plot(x = temp_data$Incubation_temperature_C,
     y = temp_data$EA,
     main = "Effect of Temperature on Enzyme Activity",
     xlab = "Temperature (°C)",
     ylab = "Enzyme Activity",
     pch = 16,
     col = "orange")