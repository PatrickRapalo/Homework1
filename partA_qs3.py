####### IMPORT BLOCK #######
import matplotlib.pyplot as plt

def iqr_rule(q1,q3):
    iqr = 1.5*(q3 -q1)
    lower_outlier = round(q1 - iqr,3)
    higher_outlier = round(q3 + iqr,3)

    print(lower_outlier, higher_outlier)

def bxplot(data_set):
    plt.boxplot(data_set)
    plt.show()

def main():
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
    iqr_rule(data_setA["Q1"],data_setA["Q3"])
    iqr_rule(data_setB["Q1"],data_setB["Q3"])

    ''' 
    Since Data Set B is not usable I will only 
    create a box plot for Data Set A
    '''   

    bxplot(data_setA)



if __name__ == "__main__":
    main()