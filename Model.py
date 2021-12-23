#RFE
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm 
from statsmodels.stats.outliers_influence import variance_inflation_factor


lm = LinearRegression()
lm.fit(X_train,y_train)
rfe = RFE(lm, 10)
rfe = rfe.fit(X_train, y_train)

list(zip(X_train.columns,rfe.support_,rfe.ranking_))

X_train.columns[rfe.support_]

X_train_rfe = X_train[X_train.columns[rfe.support_]]
X_train_rfe.head()

def build_model(X,y):
    X = sm.add_constant(X) #Adding the constant
    lm = sm.OLS(y,X).fit() # fitting the model
    print(lm.summary()) # model summary
    return X
    
def checkVIF(X):
    vif = pd.DataFrame()
    vif['Features'] = X.columns
    vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    vif['VIF'] = round(vif['VIF'], 2)
    vif = vif.sort_values(by = "VIF", ascending = False)
    return(vif)
  
  #model 1
  X_train_new = build_model(X_train_rfe,y_train)
  X_train_new = X_train_rfe.drop(["twelve"], axis = 1)
  
  #model 2
  
  X_train_new = build_model(X_train_new,y_train)
  X_train_new = X_train_new.drop(["fueleconomy"], axis = 1)
  
  #model 3
  X_train_new = build_model(X_train_new,y_train)
  
  #Calculating the Variance Inflation Factor
checkVIF(X_train_new)
X_train_new = X_train_new.drop(["curbweight"], axis = 1)

#model 4
X_train_new = build_model(X_train_new,y_train)
checkVIF(X_train_new)
X_train_new = X_train_new.drop(["sedan"], axis = 1)

#model 5
X_train_new = build_model(X_train_new,y_train)
checkVIF(X_train_new)
X_train_new = X_train_new.drop(["wagon"], axis = 1)

#model 6

X_train_new = build_model(X_train_new,y_train)
checkVIF(X_train_new)
#Dropping dohcv to see the changes in model statistics
X_train_new = X_train_new.drop(["dohcv"], axis = 1)
X_train_new = build_model(X_train_new,y_train)
checkVIF(X_train_new)

#analysis of model
lm = sm.OLS(y_train,X_train_new).fit()
y_train_price = lm.predict(X_train_new)
# Plot the histogram of the error terms
fig = plt.figure()
sns.distplot((y_train - y_train_price), bins = 20)
fig.suptitle('Error Terms', fontsize = 20)                  
# Plot heading 
plt.xlabel('Errors', fontsize = 18)   
