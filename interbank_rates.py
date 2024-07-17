import pandas as pd
df=pd.read_csv("assets/data/Inter_Bank_Rates.csv")

#drop all rows with null values and rows with value "-" and (%)
df.drop(df[df['Overnight_rate'] =='-'].index, inplace = True)
df.drop(df[df['7_day_rate'] =='-'].index, inplace = True)
df.drop(df[df['Overall_rate'] =='-'].index, inplace = True)



df.dropna(inplace = True)


#converting date column from string/object to date and time,
   # i realised there were white spaces in key namesso have to remove them first(remove space in column names using strip() function)
   df.rename(columns=lambda x: x.strip(), inplace=True)
   print(df.keys())

# format date type
df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')

#renaming coumn names
df = df.rename(columns={'Overnight  (%)': 'Overnight_rate', '7day_rate': 'Seven_day_rate', 'Overall (%)':'Overall_rate'})

#change other interest columns types to float
df["Overnight_rate"] = df.Overnight_rate.astype(float)
df["Seven_day_rate"] = df. Seven_day_rate.astype(float)

#replace valuve with (%) in overall_rate column
df["Overall_rate"]=df["Overall_rate"].str.replace("%","",regex=False).astype(float)

# summary statistics (mean, median, standard deviation).for rate grouped by year
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import statistics

summary_stats=df.describe() 
print(summary_stats)
# mean calculatioon by month of each year

df.set_index('Date', inplace=True)
monthly_mean =df.resample('ME').mean().plot(
    kind='line',
    xlabel="Year (Spread over Months)",
    ylabel="Mean Inter Bank Rates",
    title="Average Inter Bank Rates Spread over Months"
)
plt.show();

monthly_mean.to_csv('assets/data/interbank_rates_means_by_month.csv')
print(monthly_mean)

# mean calculatioon by each year
df.set_index('Date', inplace=True)
annual_mean =df.resample('YE').mean().plot(
    kind='line',
    xlabel="Years",
    ylabel="Mean Inter Bank Rates",
    title="Average Inter Bank over Years"
)
plt.show()
annual_mean.to_csv('assets/data/interbank_rates_annualmeans.csv')
print(annual_mean)

#breaking down my analysis to a period of 12 months (july 2023 - june 2024)
# mean, median ,SD calculations by month 


df.info()
df.head
df.to_csv('sample', index=False)
