from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

gbm = GradientBoostingClassifier(n_estimators=10)
rf=RandomForestClassifier()
logr = LogisticRegression()
nb=GaussianNB()
dt=tree.DecisionTreeClassifier()
# knn=KNeighborsClassifier(n_neighbors=5)
df = pd.read_csv("C:/Users/tanma/PycharmProjects/dataset/Iris.csv")
# print(df)

X=df.drop('Id',axis=1)
X=X.drop('Species',axis=1)
y=df['Species']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=1)

gbm.fit(X_train, y_train)
y_pred=gbm.predict(X_test)

print("accuracy_score:",accuracy_score(y_test,y_pred))
print("confusion_matrix:",confusion_matrix(y_test,y_pred))
print("classification_report:",classification_report(y_test,y_pred))
print("accuracy_score:", accuracy_score(y_test,y_pred))



