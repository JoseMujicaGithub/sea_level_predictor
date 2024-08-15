import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress  # verry important to do linear regresions
import numpy as np



def draw_plot():
    df=pd.read_csv("epa-sea-level.csv")
    #print(df)

    df_recent = df[df['Year'] >= 2000]

    # Filter the data to include only the years from 2000 onwards
    df_recent = df[df['Year'] >= 2000]

    # Perform linear regression on the recent data
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Generate years from 2000 to 2050 for the recent trend
    years_extended_recent = np.arange(2000, 2051)

    # Calculate the corresponding sea levels for the extended years
    sea_levels_predicted_recent = slope_recent * years_extended_recent + intercept_recent

    # Plot the original scatter plot and the first line of best fit
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # First line of best fit (all data)
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended_all = np.arange(df['Year'].min(), 2051)
    sea_levels_predicted_all = slope * years_extended_all + intercept
    plt.plot(years_extended_all, sea_levels_predicted_all, color='red', label='Line of Best Fit (All Data)')

    # Second line of best fit (2000 onwards)
    plt.plot(years_extended_recent, sea_levels_predicted_recent, color='green', label='Line of Best Fit (2000 Onwards)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()
    return plt.gca()

draw_plot()