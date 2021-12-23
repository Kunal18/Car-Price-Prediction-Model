#Scaling the test set
num_vars = ['wheelbase', 'curbweight', 'enginesize', 'boreratio', 'horsepower','fueleconomy','carlength','carwidth','price']
df_test[num_vars] = scaler.fit_transform(df_test[num_vars])


#Dividing into X and y
y_test = df_test.pop('price')
X_test = df_test

# use our model to make predictions.
X_train_new = X_train_new.drop('const',axis=1)
# Creating X_test_new dataframe by dropping variables from X_test
X_test_new = X_test[X_train_new.columns]

# Add constant variable 
X_test_new = sm.add_constant(X_test_new)

# predictions
y_pred = lm.predict(X_test_new)

from sklearn.metrics import r2_score 
r2_score(y_test, y_pred)

#EVALUATE THE MODEL
# Plotting y_test and y_pred.
fig = plt.figure()
plt.scatter(y_test,y_pred)
fig.suptitle('y_test vs y_pred', fontsize=20)              # Plot heading 
plt.xlabel('y_test', fontsize=18)                          # X-label
plt.ylabel('y_pred', fontsize=16)   

print(lm.summary())
