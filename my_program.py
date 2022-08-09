from my_module import LinearRegression, Graph

x_list =[70.38, 223.56, 132.48, 182.16 ,204.93, 105.57]
y_list=[10.35, 35.19, 22.77, 16.56, 28.98, 10.35]


lr = LinearRegression()
lr.fit(x_list, y_list) 

#----Y Prediction
y_prediction = round(lr.predict(200),2)
print("Y prediction is: ", y_prediction)

#---R_squared
R_Squared = lr.rsquared(x_list , y_list)
print("R_Squared is: ", R_Squared)

#---Show Graph
graph = Graph()
graph.plot(x_list, y_list)