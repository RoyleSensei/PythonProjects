from lib2to3.pgen2.pgen import DFAState
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set_theme(style="darkgrid")

class LinearRegression():
    

    def fit(self, x_list, y_list):

        '''
        Target: y=kx+b
        k = slope = upper / lower 
        b = intercept 

        upper = sum((x_i - x_mean)(y_i - y_mean))
        lower = sum((x_i - x_mean)**2)

        '''
        x_mean = self.mean(x_list)
        y_mean = self.mean(y_list)

        n = len(x_list)
        upper = 0
        for i in range(n):
            upper += (x_list[i] - x_mean)*(y_list[i]-y_mean)

        lower = 0
        for i in range(n):
            lower += (x_list[i] - x_mean)**2


        self.slope = upper/lower 
        # b = y-kx [y_predicted]
        self.intercept = y_mean - self.slope * x_mean

    def mean(self, lst):
        return sum(lst)/len(lst)


    def predict(self, x):
        '''
        predict y_predicted = kx + b 
        on linear regression

        k = self.slope
        b = self.intercept

        '''
        return self.slope*x + self.intercept

    
    def rsquared(self, x_list , y_list):
        '''
        r^2 = sum((y_i - y_mean)^2) - sum((y_predicted_i - y_i)^2) /sum((y_i - y_mean)^2)

        top_r1 = sum((y_i - y_mean)^2) 
        top_r2 = sum((y_predicted - y_i)^2)
        bot_r = sum((y_i - y_mean)^2)
        
        '''
        n = len(y_list)
        top_r1 = 0
        y_mean = sum(y_list)/len(y_list)
        for i in range(n):
            top_r1 += (y_list[i] - y_mean)**2

        top_r2 = 0
        for i in range(n):
            top_r2 += (self.predict(x_list[i]) - y_list[i])**2

        return (top_r1 - top_r2) / top_r1



class Graph():

    def plot(self, x_list, y_list):
        d = {'total_bill':x_list, 'tip': y_list}
        df = pd.DataFrame(data=d)
        print(df)

        #sns.jointplot(x = 'x', y = 'y', data = df, kind='reg', color='m')
        sns.jointplot(x="total_bill", y="tip", data=df, kind='reg')
        plt.show()

