from sklearn.metrics import classification_report
# precision-recall curve and f1
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import f1_score
from sklearn.metrics import auc
from sklearn.metrics import average_precision_score
from matplotlib import pyplot
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd
from sklearn.preprocessing import label_binarize
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt

from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
from sklearn.metrics import accuracy_score
from scikitplot.metrics import plot_confusion_matrix



#MATRICE DI CONFUSIONE
filename_glass = "25 training.xlsx"
df_glass = pd.read_excel(filename_glass)

filename_glass2 = "25 test.xlsx"
df_glass2 = pd.read_excel(filename_glass2)

y_col_glass = 'Persona'
x_cols_glass = list(df_glass.columns.values)
x_cols_glass.remove(y_col_glass)

X_train = df_glass[x_cols_glass].values
Y_train = df_glass[y_col_glass]

X_test = df_glass2[x_cols_glass].values
Y_test = df_glass2[y_col_glass]

classifier = KNeighborsClassifier()
y_pred = classifier.fit(X_train, Y_train).predict(X_test)

accuracy = accuracy_score(Y_test, y_pred)
print("Accuratezza: ", accuracy)

plot_confusion_matrix(Y_test, y_pred)
plt.show()



'''
#Precisio,Recall, f1-score, support
filename_glass = "Dataset-grande-training.xlsx"
df_glass = pd.read_excel(filename_glass)

filename_glass2 = "Dataset-grande-test.xlsx"
df_glass2 = pd.read_excel(filename_glass2)

y_col_glass = 'Persona'
x_cols_glass = list(df_glass.columns.values)
x_cols_glass.remove(y_col_glass)

X_train = df_glass[x_cols_glass].values
Y_train = df_glass[y_col_glass]

X_test = df_glass2[x_cols_glass].values
Y_test = df_glass2[y_col_glass]



target_names = ['Classe1', 'Classe2','Classe3','Classe4', 'Classe5','Classe6','Classe7','Classe8','Classe9','Classe10','Classe11','Classe12',
                'Classe13', 'Classe14','Classe15','Classe16', 'Classe17','Classe18','Classe19', 'Classe20','Classe21','Classe22',
                'Classe23', 'Classe33', 'Classe34', 'Classe35', 'Classe36', 'Classe37','Classe24', 'Classe25', 'Classe26', 'Classe27', 'Classe28', 'Classe29', 'Classe30','Classe31', 'Classe32',
                 'Classe39', 'Classe40', 'Classe41', 'Classe42',
                'Classe43', 'Classe44', 'Classe45', 'Classe46', 'Classe47', 'Classe48', 'Classe49', 'Classe50', 'Classe51', 'Classe52',
                'Classe53', 'Classe54','Classe55']

# Run classifier, using a model that is too regularized (C too low) to see
# the impact on the results
classifier = KNeighborsClassifier()
y_pred = classifier.fit(X_train, Y_train).predict(X_test)
print(classification_report(Y_test,y_pred,target_names=target_names))
'''



