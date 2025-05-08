 Restaurant Recommendation
 Objective: Create a restaurant recommendation system based on user preferences
Steps:
Preprocess the dataset by handling missingvalues and encoding categorical variables.
Determine the criteria for restaurant recommendations (e.g., cuisine preference,price range).
Implement a content-based filteringapproach where users are recommendedrestaurants similar to their preferred criteria.
Test the recommendation system byproviding sample user preferences andevaluating the quality of recommendations.
code guidelines: 
import pandas to read dataset -code- read_csv(file)
import sklearn for feature extraction, pre processing, metrics evaluation.
handle missing values  -code- fillna('unknown')
create a buplicate data frame with features to be considered - here i coosen   'Cuisines', 'Average Cost for two', 'Price range', 'Aggregate rating' .
for easy process i vectorized and matrixified cuisines and then transformed .
using numpy combined featues
now function to get result
give input cuisine , min and max costs, rating 
get result of top 5 restautents which are recommended

steps to implement the file
get app.py and dataset.csv ready  
change file_path in app.py with dataset.csv location 
1.pip install streamlit
2.streamlit run app.py

