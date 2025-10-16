import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")
gender_df = pd.read_csv("gender_submission.csv")

print("Train Data")
print(train_df.head)

print("\nTest Data")
print(test_df.head)

print(train_df.info())

print("\nMissing Values per column:")
print(train_df.isnull().sum())

print("\nSummary Statistics")
print(train_df.describe())

print("\nUnique Values in categorical columns:")
print(train_df.nunique())

#Filling missing Age with median
train_df.loc[:, "Age"] = train_df["Age"].fillna(train_df["Age"].median(), inplace=True)

#Filling missing Embarked with the most frequent value
train_df.loc[:, "Embarked"] = train_df["Embarked"].fillna(train_df["Embarked"].mode()[0], inplace=True)

#Drop Cabin because it has too many missing values
train_df.drop("Cabin", axis=1, inplace=True)

print(train_df.isnull().sum())

sns.countplot(x="Sex", hue="Survived", data=train_df)
plt.title("Survival Count by Gender")
plt.show()

sns.countplot(x="Pclass", hue="Survived", data=train_df)
plt.title("Survival Count by Passenger Class")
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(train_df["Age"], bins=30, kde=True)
plt.title("Age Distribution")
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(train_df.corr(), annot=True, cmap = "coolwarm")
plt.title("Correlation Heatmap")
plt.show

print(train_df[["Pclass", "Survived"]].groupby("Pclass").mean())
print(train_df[["Sex", "Survived"]].groupby("Sex").mean())
print(train_df[["Embarked", "Survived"]].groupby("Embarked").mean())

merged_df = test_df.merge(gender_df, on="PassengerId", how="left")
print(merged_df.head())