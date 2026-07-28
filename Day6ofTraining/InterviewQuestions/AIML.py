# #
# # from sklearn.linear_model import LinearRegression
# #
# # model = LinearRegression()
# #
# # model.fit(X, y)
# # pred = model.predict([[5]])
# # print(pred)
#
from sklearn.linear_model import LinearRegression
import numpy as np
#
# # Data
X = np.array([20, 25, 30]).reshape(-1, 1)
Y = np.array([100, 150, 200])

# Model
model = LinearRegression()
model.fit(X, Y)

# Prediction
print(model.predict([[35]]))
#
#
#
# #####Salary Prediction
# from sklearn.linear_model import LinearRegression
# import numpy as np
#
# # Experience (years)
# X = np.array([1, 2, 3, 4]).reshape(-1, 1)
#
# # Salary (in thousands)
# Y = np.array([10, 20, 30, 40])
#
# model = LinearRegression()
# model.fit(X, Y)
#
# # Predict salary for 5 years experience
# print(model.predict([[5]]))
#
#
#
# ####Study Hours vs Marks
#
# from sklearn.linear_model import LinearRegression
# import numpy as np
#
# # Study hours
# X = np.array([1, 2, 3, 4]).reshape(-1, 1)
#
# # Marks
# Y = np.array([20, 40, 60, 80])
#
# model = LinearRegression()
# model.fit(X, Y)
#
# # Predict marks for 5 hours study
# print(model.predict([[5]]))
#
#
# ###Product Price Prediction
# from sklearn.linear_model import LinearRegression
# import numpy as np
#
# # Quantity
# X = np.array([1, 2, 3, 4]).reshape(-1, 1)
#
# # Total Price
# Y = np.array([100, 200, 300, 400])
#
# model = LinearRegression()
# model.fit(X, Y)
#
# # Predict price for 6 items
# print(model.predict([[6]]))


##Basic Logistic Regression Code
# Basic Difference (Simple Language)
#
#
# Linear Regression → Predicts numbers (continuous values)
# Logistic Regression → Predicts categories (0/1, Yes/No)
#Linear Regression
# y=mx+b

#Logistic Regression
# p=1/1+e^-z
# Probability (0 to 1)


#Real Life Example
# 🔹 Linear Regression
#
# 👉 Example:
#
# House price prediction
# Salary prediction
#
# 📌 Output:
#
# ₹5,00,000 / ₹10,00,000 (continuous value)
#
# 🔹 Logistic Regression
#
# 👉 Example:
#
# Pass / Fail
# Spam / Not Spam
# Disease / No Disease
#
# 📌 Output:
#
# 0 किंवा 1
#
# ⚠️ 4. Why Both Are Different? (Most Important)
#
# 👉 Student ला असं सांग:
#
# ❌ Linear Regression Problem:
# Output negative येऊ शकतो
# Output 1 पेक्षा जास्त येऊ शकतो
#
# 📌 Example:
#
# Probability = 1.5 ❌ (impossible)
# ✅ Logistic Regression Solution:
# Output नेहमी 0 ते 1 मध्ये
# Valid probability
#
# 🔥 Line:
#
# “Classification problems साठी Logistic Regression वापरतो”
#
# 📈 5. Graph Difference
# Linear Regression → Straight Line 📉
# Logistic Regression → S-Curve (Sigmoid) 📊
#
# 👉 Explain:
#
# Linear = unlimited
# Logistic = bounded (0–1)
# 🧩 6. Output Type
# Feature	Linear Regression	Logistic Regression
# Output	Continuous value	Category (0/1)
# Range	(-∞, +∞)	(0, 1)
# Use	Prediction	Classification
# Graph	Straight line	S-curve
#
# “Linear Regression answers HOW MUCH
# Logistic Regression answers YES or NO”



# Q: Difference between Linear & Logistic Regression?
# Linear Regression is used for predicting
# continuous values, while Logistic Regression is used for
# classification problems. Linear Regression outputs any real value,
# whereas Logistic Regression outputs probabilities between 0 and 1 using a
# sigmoid function.



#Linear → Line → Numbers
# Logistic → Logic → Yes/No



# Step 1: Import libraries
import numpy as np
from sklearn.linear_model import LogisticRegression

# Step 2: Dataset (same as PPT)
X = np.array([1, 2, 3, 5, 7, 9, 10]).reshape(-1, 1)
y = np.array([0, 0, 0, 1, 1, 1, 1])

# Step 3: Create model
model = LogisticRegression()

# Step 4: Train model
model.fit(X, y)

# Step 5: Prediction
print("Prediction for 4 hours:", model.predict([[4]]))

# Step 6: Probability
print("Probability:", model.predict_proba([[4]]))