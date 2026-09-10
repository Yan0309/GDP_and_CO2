import pandas as pd
# read the file
world = pd.read_csv(
    "https://github.com/nickeubank/MIDS_Data/"
    "raw/refs/heads/master/World_Development_Indicators/"
    "wdi_small_tidy_2015.csv"
)
# make a scatter plot for mortality rate per 1000 live briths and GDP
world = world.plot.scatter(
    "Mortality rate, infant (per 1,000 live births)",
    "GDP per capita (constant 2010 US$)",
)
