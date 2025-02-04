def mean(data_set):
    total_sum = 0
    
    for x in data_set:
        total_sum += x

    return total_sum / len(data_set)

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
           
def main():
   ds = [43, 37, 50, 51, 58, 105, 52, 45, 45, 10]
   sorted_ds = sorted(ds)

   # Question 1 Part A answers

   q1,q2,q3 = quartiles(sorted_ds)
   print(sorted_ds)
   print(f"Mean: {mean(sorted_ds)}")
   print(f"Median: {median(sorted_ds)}")
   print(f"Quartiles: Q1 = {q1}, Q2 = {q2} , Q3 = {q3}")
   print(f"Standard Deviation: {sd(sorted_ds)}")

   # Question 1 Part B/C

   ds_iqr = iqr_rule(sorted_ds,q1,q3)
   iqrQ1,iqrQ2,iqrQ3 = quartiles(ds_iqr)
   print(f"After the 1.5IQR rule the data set is : {ds_iqr}")
   print(f"Mean: {mean(ds_iqr)}")
   print(f"Median: {median(ds_iqr)}")
   print(f"Quartiles: Q1 = {iqrQ1}, Q2 = {iqrQ2} , Q3 = {iqrQ3}")
   print(f"Standard Deviation: {sd(ds_iqr)}")

if __name__ == '__main__':
    main()