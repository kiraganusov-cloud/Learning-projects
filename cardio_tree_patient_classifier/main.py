import pandas as pd
import GWCutilities as util
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

print("\n-----\n")


#Create a variable to read the dataset
df = pd.read_csv("heartDisease_2020_sampling.csv")
print(
    "We will be performing data analysis on this Indicators of Heart Disease Dataset. Here is a sample of it: \n"
)

#Print the dataset's first five rows
print(df.head())

input("\n Press Enter to continue.\n")


#Data Cleaning
#Label encode the dataset
df = util.labelEncoder(df, ["HeartDisease","Smoking","AlcoholDrinking","Sex","AgeCategory","PhysicalActivity","GenHealth"])
print("\nHere is a preview of the dataset after label encoding. \n")
print(df.head())

input("\nPress Enter to continue.\n")


#One hot encode the dataset
df = util.oneHotEncoder(df,["Race"])

print(
    "\nHere is a preview of the dataset after one hot encoding. This will be the dataset used for data analysis: \n"
)
print(df.head())

input("\nPress Enter to continue.\n")



#Creates and trains Decision Tree Model

X = df.drop("HeartDisease",axis = 1)
y = df["HeartDisease"]

X_train, X_test, y_train, y_test = train_test_split(X,y)



from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(max_depth = 2, class_weight = "balanced")
clf = clf.fit(X_train, y_train)


#Test the model with the testing data set and prints accuracy score
test_predications = clf.predict(X_test)
test_acc = accuracy_score(y_test, test_predications)
print("The accuracy with the testing data set of the decisions tree is: " + str(test_acc))

#Prints the confusion matrix
cm = confusion_matrix(y_test, test_predications, labels = [1,0])
print("The confusion matrix of the tree is: ")
print(cm)


#Test the model with the training data set and prints accuracy score
train_predications = clf.predict(X_train)
train_acc = accuracy_score(y_train, train_predications)
print("The accuracy with the training data set of the decisions tree is: " + str(train_acc))



input("\nPress Enter to continue.\n")



#Prints another application of Decision Trees and considerations
print("\nBelow is another application of decision trees and considerations for using them:\n")

print("A decision tree could also be used as a dog breed classifier system. A couple of the factors that could be included are color, size, and ear type.")


#Prints a text representation of the Decision Tree
print("\nBelow is a text representation of how the Decision Tree makes choices:\n")
input("\nPress Enter to continue.\n")

print("Older aged people with poor general health tend to have heart disease")

util.printTree(clf, X.columns)