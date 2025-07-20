import pandas as pd
df = pd.read_csv("C:\\Users\\hp\\OneDrive\\文档\\global_housing_market_extended.csv")
def print5rows():
 print(df.head(5))

print5rows()
def last5rows():
    print(df.tail(5))

last5rows()
def size():
    rows,cols=df.shape
    print(f"The dataset has {rows} rows and {cols} columns.")

size()
print(df.columns)
print(df.info())
"""
The line df.set_index('Country', inplace=True) in Python with the pandas library
 modifies the DataFrame df by setting the column 'Country' as its index. 
 The inplace=True argument ensures that the changes are made directly 
 to the original DataFrame, rather than creating a new one. 
 This operation is useful for accessing and manipulating data 
 based on the 'Country' values, as the index provides a way to label 
 and reference rows.
 """
df.set_index('Country', inplace=True)
first=df.loc["USA"]
print(first)
print("-"*30)
last_row = df.iloc[-1] 
print(last_row)

def subset():
    selected_col=input("enter the column you want in new subset , separated")
    new_df=df[[col.strip() for col in selected_col.split(",")]].copy()
    print(new_df)

#subset()
import matplotlib.pyplot as plt
def plot_gdp_by_country():
    plt.figure(figsize=(12, 5))
    df_sorted = df.sort_values('GDP Growth (%)',ascending=False).head(10)
    plt.bar(df_sorted.index, df_sorted['GDP Growth (%)'])
    plt.title('Top 10 Countries by GDP')
    plt.xlabel('Country')
    plt.ylabel('GDP Growth (%)')
    plt.show()

plot_gdp_by_country()

def scatterplot_hpivsar():
   plt.figure(figsize=(10, 6))
   plt.scatter(df['House Price Index'], df['Affordability Ratio'])
   plt.title('House Price Index vs Affordability Ratio')
   plt.xlabel('House Price Index')
   plt.ylabel('Affordability Ratio')
   plt.show()

scatterplot_hpivsar()

def boxplot():
    plt.figure(figsize=(12,5))
    plt.boxplot(df['GDP Growth (%)'],patch_artist=True)
    plt.title('gdp growth')
    plt.xlabel('GDP Growth (%)')  # Label the x-axis
    plt.show()

boxplot()

def plot_pie_chart_gdp_growth():
    # Grouping GDP Growth by country and taking the average of each country's GDP Growth
    country_gdp_growth = df.groupby('Country')['GDP Growth (%)'].mean()  # You can also use sum() or other aggregations
    plt.figure(figsize=(10, 8))

    # Plotting the pie chart
    plt.pie(country_gdp_growth, labels=country_gdp_growth.index, autopct='%1.1f%%')
    plt.title('GDP Growth (%) by Country (Average)')
    # plt.axis('equal')  # Equal aspect ratio ensures the pie chart is a circle.
    plt.show()

# Example function call
plot_pie_chart_gdp_growth()
    