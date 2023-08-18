import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style='white', palette='Pastel2')
import os

def read_file(filepath, plot = True):
    """
    Read a CSV file from a given filepath, convert it into a pandas DataFrame,
    and return a processed DataFrame with three columns: 'week', 'region', and 'interest'. Generate a line plot using Seaborn to visualize the data. This corresponds to the first graphic (time series) returned by trends.google.com. 
    """
    file = pd.read_csv(filepath, header=1)
    df = file.set_index('Week').stack().reset_index()
    df.columns = ['week','region','interest']
    df['week'] = pd.to_datetime(df['week'])
    plt.figure(figsize=(8,3))
    df = df[df['interest']!="<1"]
    df['interest'] = df['interest'].astype(float)

    if plot:
        sns.lineplot(data = df, x= 'week', y= 'interest',hue='region')
    return df

def read_geo(filepath, multi=False):
    """
    Read a CSV file from a given filepath, convert it into a pandas DataFrame,
    and return a processed DataFrame with two columns: 'country' and 'interest'. Generate a bar plot using Seaborn to visualize the data. This corresponds to the second graphic returned by trends.google.com. Use multi=False if only one keyword is being analyzed, and multi=True if more than one keyword is being analyzed.
    """
    file = pd.read_csv(filepath, header=1)

    if not multi:
        file.columns = ['country', 'interest']
        plt.figure(figsize=(8,4))
        sns.barplot(data = file.dropna().iloc[:25,:], y = 'country', x='interest')

    if multi:
        plt.figure(figsize=(3,8))
        file = file.set_index('Country').stack().reset_index()
        file.columns = ['country','category','interest']
        file['interest'] = pd.to_numeric(file['interest'].apply(lambda x: x[:-1]))
        sns.barplot(data=file.dropna(), y = 'country', x='interest', hue='category')

    file = file.sort_values(ascending=False,by='interest')
    return file
# Read the 'workout.csv' file and assign it to the variable 'workout'
workout = read_file('data/workout.csv')

# Resample the 'workout' dataframe by month and calculate the mean of the 'interest' column
workout_by_month = workout.set_index('week').resample('MS').mean()

# Find the month with the highest interest in workouts and convert it to a string in the format 'YYYY-MM-DD'
month_high = workout_by_month[workout_by_month['interest'] == workout_by_month['interest'].max()]
month_str = str(month_high.index[0].date())

# Read the 'three_keywords.csv' file and assign it to the variable 'three_keywords'
three_keywords = read_file('data/three_keywords.csv')

# Set the current and peak COVID keywords
current = 'gym workout'
peak_covid = 'home workout'

# Read the 'workout_global.csv' file and assign it to the variable 'workout_global'
workout_global = read_geo('data/workout_global.csv')

# Get the top country with the highest workout interest from the 'workout_global' dataframe
top_25_countries = workout_global.head(25)
top_country = top_25_countries['country'].iloc[0]

# Read the 'geo_three_keywords.csv' file with multiple columns and assign it to the variable 'geo_three_keywords'
geo_three_keywords = read_geo('data/geo_three_keywords.csv', multi=True)

# Define a list of countries
MESA_countries = ["Philippines", "Singapore", "United Arab Emirates", "Qatar", "Kuwait", "Malaysia", "Sri Lanka", "India", "Pakistan", "Lebanon"]

# Filter the 'geo_three_keywords' dataframe to include only the countries in the 'countries_list' and assign it to the variable 'MESA'
MESA = geo_three_keywords.loc[geo_three_keywords.country.isin(MESA_countries), :]

# Unstack the 'MESA' dataframe
MESA.set_index(['country','category']).unstack()

# Set the top home workout country
top_home_workout_country = 'Philippines'

# Read the 'yoga_zumba_sng.csv' file and assign it to the variable 'sng'
sng = read_file('data/yoga_zumba_sng.csv')

# Read the 'yoga_zumba_phl.csv' file and assign it to the variable 'phl'
phl = read_file('data/yoga_zumba_phl.csv')

# Define a list of pilot content
pilot_content = ['yoga', 'zumba']
