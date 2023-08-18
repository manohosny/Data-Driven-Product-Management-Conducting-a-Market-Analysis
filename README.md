Google Trends Data Visualization
This project provides a set of functions to read, process, and visualize data from Google Trends. The data is related to workout trends and interests across different regions and time periods.

Features
Time Series Visualization: Visualize the interest of certain keywords over time.
Geographical Interest Visualization: Visualize the interest of certain keywords across different countries.
Data Processing: Process raw data from Google Trends to make it suitable for visualization.
Dependencies
pandas
seaborn
matplotlib
How to Use
1. Reading and Visualizing Time Series Data
python
Copy code
# Read the 'workout.csv' file and visualize it
workout = read_file('data/workout.csv')
2. Reading and Visualizing Geographical Data
python
Copy code
# Read the 'workout_global.csv' file and visualize the top 25 countries with the highest workout interest
workout_global = read_geo('data/workout_global.csv')
3. Analyzing Multiple Keywords
python
Copy code
# Read the 'three_keywords.csv' file and visualize it
three_keywords = read_file('data/three_keywords.csv')
4. Filtering Data by Specific Countries
python
Copy code
# Define a list of countries
MESA_countries = ["Philippines", "Singapore", "United Arab Emirates", "Qatar", "Kuwait", "Malaysia", "Sri Lanka", "India", "Pakistan", "Lebanon"]

# Filter the 'geo_three_keywords' dataframe to include only the countries in the 'countries_list'
MESA = geo_three_keywords.loc[geo_three_keywords.country.isin(MESA_countries), :]
Sample Analysis
Resample the 'workout' dataframe by month and calculate the mean of the 'interest' column.
Find the month with the highest interest in workouts.
Get the top country with the highest workout interest.
Analyze the interest in pilot content like 'yoga' and 'zumba'.
Data Source
The data used in this project is sourced from Google Trends. It provides insights into the popularity of search queries in Google Search across various regions and languages.

Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

Licensing
The code in this project is licensed under MIT license.

