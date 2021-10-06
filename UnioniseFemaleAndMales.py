import os
import pandas as pd

# Load the data
data_directory = os.getcwd() + '/' # Replace this with the appropriate data directory
male_df = pd.read_csv(data_directory + 'Males.csv', index_col=0) # Load the males, where the samples are the indices
female_df = pd.read_csv(data_directory + 'Females.csv', index_col=0) # Load the females, where the samples are the indices

# Calculate the union of the indices (samples) and columns (ASVs)
male_samples = male_df.index
male_asvs = male_df.columns

female_samples = female_df.index
female_asvs = female_df.columns

combined_samples = pd.Index.union(male_samples, female_samples)
combined_asvs = pd.Index.union(male_asvs, female_asvs)

# Create the unionised dataframe
combined_df = pd.DataFrame(index=combined_samples, columns=combined_asvs)

# Fill the dataframe with the male and female data
combined_df.update(male_df)
combined_df.update(female_df)

# There will be NaNs. We fill those with 0.
combined_df.fillna(0, inplace=True)

# Save the data
combined_df.to_csv(data_directory + 'NewFemalesAndMales.csv')
