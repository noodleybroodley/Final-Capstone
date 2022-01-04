# Health Factors & High Blood Pressure
<br></br>
<img src="img/popcorn.gif">
<br></br>
# Background & Motivation
Being an Army Officer, physical readiness is paramount; you have to keep your body in good shape to meet the requirements of the profession. Exercise plays a key role in maintaining physical fitness, but the things you consume are equally important. Nicotine use is widespread among officers, non-commissioned officers and soldiers alike and I am concerned about what negative impacts this might have on health. Because of this, I wanted to examine the effects of nicotine use on blood pressure.

# Questions
<ul>
	<li>How does nicotine affect the likelihood that someone has high blood pressure?</li>
	<li>What other health factors have an effect on this likelihood?</li>
</ul>

# Data
The data I used for this project comes from the <a href="https://www.kaggle.com/cdc/national-health-and-nutrition-examination-survey">2013-2014 National Health and Nutrition Examination Survey (NHANES)</a>, an annual survey conducted by the CDC. The survey contains information about participants from 15 different counties across the United States. The data combines medical questionnaire answers as well as medical examinations and labs. The data was broken up into 6 files:
<ul>
	<li>"demographic": 47 columns, 10176 rows</li>
	<li>"diet": 168 columns, 9814 rows</li>
	<li>"examination": 224 columns, 9814 rows</li>
	<li>"labs": 424 columns, 9814 rows</li>
	<li>"medications": 13 columns, 20195 rows</li>
	<li>"questionnaire": 953 columns, 10176 rows</li>
</ul>
Obviously, I couldn't include every column in my analysis, so I decided to focus on participants' ages, blood pressure, marital status, and the amount of nicotine found during their labs. This resulted in the data below:
<br></br>
## Include screenshot
<br></br>

## <u>Summary of the Data:</u>
10175 Rows, each containing the following information for unique patients:
<ul>
	<li>SEQN: the Participant's Unique Sequence Number</li>
	<li>RIDAGEYR: Age</li>
	<li>DMQMILIZ: Did the participant serve active duty in US Armed Forces?</li>
	<li>DMDMARTL: Marital Status</li>
	<li>AVG_SYS_BP: Average Systolic Blood Pressure</li>
	<li>AVG_DIAS_BP: Average Diastolic Blood Pressure</li>
	<li>High_SYS_BP: Does the participant have a High Average Systolic Blood Pressure (>= 130 mmHg)</li>
	<li>High_DIAS_BP: Does the participant have a High Average Diastolic Blood Pressure (>= 80 mmHg)</li>
	<li>LBXHCT: Nicotine Metabolate Levels Detected (Hydroxycotinine, Serum (ng/mL))</li>

</ul>

## <u>Cleaning:</u>
<ul>
	<li>I first selected the columns that I wanted to focus on and removed the rest.</li>
	<li>Initially, all categorical column entries were recorded as integers representing participant responses. I found a website that had a legend that explained each number, then I replaced all the numbers with more readable text.</li>
	<li>I created the AVG_SYS_BP and AVG_DIAS_BP columns by taking the average of the four blood pressure readings for each patient.</li>
	<li>I then created the High_SYS_BP and High_DIAS_BP columns by comparing each average blood pressure with the threshold for high blood pressure (Systolic >= 130 mmHg; Diastolic >= 80 mmHg). I had to convert these columns to integers because the Logistic Regression function couldn't interpret Boolean values.</li>
	<li>I created a CleanDF class that creates a cleaned dataframe containing all of the features listed above.</li>
	<li>While NaN values are ignored by the plotting libraries that I used, I had to drop rows containing NaN values when creating my logistic regression models.</li>
</ul>

# Part 1: Visualization
<p>I first made a scatterplot of Average Systolic Blood Pressure vs Nicotine to quickly visualize my data.<p>

* ADD INITIAL SCATTERPLOT
<p>The relationship between Blood Pressure and Nicotine does not appear to be linear, so a linear regression would not be appropriate for modeling this relationship.</p>
<p>I also wanted to see how blood pressure varied between different demographics of people. Below are Box and Whisker plots showing the distribution of blood pressure readings for people of different marital statuses:</p>

* ADD MARITAL STATUS BOX N WHISKER
<p>...and another comparing blood pressure readings of people who served in the active duty military and those that didn't:</p>

* ADD MILITARY BOX N WHISKER
<p>It is interesting to note that widowers seem to have a higher mean blood pressure than people of other marital statuses, while people living with a partner seem to have the lowest mean blood pressure. People who have served in the also seem to have higher mean blood pressure than people who haven't.</p>

# Part 2: Creating a Model
<p>As previously noted, the relationship between Blood Pressure and Nicotine cannot be represented linearly, so it would be more appropriate to view this as a binary classification problem: "What are the odds that a participant has high blood pressure, based on the amount of nicotine detected during their labs? I chose to create an inferential logistic regression!</p>

## Assumptions of Inferential Logistic Regression:
<p>In order to perform an inferential logistic regression, my problem had to meet the following requirements:</p>
  
  * Correct Distribution of Outcome: a binary regression requires the dependent variable to be binary
    * In my regression dependent variable is binary: a person either has high blood pressure (1) or doesn't (0) :white_check_mark:
  * Independence: observations should be independent
  * No Multicollinearity: logistic regression requires there to be little to no multicollinearity among the independent variables
  * Linearity of the Log Odds: independent variables must be linearly related to the log odds
  * Sample Size: at minimum, 10 cases with the least frequent outcome for each independent variable in your model
    * (10 x 1 independent variable)/(0.43 probability of a person having high blood pressure) = 23 minimum samples
<p>To accomplish this, I created a new column in my data containing a "1" if the participant had high systolic blood pressure on average and a "0" if they did not (scatterplot below).</p>

* ADD SCATTERPLOT
<p>I then created my initial logistic regression model</p>

* add model plot

# Part 3: Improving the Model
<p>As you can see, our regression line doesn't exactly fit the data. In this case, it is necessary to choose a probability threshold for classifying a data point as having high blood pressure. I initially chose 0.15.</p>

<p>evaluated its performance using a Receiver Operating Characteristic (ROC) curve:</p>

* add model plot with 0.15 threshold line
* add roc curve
<p>In my model, I want to minimize the false positive rate and maximize the true positive rate. In other words, I want my model to correctly categorize a person's blood pressure as much as possible. I used the area under the ROC curve to determine if my model is successful at this. On this plot, an area of 0.5 represents a 50% probability that a model will correctly categorize data, equivalent to random guessing or a coin-flip. The closer to an area of 1.0, the better the model. This initial model is only slightly better than random guessing so I tried improving it by changing the threshold a few times.</p>

* add all threshold changes
<p></p>



# Conclusions


## <u>Future Research:</u>
<ul>
<li></li>
</ul>

# Works Cited
<ol>
<li>https://www.boxofficemojo.com/chart/top_opening_weekend/</li>
</ol>