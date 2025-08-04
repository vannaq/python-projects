# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSVs
workoutData = pd.read_csv('datacamp/basic_projects/conducting_market_analysis/data/workout.csv')
keywords = pd.read_csv('datacamp/basic_projects/conducting_market_analysis/data/three_keywords.csv')
workout_geo = pd.read_csv('datacamp/basic_projects/conducting_market_analysis/data/workout_geo.csv', index_col=0)

# Using a simple plot function that's well-suited for quick and easy scripts
def simple_plot_data():
    x = workoutData['month']
    y = workoutData['workout_worldwide']
    plt.plot(x, y)
    plt.xlabel("YYYY-MM")
    plt.ylabel("Popularity of Search")
    plt.xticks(rotation=90)
    plt.show() 

# Plotting two charts side by side
def plot_data():
    # More robust plotting function with more control over axes
    _fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5)) #creates a figure with axes

    # First plot
    x = workoutData['month']
    y = workoutData['workout_worldwide']
    ax1.plot(x, y)
    ax1.set_xlabel('YYYY-MM')
    ax1.set_ylabel("Popularity of search")
    ax1.set_xticks(x)
    ax1.set_xticklabels(x, rotation=90)

    # Second plot
    x1 = keywords['month']
    y1 = keywords['home_workout_worldwide']
    y2 = keywords['gym_workout_worldwide']
    y3 = keywords['home_gym_worldwide']

    # Plotting each line
    ax2.plot(x1, y1, label='home workout')
    ax2.plot(x1, y2, label='gym workout')
    ax2.plot(x1, y3, label='home gym')

    # Labeling axes & legend
    ax2.set_xticks(x1)
    ax2.set_xticklabels(x1, rotation=90, fontsize=8)
    plt.margins(x=0.0001)
    plt.legend()
    plt.show()

# Prints project answers
def print_answers():
    peak_covid = 'home workout'
    current = 'gym workout'
    year_str = "2020"
    top_country = "United States"
    home_workout_geo = 'Philippines'

    print("\n\n----------ANSWER KEY-------------")
    print(f"Peak Covid search: {peak_covid}")
    print(f"Current most popular search: {current}")
    print(f"Year of peak interest for workout: {year_str}")
    print(f"Country with highest interest for workouts: {top_country}")
    print(f"Country most interested in home workouts: {home_workout_geo}")


if __name__ == '__main__':
    print_answers()
    plot_data()

