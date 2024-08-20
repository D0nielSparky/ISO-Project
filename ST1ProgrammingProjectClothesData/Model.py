import matplotlib.pyplot as pyplot
import pandas as pd
import sklearn
from matplotlib import pyplot as plt
from sklearn import preprocessing
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay, roc_auc_score, roc_curve, \
    accuracy_score
from sklearn.model_selection import KFold, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

# Importing dataframe from file
clothes_data = pd.read_csv("clothesData.csv")

# Variable for prediction
predict = "target"

le = preprocessing.LabelEncoder()
brand = le.fit_transform(list(clothes_data["Brand"]))
category = le.fit_transform(list(clothes_data["Category"]))
color = le.fit_transform(list(clothes_data["Color"]))
size = le.fit_transform(list(clothes_data["Size"]))
material = le.fit_transform(list(clothes_data["Material"]))
target = le.fit_transform(list(clothes_data["Price"]))

x = list(zip(brand, category, color, size, material))
y = list(target)
num_folds = 5
seed = 7
scoring = "accuracy"

# Model Test/Train
# Splitting what we are trying to predict into 4 different arrays:
# x_train, x_test, y_train and y_test
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.20, random_state=seed)
# test_size being .20 will split 20% of the data into test samples.

# Checking with different Scikit-learn classification algorithms
models = [("DT", DecisionTreeClassifier()), ("NB", GaussianNB()), ("SVM", SVC()), ("GBM", GradientBoostingClassifier()),
          ("RF", RandomForestClassifier())]
# Evaluate each model in turn
results = []
names = []

for name, model in models:
    k_fold = KFold(n_splits=num_folds, shuffle=True, random_state=seed)
    cv_results = cross_val_score(model, x_train, y_train, cv=k_fold, scoring="accuracy")
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    msg += "\n"
    print(msg)

# Comparing Performance of Algorithms
fig = pyplot.figure()
fig.suptitle("Algorithm Comparison")
ax = fig.add_subplot(111)
pyplot.boxplot(results)
ax.set_xticklabels(names)
pyplot.show()

# Make predictions on validation/test dataset
dt = DecisionTreeClassifier()
nb = GaussianNB()
gb = GradientBoostingClassifier()
rf = RandomForestClassifier()

best_model = rf
best_model.fit(x_train, y_train)
y_pred = best_model.predict(x_test)
model_accuracy = accuracy_score(y_test, y_pred)
print("Best Model Accuracy Score on Test Set:", model_accuracy)

# Model Evaluation Metric 1
print(classification_report(y_test, y_pred))
"""
# Model Evaluation Metric 2
# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()
"""
# Model Evaluation metric 3
best_model = rf
best_model.fit(x_train, y_train)
rf_roc_auc = roc_auc_score(y_test, best_model.predict(x_test))
fpr, tpr, thresholds = roc_curve(y_test, best_model.predict_proba(x_test)[:, 1])

plt.figure()
plt.plot(fpr, tpr, label="Random Forest(area = %0.2f)" % rf_roc_auc)
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False positive rate")
plt.ylabel("True positive rate")
plt.title("Receiver Operating Characteristic")
plt.legend(loc="lower right")
plt.savefig("LOC_ROC")
plt.show()

# Check actual/ground truth vs predicted diagnosis
for x in range(len(y_pred)):
    print("Predicted: ", y_pred[x], "Actual: ", y_test[x], "Data: ", x_test[x],)
