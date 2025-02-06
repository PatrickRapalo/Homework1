####### IMPORT BLOCK #######

import pandas as pd
import matplotlib.pyplot as plt

####### Q1 BLOCK #######

def mean(data_set):
    n = len(data_set)
    total_sum = 0
    
    for x in data_set:
        total_sum += x

    return total_sum / n

def median(data_set):
   n = len(data_set)

   if n % 2 == 0:
       total = data_set[int(n/2) -1] + data_set[int(n / 2)]
       middle = total / 2
       return middle
   else:
       return data_set[n//2] 

def quartiles(data_set):
   n = len(data_set)
   lower_half = data_set[:n // 2]
   upper_half = data_set[(n + 1) // 2:]

   q1 = median(lower_half)
   q3 = median(upper_half)

   q2 = median(data_set) 
  
   return q1,q2,q3

def sd(data_set):
   n = len(data_set)
   total = 0
   total_sqrd = 0

   for x in data_set:
       total += x
       total_sqrd += x**2
    
   variance = ((n*total_sqrd) - (total **2)) / (n *(n-1))
   sd = variance ** 0.5

   return round(sd,1)

def iqr_rule(data_set,q1,q3):
   iqr = 1.5*(q3 -q1)
   lower_outlier = q1 - iqr
   higher_outlier = q3 + iqr

   for x,i in enumerate(data_set):
       if i < lower_outlier or x > higher_outlier:
           del data_set[x]

   return data_set

def question1():
   
   print("###### QUESTION 1 ######")
   print('')
  
   ds = [43, 37, 50, 51, 58, 105, 52, 45, 45, 10]
   #Sorting the data set for future use
   sorted_ds = sorted(ds)

   
   q1,q2,q3 = quartiles(sorted_ds)
   print(sorted_ds)
   print(f"Mean: {mean(sorted_ds)}")
   print(f"Median: {median(sorted_ds)}")
   print(f"Quartiles: Q1 = {q1}, Q2 = {q2} , Q3 = {q3}")
   print(f"Standard Deviation: {sd(sorted_ds)}")
   print('')

   # Question 1 Part B/C
   # Setting the new Data set to ds_iqr becasue of the post IQR rule
   ds_iqr = iqr_rule(sorted_ds,q1,q3)
   
   iqrQ1,iqrQ2,iqrQ3 = quartiles(ds_iqr)
   print(f"After the 1.5IQR rule the data set is : {ds_iqr}")
   print(f"Mean: {mean(ds_iqr)}")
   print(f"Median: {median(ds_iqr)}")
   print(f"Quartiles: Q1 = {iqrQ1}, Q2 = {iqrQ2} , Q3 = {iqrQ3}")
   print(f"Standard Deviation: {sd(ds_iqr)}")
   print('')


####### Q2 BLOCK #######

def time_series_population(df):
    plt.plot(df["year"],df["population"])
    plt.title("Population Growth (US)")
    plt.xlabel("Year")
    plt.ylabel("Population (Millions)")
    plt.show()

def time_series_increment_x(df):
    plt.plot(df["year"],df["increment"])
    plt.title("Relative Change in Population(US)")
    plt.xlabel("Year")
    plt.ylabel("Population Change (Millions)")
    plt.show()

def time_series_increment_y(df):
    plt.plot(df["year"],df["increment"])
    plt.title("Relative Change in Population(US)")
    plt.xlabel("Year")
    plt.ylabel("Population Change (%)")
    plt.show()

def ten_year_increment_x(df):
    df["increment"] = df["population"].diff()
    df = df.dropna()
    return df

def ten_year_increment_y(df):
    increment = []
    for x in range(1,len(df["population"])):
        increment.append(round((df["population"][x] - df["population"][x-1]) / df["population"][x],3))

    df = df.drop(0)
    df ["increment"] = increment

    return df

def compute_sample_analytics(df):
    mean_increment = round(df["increment"].mean(),1)
    median_increment = round(df["increment"].median(),1)
    variance_increment = round(df["increment"].var(),4)

    print(f"Mean Increment: {mean_increment}")
    print(f"Median Increment: {median_increment}")
    print(f"Variance of Increments: {variance_increment}")

    return None

def question2():

    print("###### QUESTION 2 ######")
    print('')

    data = {
        "year": [1790,1800,1810,1820,1830,1840,1850,1860,1870,1880,1890,1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000],
        "population" : [3.9,5.3,7.2,9.6,12.9,17.1,23.2,31.4,38.6,50.2,63.0,76.2,92.2,106.0,123.2,132.2,151.3,179.3,203.3,226.5,248.7,281.4]
    }
    
    df = pd.DataFrame(data)
    time_series_population(df)

    df_increment_x = ten_year_increment_x(df)
    time_series_increment_x(df_increment_x)

    df_increment_y = ten_year_increment_y(df)
    time_series_increment_y(df_increment_y)

    print("Sample Analytics for increment of X: ")
    compute_sample_analytics(df_increment_x)
    print("")
    print("Sample Analytics for increment of Y: ")
    compute_sample_analytics(df_increment_y)
    print('')


####### Q3 BLOCK #######

def iqr_rule2(q1,q3):
    iqr = 1.5*(q3 -q1)
    lower_outlier = round(q1 - iqr,3)
    higher_outlier = round(q3 + iqr,3)

    print(lower_outlier, higher_outlier)

def bxplot(data_set):
    box_data = [[data_set["Min"],data_set["Q1"], data_set["Median"], data_set["Q3"], data_set["Max"]]]

    # Create the boxplot
    fig, ax = plt.subplots()
    ax.boxplot(box_data, vert=True, showfliers=False)  # `showfliers=False` to avoid outliers since we don’t have them

    # Label the plot
    ax.set_xticklabels(["Data"])
    ax.set_title("Boxplot from Summary Statistics")
    ax.set_ylabel("Value")

    # Show the plot
    plt.show()
    
def question3():
    print("###### QUESTION 3 ######")
    print('')

    data_setA = {
        "Min" : 0.066,
        "Q1" : 1.42,
        "Median" : 2.60,
        "Q3" : 6.02,
        "Max" : 10.08
    }
    data_setB = {
        "Min" : -2.235,
        "Q1" : 5.27,
        "Median" : 8.03,
        "Q3" : 9.13,
        "Max" : 10.51
    }

    # IQR rule for both data sets
    iqr_rule2(data_setA["Q1"],data_setA["Q3"])
    iqr_rule2(data_setB["Q1"],data_setB["Q3"])

    ''' 
    Since Data Set B is not usable I will only 
    create a box plot for Data Set A
    '''   

    input("Press Enter for Boxplot")

    bxplot(data_setA)
    print('')


####### Q4 BLOCK #######

def histplot(data_set):

    plt.hist(data_set, bins= 10)
    plt.title("Total Users Logins (Per Month)")
    plt.ylabel("Frequency")
    plt.xlabel("Logins (Thousands)")
    plt.show()

def question4():

    print("###### QUESTION 4 ######")
    print('')

    ds = [56,52,13,34,33,18,44,41,48,75,24,19,35,27,46,62,71,24,66,94,40,18,15,39,53,23,41,78,15,35]

    histplot(ds)

    print(f"Mean: {mean(ds)}")
    print(f"Median: {median(ds)}")


####### MAIN BLOCK #######

def main():

    question1()
    input("Press Enter to proceed to the next question...\n")
    
    question2()
    input("Press Enter to proceed to the next question...\n")
    
    question3()
    input("Press Enter to proceed to the next question...\n")
    
    question4()
   

if __name__ == '__main__':
    main()