# surfs_up

Note: Some cell-outputs are cleared to ease-reading. I have attached screenshots of the output.
### Report that describes the key differences in weather between June and December and two recommendations for further analysis.
* Overview of the analysis: Explain the purpose of this analysis:

* Results: Provide a bulleted list with three major points from the two analysis deliverables. There is a bulleted list that addresses the three key differences in weather between June and December: Use images as support where needed.

* Summary: Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.

### Overview of the analysis: Explain the purpose of this analysis:

The purpose of this analysis was to provide additional information to W. Avy about temperatures in Oahu so he can make the best decision about opening an ice-cream and surf shop. We needed to collect the temperatures for the months of June and December to see how sustainable the ice-cream sales would be year-round. The summary statistics have been generated for both months so we could easily analyze our findings.

### Provide a bulleted list with three major points from the two analysis deliverables.

The three main points or differences between the weather in these two months will help us understand how successful the surf and ice-cream shop will be.
* The minimum temperature in Oahu in December is about 8 degrees cooler than the minimum temperature in June.
* The maximum temperature in Oahu in December is only 2 degrees cooler than the maximum temperature in June.
* The average temperature in Oahu in December is only about 3 degrees cooler than the average temperature in June.

First, it will help to see the statistical summary for each month's temperatures:

![dec_temps](https://github.com/jmalauss/surfs_up/blob/main/dec_temps.png)
![june_temps](https://github.com/jmalauss/surfs_up/blob/main/june_temps.png)

* The minimum temperatures for each month are interesting because they tell us how low it could possibly get. Ice-cream is best served cold on a hot day, so this information is important to because it allows us to make assumptions about our potential ice-cream sales in December. Given the strong positive correlation between ice-cream sales and temperature, we can assume that sales will drop with colder temperatures in December. An additional question we could ask here: How often are temperatures low?
* The maximum temperatures help us understand the potential for ice-cream sales in December, which will likely increase on the hottest days. According to our summary statistics, it seems December's hot days are not much cooler than those in June. In other words, if we consider again the positive correlation between ice-cream sales and temperature, we can assume that our ice-cream sales will be just as profitable on an 83 degree day in June, or December. Once again we can ask how often we get days that are this hot in December?
* The average temperatures from both months help us understand the questions above. In December, it is an average of 71 degrees. In June, 74. Although the minimum temperatures are 8 degrees apart, we can tell by the average temperature that December weather will more often be in the low 70s. By looking at the average temperatures for both months, we next likely ask: Are temperatures in the low 70s good for icecream sales?

### Summary: Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.

The results we found show that there may not be much of a difference in temperatures between December and June, in Oahu. The differences that we found, warrant additional questions. For example: We would need more granular data on ice-cream sales in Oahu. This would help us understand how successful our shop would be on a 71 degree day - which could be a near average day for temperatures in both December and June. 

Here are some additional questions we could explore before feeling fully informed about our business decision:
* Analysis of existing ice-cream shops in Oahu: Sales per temperature and other factors that influence sales.
* Does the weekend or weekday matter? If we conducted an analysis, and found a trend that there are less ice-cream sales during the weekdays, we could manipulate store hours to be more cost efficient proactively. This analysis could be conducted by deep diving the date of sales in existing ice-cream shops, and generating summary statistics for sales per days of the week.
* Do clouds in the sky influence the desire for ice-cream on a hot day? We can agree that the sun makes things feel hotter, but is there a relationship here? By analyzing data about cloudiness in Oahu, we could further our understanding of ice-cream sales on hot days. What if there is a really cloudy 85 degree day? Do people still have the same desire for ice-cream?
