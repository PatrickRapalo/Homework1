import pandas as pd
import matplotlib.pyplot as plt


def time_series_population(df):
    plt.plot(df["year"],df["population"])
    plt.title("Population Growth (US)")
    plt.xlabel("Year")
    plt.ylabel("Population (Millions)")
    plt.show()

def time_series_increment(df):
    plt.plot(df["year"],df["increment"])
    plt.title("Population Growth (US)")
    plt.xlabel("Year")
    plt.ylabel("Population (Millions)")
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

def main():
    data = {
        "year": [1790,1800,1810,1820,1830,1840,1850,1860,1870,1880,1890,1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000],
        "population" : [3.9,5.3,7.2,9.6,12.9,17.1,23.2,31.4,38.6,50.2,63.0,76.2,92.2,106.0,123.2,132.2,151.3,179.3,203.3,226.5,248.7,281.4]
    }
    
    df = pd.DataFrame(data)
    time_series_population(df)

    df_inrement_x = ten_year_increment_x(df)
    time_series_increment(df_inrement_x)

    df_increment_y = ten_year_increment_y(df)
    time_series_increment(df_increment_y)

    print("Sample Analytics for increment of X: ")
    compute_sample_analytics(df_inrement_x)
    print("")
    print("Sample Analytics for increment of Y: ")
    compute_sample_analytics(df_increment_y)
    
if __name__ == "__main__":
    main()