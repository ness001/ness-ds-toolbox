class_weights = {1:1, 2:4}
credit_model_cost = DecisionTreeClassifier(maxx_depth=6,class_weight = class_weights)
credit_model_cost.fit(X_train, y_train)
credit_pred_cost = credit_model_cost.predict(X_test)

print metrics.classification_report(y_test, credit_pred_cost)
print metrics.confusion_matrix(y_test, credit_pred_cost)
print metrics.accuracy_score(y_test, credit_pred_cost)