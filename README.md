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

# Visualization
## Part 1:
I first made a scatterplot of AVG_SYS_BP vs Nicotine to quickly visualize the distribution of my data.

# Conclusions


## <u>Future Research:</u>
<ul>
<li></li>
</ul>

# Works Cited
<ol>
<li>https://www.boxofficemojo.com/chart/top_opening_weekend/</li>
</ol>