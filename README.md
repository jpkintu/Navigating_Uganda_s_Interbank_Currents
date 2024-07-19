<h1 style="text-align: center;">Navigating Uganda’s Interbank Currents: A Data Odyssey</h1>

## Introduction.

Picture this: In the heart of East Africa, a nation's economic destiny unfolds in the quiet exchanges between banks. Every day, financial institutions in Uganda engage in a delicate dance of lending and borrowing, their moves choreographed by a single, powerful number - the interbank rate. This rate, often overlooked by the general public, holds the power to influence everything from the cost of your next business loan to the interest earned on your savings account.

"The interbank rate is the heartbeat of a nation's financial system," as renowned economist John Maynard Keynes once observed. "It sets the rhythm for economic growth and stability."

This project delves into Uganda’s interbank rates from 2012 to 2024, using Excel for organizing and extracting data, Python for data cleaning and analysis, and Tableau further analysis,visualisation and creating interactive dashboards.

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


## Connections and Relationships
<img src="Assets/Py Charts/Inter bank rate correlations.png" alt="Inter bank rate correlations"/>
<p><i>Our correlation analysis of Uganda’s interbank rates from 2012 to 2024 reveals several key insights:
<li>Overnight rate and Overall rate have a very strong positive correlation (0.98).</li>
<li>Seven-day rate has a moderate positive correlation with both the Overnight rate (0.73) and the Overall rate (0.78).</li>
<li>The Overall rate is more closely aligned with the Overnight rate than the Seven-day rate.</li></i></p>

<p><i>These findings suggest that short-term (overnight) rates have a stronger influence on the overall interbank rate compared to slightly longer-term (seven-day) rates. In practical terms, this means that fluctuations in the overnight rate are more likely to impact the overall cost of interbank lending. Financial institutions may prioritize monitoring and responding to changes in the overnight rate to manage their short-term liquidity needs effectively.

The strong correlation between the overnight and overall rates indicates that the overall interbank rate is highly sensitive to short-term liquidity conditions. This could lead to more immediate adjustments in lending rates in response to central bank policies or market conditions affecting overnight funds. On the other hand, the moderate correlation of the seven-day rate with both the overnight and overall rates suggests that while it is still influential, its impact is less pronounced.</i></p>

## Volatility Unleashed
<img src="Assets/Tableau Charts/Interbank rates SD by month 2012.png" alt="Volatility of Interbank Rates 2012"/>
<p><i>The analysis of volatility in 2012 reveals several key observations. February 2012 experienced the highest volatility across all rates. The Overnight rate exhibited the highest average volatility at 3.16, followed by the Overall rate at 2.82, and the Seven-day rate at 1.44. After February, volatility generally decreased, although there were some fluctuations throughout the year. This trend highlights the significant impact of early-year market conditions on interbank rate stability.</i></p>

<img src="Assets/Tableau Charts/Interbank rates SD 2023-2024.png" alt="Volatility of Interbank Rates July 2023 - June 2024"/>
<p><i>The analysis of interbank rate volatility from July 2023 to June 2024 reveals several key observations. The Overnight rate exhibited the highest average volatility at 0.369, followed by the Overall rate at 0.323, and the Seven-day rate at 0.230. June 2024 experienced the highest volatility for both the Overnight and Overall rates, while September 2023 saw the peak volatility for the Seven-day rate. Volatility fluctuated throughout the period, with notable spikes in certain months.

Compared to the previous period in 2012, the overall volatility levels are significantly lower in 2023-2024. The ranking of rates by average volatility remains consistent (Overnight > Overall > Seven-day). However, the timing of peak volatility has shifted from February in 2012 to various months in 2023-2024. This trend highlights changes in market dynamics and conditions over the years.</i></p>

## 6.	Regression Quest

## 7.	Plot Twists: Event Analysis and Decision Points

## 8.	Conclusion: The Journey Continues

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
