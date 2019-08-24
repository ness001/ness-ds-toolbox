from sklearn import metrics
print metrics.classification_report(y_test, credit_pred)
print metrics.confusion_matrix(y_test, credit_pred)
print metrics.accuracy_score(y_test, credit_pred)