<h1 style="text-align: center;">Navigating Uganda’s Interbank Currents: A Data Odyssey</h1>

<img src="Assets/Tableau Charts/Dashboard 2.png" alt="d2"/>

## Introduction
Picture this: In the heart of East Africa, a nation's economic destiny unfolds in the quiet exchanges between banks. Every day, financial institutions in Uganda engage in a delicate dance of lending and borrowing, their moves choreographed by a single, powerful number - the interbank rate. This rate, often overlooked by the general public, holds the power to influence everything from the cost of your next business loan to the interest earned on your savings account.

"The interbank rate is the heartbeat of a nation's financial system," as renowned economist John Maynard Keynes once observed. "It sets the rhythm for economic growth and stability."

This project delves into Uganda’s interbank rates from 2012 to 2024.
Through this project, I demonstrated expertise in:

- Data extraction and organization using Excel
- Data cleaning, modeling and analysis using Python(Libraries used included Pandas, NumPy, Matplolib, Seaborn)
- Data visualization and dashboard creation using Tableau
- Version control and creating a dedicated page for showcasing my analysis using GitHub

Effectively wove together these skills to craft a narrative that uncovered hidden patterns, trends, and insights in the data, and presented findings in a clear, concise, and visually appealing manner.
<img src="Assets/Tableau Charts/Navigating Uganda’s Interbank Currents.png" alt="Navigating Uganda’s Interbank Currents"/>

### Our guide? 
A rich dataset provided by the Bank of Uganda, offering a window into the country's economic soul. <a href="https://bou.or.ug/bouwebsite/bouwebsitecontent/statistics/InterestRates/Interest_rates.xlsx" target="_blank">SEE DATA SOURCE</a> from <a href="https://www.bou.or.ug/bouwebsite/Statistics/" target="_blank">Bank of Uganda Statistics</a>

### Why does this matter?
Interbank rates are more than just numbers on a banker's ledger. They are the invisible hand that shapes monetary policy, influences inflation, and ultimately affects the financial well-being of every Ugandan citizen. By understanding these rates, we gain insight into the nation's economic health, its challenges, and its triumphs.

This analysis will take you from the dizzying heights of 2012, where rates peaked at a staggering 18.879% for 7-day rates, to the valleys of recent years where rates have moderated. As we dive into this data, we're not just crunching numbers; we're telling the story of a nation's economic journey. We'll uncover the tales hidden in the trends, the dramas played out in the dips and spikes, and the potential future written in the current trajectories.

Buckle up for a journey through the peaks and troughs of Uganda's financial heartbeat - a story told through the lens of interbank rates, where every percentage point tells a story.

## Understanding the Data
### Trends in Uganda's Interbank Rates (2012-2024)
Our journey into Uganda's financial landscape begins with an overview of the interbank rates from 2012 to 2024. This analysis provides a bird's-eye view of the trends and fluctuations in the country's financial system over more than a decade.

Let's start by examining the visual representation of the data:
<img src="Assets/Tableau Charts/Avg inter bank rates over years(2012-2024).png" alt="Avg inter bank rates over years(2012-2024)"/>
<p align="center"><i>This graph illustrates the annual mean rates for three key metrics: the overnight rate, the seven-day rate, and the overall rate. Each line tells a story of Uganda's economic journey, with peaks and troughs reflecting various economic conditions and policy decisions.</i></p>

#### Key Observations:

**Peak in 2012:** The most striking feature of this graph is the pronounced peak in 2012. During this year, we observed the highest rates across all three categories.

<img src="Assets/Tableau Charts/Average Interbank Rates by month 2012.png" alt="Avg Interbank Rates by month 2012"/>
<p><i>In 2012, Uganda’s interbank rates were notably high compared to subsequent years. The overall rate averaged 16.64%, with the seven-day rate at 18.96% and the overnight rate at 15.23%. January 2012 saw peak rates, with the overnight rate at 25.90%, the seven-day rate at 28.54%, and the overall rate at 26.65%, indicating significant financial stress or tight monetary policy. Rates generally trended downward throughout the year, with the overnight rate dropping to 10.00% by September, reflecting eased monetary conditions. The seven-day rate consistently exceeded the overnight rate, with an average spread of 3.73 percentage points, suggesting a premium for longer-term lending. Rates were volatile, with the overnight rate ranging from 25.90% in January to 10.00% in September, and the seven-day rate consistently higher, especially in February and August.</i></p>

<img src="Assets/Tableau Charts/Avg Interbank Rates 2012(Data_Table).png" alt="Avg Interbank Rates 2012(Data_Table)"/>

**General Downward Trend:** Following the 2012 peak, we see a general downward trend in all three rates. This decline indicates a gradual easing of monetary policy over the years, potentially aimed at stimulating economic growth by reducing borrowing costs.

**Convergence of Rates:** As we move towards more recent years, we notice a convergence of the three rates. This narrowing spread between overnight and seven-day rates indicates increased stability and predictability in the short-term money market.

**Recent Uptick:** Towards the end of the observed period, focusing on 12 months (July 2023-June 2024), we see a slight upturn in rates. This recent increase might signal a shift in monetary policy stance, possibly in response to changing economic conditions or inflationary concerns.

<img src="Assets/Tableau Charts/Avg Interbank Rates (2023-2024).png" alt="Avg Interbank Rates (2023-2024)"/>
<p ><i>The seven-day rate consistently remained higher than the overnight rate between this period. Overall rates fluctuated between 10.106% and 12.005%.
There was a significant drop in rates in June 2024. The highest rates were observed in April and May 2024. 
The Average rate difference (Seven-day - Overnight): 0.3239166666666667
    
This indicates that longer-term lending (seven-day) was generally perceived as riskier than overnight lending. </i></p>
<img src="Assets/Tableau Charts/Avg Interbank Rates (2023-2024) Data Table.png" alt="Avg Interbank Rates (2023-2024) Data Table"/>

**Volatility:** The graphs reveal periods of significant volatility, particularly in the earlier years. This volatility gradually decreases over time, suggesting an increasing maturity and stability in Uganda's financial markets.

## Time Travel
### End of 2024 Estimates
<img src="Assets/Tableau Charts/Forecast of Average Interbank Rates.png" alt="2024 Forecast of Average Interbank Rates"/>

<p><i>In examining Uganda's interbank rates from July 2023 to June 2024, we observed a forecasted increase in rates for the period from July to December 2024. The average seven-day rate is expected to rise to 11.3392%, the overnight rate to 10.8884%, and the overall rate to 10.9189%, compared to June 2024 averages of 10.7580%, 9.8070%, and 10.1060%, respectively. This projected rise suggests higher short-term lending costs due to anticipated economic conditions or monetary policy adjustments, reflecting tighter liquidity conditions or increased demand for short-term funds. The general upward trend in interbank lending rates indicates a cautious approach by financial institutions in response to expected economic developments.</i></p>

### Forecasted Annual Average Rates for 2024 and 2025
<img src="Assets/Tableau Charts/Annual forecast 2024 & 2025.png" alt="Annual forecast 2024 & 2025"/>
<p><i>Based on the analysis of annual average rates from 2012 to 2023, the forecasted rates for 2024 and 2025 show significant trends. For 2024, the average seven-day rate is estimated at 10.65%, and the overnight rate at 9.076%. This indicates a slight decrease from the 2023 averages of 11.03% for the seven-day rate and 10.683% for the overnight rate, suggesting a potential easing of short-term lending costs and improved liquidity conditions.

However, the forecast for 2025 shows a more pronounced change, with the seven-day rate dropping to 6.91%, while the overnight rate remains steady at 9.076%.  The stability of the overnight rate suggests that while short-term lending costs may decrease, the demand for very short-term funds might remain consistent.</i></p>


## Connections and Relationships: Correlation and Spread Analysis
<img src="Assets/Py Charts/Inter bank rate correlations.png" alt="Inter bank rate correlations"/>
<p><i>Our correlation analysis of Uganda’s interbank rates from 2012 to 2024 reveals several key insights:
<li>Overnight rate and Overall rate have a very strong positive correlation (0.98).</li>
<li>Seven-day rate has a moderate positive correlation with both the Overnight rate (0.73) and the Overall rate (0.78).</li>
<li>The Overall rate is more closely aligned with the Overnight rate than the Seven-day rate.</li></i></p>

<p><i>These findings suggest that short-term (overnight) rates have a stronger influence on the overall interbank rate compared to slightly longer-term (seven-day) rates. In practical terms, this means that fluctuations in the overnight rate are more likely to impact the overall cost of interbank lending. Financial institutions may prioritize monitoring and responding to changes in the overnight rate to manage their short-term liquidity needs effectively.

The strong correlation between the overnight and overall rates indicates that the overall interbank rate is highly sensitive to short-term liquidity conditions. This could lead to more immediate adjustments in lending rates in response to central bank policies or market conditions affecting overnight funds. On the other hand, the moderate correlation of the seven-day rate with both the overnight and overall rates suggests that while it is still influential, its impact is less pronounced.</i></p>

<img src="Assets/Tableau Charts/Trends in Interbank Rate Spreads.png" alt="Trends in Interbank Rate Spreads"/>
<P><i>The analysis  from 2012 to 2024 reveals significant trends and fluctuations over the years. The average spread between the Seven-day and Overnight rates has generally decreased over time, with notable peaks and troughs. The years 2012 to 2016 experienced the highest average spreads, with 2012 peaking at 3.75360. From 2017 onwards, there is a noticeable decline in the average spreads, reaching as  low as 0.34367 in 2023. This trend suggests improved market stability and more consistent short-term lending conditions. The spread in 2024 shows a slight increase to 0.39723 compared to 2023.</i></P>

## Volatility Unleashed
<img src="Assets/Tableau Charts/Interbank rates SD by month 2012.png" alt="Volatility of Interbank Rates 2012"/>
<p><i>The analysis of volatility in 2012 reveals several key observations. February 2012 experienced the highest volatility across all rates. The Overnight rate exhibited the highest average volatility at 3.16, followed by the Overall rate at 2.82, and the Seven-day rate at 1.44. After February, volatility generally decreased, although there were some fluctuations throughout the year. This trend highlights the significant impact of early-year market conditions on interbank rate stability.</i></p>

<img src="Assets/Tableau Charts/Interbank rates SD 2023-2024.png" alt="Volatility of Interbank Rates July 2023 - June 2024"/>
<p><i>The analysis of interbank rate volatility from July 2023 to June 2024 reveals several key observations. The Overnight rate exhibited the highest average volatility at 0.369, followed by the Overall rate at 0.323, and the Seven-day rate at 0.230. June 2024 experienced the highest volatility for both the Overnight and Overall rates, while September 2023 saw the peak volatility for the Seven-day rate. Volatility fluctuated throughout the period, with notable spikes in certain months.

Compared to the previous period in 2012, the overall volatility levels are significantly lower in 2023-2024. The ranking of rates by average volatility remains consistent (Overnight > Overall > Seven-day). However, the timing of peak volatility has shifted from February in 2012 to various months in 2023-2024. This trend highlights changes in market dynamics and conditions over the years.</i></p>

<img src="Assets/Tableau Charts/Volatility of Interbank RatesJune 2024.png" alt="Volatility of Interbank RatesJune 2024"/>
<p><i>The weekly volatility analysis for June 2024 shows varying levels of interbank rate fluctuations. Week 1 experienced relatively low volatility, with the Overall rate being the most volatile. Week 2 saw a significant increase, particularly in the Seven-day and Overnight rates. Week 3 maintained high volatility, especially for the Overnight rate, indicating continued market instability. In Week 4, the Overnight rate’s volatility sharply increased, while the Seven-day rate had the lowest volatility of the month. Overall, June 2024 exhibited fluctuating volatility levels, with notable spikes in the second and fourth weeks, highlighting periods of increased market uncertainty and activity.</i></p>

## Regression Quest
<img src="Assets/Tableau Charts/Regression of Interbank Rates Vs Inflation2012-2023.png" alt="Regression of Interbank Rates Vs Inflation2012-2023"/>
In analyzing the relationship between interbank rates and inflation in Uganda from 2012 to 2023, our findings reveal a significant positive correlation across all three interbank rates: Overall, Overnight, and Seven-day. As interbank rates rise, inflation tends to follow suit, highlighting the critical role of monetary policy in shaping economic conditions.

These insights are particularly relevant for policymakers, as they underscore the delicate balance required in managing interest rates to control inflation without stifling economic growth. The variability observed in the scatter plots suggests that while interbank rates are a key factor, other external influences also contribute to inflation dynamics.

For investors and businesses, understanding this relationship is essential for making informed decisions regarding borrowing, investment, and pricing strategies. As we navigate the complexities of the economic landscape, these findings serve as a reminder of the interconnectedness of monetary policy and inflation, and the importance of data-driven decision-making in fostering economic stability.

## Plot Twists: Event Analysis and Decision Points
### Central Bank Announcements:
- 2012: The Bank of Uganda (BoU) maintained a tight monetary policy to control high inflation caused by global food and fuel price shocks.
- 2016: BoU reduced the Central Bank Rate (CBR) to stimulate economic growth amid low inflation , which  resulted in reduced interbank rates, aiming to boost lending and economic activity.
- 2020: In response to the COVID-19 pandemic, BoU cut the CBR to a record low of 7% to support economic activity, this led to lower interbank rates, providing liquidity to the financial system during the pandemic.
- 2024: BoU raised the CBR to 10.25% in April to curb rising inflation and stabilize the depreciating shilling. This caused interbank rates to rise, aiming to control inflation and stabilize the currency.
  
### Economic Shocks:
- 2012-2013: Global commodity price fluctuations impacted Uganda’s inflation and trade balance.
- 2016: Droughts affected agricultural output, leading to food price inflation.
- 2020: The COVID-19 pandemic caused significant economic disruptions, leading to a contraction in GDP.
- 2022-2023: Geopolitical tensions, such as the Russia-Ukraine conflict, led to volatility in energy and commodity 

For further reading, refer to sources below;
- <a href="https://www.bou.or.ug/bouwebsite/bouwebsitecontent/MonetaryPolicy/Monetary_Policy_Reports/2024/Apr/Monetary-Policy-Report-April-2024-v1-002-004.pdf" target="_blank">Monetary Policy Report</a>
- <a href="https://www.bou.or.ug/bouwebsite/bouwebsitecontent/MonetaryPolicy/Monetary-Policy-Statements-At-a-Glance/2024/Monetary-Policy-Statement-at-a-glance-for-March-2024.-.pdf" target="_blank">MONETARY POLICY STATEMENT - at a glance</a>
- <a href="https://thedocs.worldbank.org/en/doc/bae48ff2fefc5a869546775b3f010735-0500062021/related/mpo-uga.pdf" target="_blank">Uganda:Key Conditions and Challenges</a>

<!-- Footer section -->
<footer>
    <div class="footer-content">
        <p>Contact me:</p>
        <ul>
            <li>Email: <a href="mailto:kintujp@gmail.com">kintujp@gmail.com</a></li>
            <li>LinkedIn: <a href="https://www.linkedin.com/in/john-paul-k-aa6b8757" target="_blank" rel="noreferrer noopener">John Paul Kintu</a></li>
            <li>Portforlio: <a href="https://jpkintu.github.io/Portfolio-Resume/" target="_blank" rel="noreferrer noopener">www.jpkintu.com</a></li>
        </ul>
    </div>
</footer>
