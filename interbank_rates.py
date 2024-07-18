import pandas as pd
df=pd.read_csv("assets/data/Inter_Bank_Rates.csv")

#converting date column from string/object to date and time,
   # i realised there were white spaces in key namesso have to remove them first(remove space in column names using strip() function)
   df.rename(columns=lambda x: x.strip(), inplace=True)
   print(df.keys())
#renaming coumn names
df = df.rename(columns={'Overnight  (%)': 'Overnight_rate', '7-day (%)': 'Seven_day_rate', 'Overall (%)':'Overall_rate'})


#drop all rows with null values and rows with value "-" and (%)
df.drop(df[df['Overnight_rate'] =='-'].index, inplace = True)
df.drop(df[df['Seven_day_rate'] =='-'].index, inplace = True)
df.drop(df[df['Overall_rate'] =='-'].index, inplace = True)

df.dropna(inplace = True)


# format date type
df['Date'] = pd.to_datetime(df['Date'],format='%d-%b-%y')
df.info()
df.head()

#change other interest columns types to float
df["Overnight_rate"] = df.Overnight_rate.astype(float)
df["Seven_day_rate"] = df. Seven_day_rate.astype(float)

#replace valuve with (%) in overall_rate column
df["Overall_rate"]=df["Overall_rate"].str.replace("%","",regex=False).astype(float)

df.to_csv('assets/data/Inter_Bank_Rates_Python_Cleaned.csv', index=False)

# summary statistics (mean, median, standard deviation).for rate grouped by year
df1=pd.read_csv('assets/data/Inter_Bank_Rates_Python_Cleaned.csv')
df1['Date'] = pd.to_datetime(df1['Date'],format='%Y-%m-%d')

df1.info()
df1.head()

import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import statistics

summary_stats=df1.describe().round(3)
print(summary_stats)
summary_stats.to_csv('assets/data/entire_df_summary_stats.csv',index =False)
df1.info()
# mean calculatioon by month of each year
df1.set_index('Date',inplace=True)
monthly_mean =df1.resample('ME').mean().round(3).plot(
    kind='line',
    xlabel="Year (Spread over Months)",
    ylabel="Mean Inter Bank Rates",
    title="Average Inter Bank Rates Spread over Months"
)
plt.show();
df1.info()
monthly_mean.to_csv('assets/data/interbank_rates_means_by_month.csv')
print(monthly_mean)

# mean calculatioon by each year
annual_mean =df.resample('YE').mean().round(3).plot(
    kind='line',
    xlabel="Years",
    ylabel="Mean Inter Bank Rates",
    title="Average Inter Bank Rates over Years"
)
plt.show()
annual_mean.to_csv('assets/data/interbank_rates_annualmeans.csv')
print(annual_mean)

#breaking down my analysis to a period of 12 months (july 2023 - june 2024)

#1ST FILTER DATA FOR THE PERIOD JULY 2023-JUNE 2024, AND EXTRACT IN NEW CSV
df=pd.read_csv("assets/data/Inter_Bank_Rates_Python_Cleaned.csv")
start_date = '2023-07-01'
end_date = '2024-06-30'

filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

filtered_df.set_index('Date', inplace=True)

filtered_df.to_csv('assets/data/inter_bank_rates_july23_june24.csv')

# mean, median ,SD calculations on period 2023-2024
df_june24=pd.read_csv('assets/data/inter_bank_rates_july23_june24.csv')
df_june24['Date'] = pd.to_datetime(df_june24['Date'])

df_june24.info()

import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import statistics

#General Stats for 2023-2024
fy_summary_stats=df_june24.describe().round(3)
print(fy_summary_stats)
fy_summary_stats.to_csv('assets/data/fy_summary_stats.csv',index =False)

# mean calculatioon by month 2023-2024
df_june24.set_index('Date',inplace=True)
fy_monthly_mean =df_june24.resample('ME').mean().round(3).plot(
    kind='line',
    xlabel="Months",
    ylabel="Mean Inter Bank Rates",
    title="Average Inter Bank Rates Spread over Months (JULY 2023 -JUNE-2024)"
)
plt.show();
fy_monthly_mean.to_csv('assets/data/interbank_rates_means_by_month_2023_2024.csv')
print(fy_monthly_mean)

# median calculatioon by month 2023-2024
fy_monthly_median =df_june24.resample('ME').median().round(3).plot(
    kind='line',
    xlabel="Months",
    ylabel="Median Inter Bank Rates",
    title="Median Inter Bank Rates Spread over Months (JULY 2023 -JUNE-2024)"
)
plt.show();
fy_monthly_median.to_csv('assets/data/interbank_rates_median_by_month_2023_2024.csv')
print(fy_monthly_median)

# SD calculatioon by month 2023-2024
df_june24=pd.read_csv('assets/data/inter_bank_rates_july23_june24.csv')
df_june24['Date'] = pd.to_datetime(df_june24['Date'])


df_sd = df_june24.groupby(df_june24['Date'].dt.to_period('M')).agg({'Overnight_rate': 'std', 'Seven_day_rate': 'std', 'Overall_rate': 'std'}).round(3).plot(
    kind='line',
    xlabel="Months",
    ylabel="SD Inter Bank Rates",
    title="Standard Deviation Inter Bank Rates Spread over Months (JULY 2023 -JUNE-2024)"
)
plt.show();
df_sd.to_csv('assets/data/interbank_rates_sd_by_month_2023_2024.csv')


print(df_sd)


# mean, median ,SD calculations on period 2012 where  we had the heighest picks
#1ST FILTER DATA FOR THE PERIOD JAN 2012 -DEC 2012, AND EXTRACT IN NEW CSV
df.info()
start_date_2012 = '2012-01-01'
end_date_2012 = '2012-12-31'

df.info()
df.head()
df['Date'] = pd.to_datetime(df['Date'],format="%Y-%m-%d")

df_2012 = df[(df['Date'] >= start_date_2012) & (df['Date'] <= end_date_2012)]
df_2012.head()
df_2012.info()



df_2012.to_csv('assets/data/inter_bank_rates_2012.csv',index=False)


import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import statistics

#General Stats for 2012
df_2012_summary=df_2012.describe().round(3)
print(df_2012_summary)
df_2012_summary.to_csv('assets/data/df_2012_summary.csv',index =False)

# mean calculatioon by month for 2012
df_2012.set_index('Date',inplace=True)
df_2012_mean =df_2012.resample('ME').mean().round(3).plot(
    kind='line',
    xlabel="Months",
    ylabel="Mean Inter Bank Rates",
    title="Average Inter Bank Rates Spread over Months 2012"
)
plt.show();
df_2012_mean.to_csv('assets/data/interbank_rates_means_by_month_2012.csv')
print(df_2012_mean)

# median calculatioon by month 2012
df_2012_median =df_2012.resample('ME').median().round(3).plot(
    kind='line',
    xlabel="Months",
    ylabel="Median Inter Bank Rates",
    title="Median Inter Bank Rates Spread over Months 2012"
)
plt.show();
df_2012_median.to_csv('assets/data/interbank_rates_median_by_month_2012.csv')
print(df_2012_median)

# SD calculatioon by month 2012
df_2012=pd.read_csv('assets/data/inter_bank_rates_2012.csv')
df_2012['Date'] = pd.to_datetime(df_2012['Date'],format='%Y-%m-%d')

df_2012.head()
df_2012.info()

df__2012_sd = df_2012.groupby(df_2012['Date'].dt.to_period('M')).agg({'Overnight_rate': 'std', 'Seven_day_rate': 'std', 'Overall_rate': 'std'}).round(3).plot(
    kind='line',
    xlabel="Months",
    ylabel="SD Inter Bank Rates",
    title="Standard Deviation Inter Bank Rates Spread over Months 2012"
)
plt.show();
df__2012_sd.to_csv('assets/data/interbank_rates_sd_by_month_2012.csv')


print(df__2012_sd)

