# Importing relevant modules
import pandas as pd
import sys
from datetime import datetime

# Loading data files
sample_sch = pd.read_csv('Sample_schedule.csv')
sample_site = pd.read_csv('sample_site_opening_times.csv')

# Extracting day from date
sample_sch['Day'] = pd.to_datetime(sample_sch['Scheduled Truck Arrival - 1 date'])
sample_sch['Day1'] = sample_sch['Day'].apply(lambda x : x.strftime('%a'))

# Function to convert time to minutes for comparision
def convert_to_minutes(time_str):
    time_object = datetime.strptime(time_str, '%H:%M')
    total_minutes = time_object.hour * 60 + time_object.minute
    return total_minutes

# Convert start and end times to mins in sample_site
sample_site['Start_min'] = sample_site['Start'].apply(lambda x: convert_to_minutes(x))
sample_site['End_min'] = sample_site['End'].apply(lambda x: convert_to_minutes(x))

# Convert scheduled truck arrival time to mins in sample_sch
sample_sch['minutes'] = sample_sch['Scheduled Truck Arrival - 1 time'].apply(lambda x: convert_to_minutes(x))

# print(sample_sch.head(1))
# print(sample_site.head(1))
# sys.exit()

# Making a copy of the original dataframe to make necessary imputations
sample_sch_change = sample_sch.copy()


# For each row in sample_schedule we impute the missing columns -> if the scheduled time is in the range of start and end times of sample_site_opening_times of that particular site_id
for index, row in sample_sch.iterrows():
    print(index) 
    # If condition to check whether data exits and is not empty
    # Imputing value in the new dataframe wherever the combination is available
    if (sample_site.loc[(sample_site['Site_id'] == row[0]) & (sample_site['Day'] == row[-2]) & ((sample_site['Start_min'] <= row[-1]) & (sample_site['End_min'] >= row[-1]) ), 'Start'].tolist() != []) & (sample_site.loc[(sample_site['Site_id'] == row[0]) & (sample_site['Day'] == row[-2]) & ((sample_site['Start_min'] <= row[-1]) & (sample_site['End_min'] >= row[-1]) ), 'End'].tolist() != []):
        sample_sch_change.loc[index , 'Origin_band'] = f"{sample_site.loc[(sample_site['Site_id'] == row[0]) & (sample_site['Day'] == row[-2]) & ((sample_site['Start_min'] <= row[-1]) & (sample_site['End_min'] >= row[-1]) ), 'Start'].tolist()[0]}-{sample_site.loc[(sample_site['Site_id'] == row[0]) & (sample_site['Day'] == row[-2]) & ((sample_site['Start_min'] <= row[-1]) & (sample_site['End_min'] >= row[-1]) ), 'End'].tolist()[0]}"

    if (sample_site.loc[(sample_site['Site_id'] == row[1]) & (sample_site['Day'] == row[-2]) & ((sample_site['Start_min'] <= row[-1]) & (sample_site['End_min'] >= row[-1]) ), 'Start'].tolist() != []) & (sample_site.loc[(sample_site['Site_id'] == row[1]) & (sample_site['Day'] == row[-2]) & ((sample_site['Start_min'] <= row[-1]) & (sample_site['End_min'] >= row[-1]) ), 'End'].tolist() != []):
        sample_sch_change.loc[index, 'Destination_band'] = f"{sample_site.loc[(sample_site['Site_id'] == row[1]) & (sample_site['Day'] == row[-2]) & ((sample_site['Start_min'] <= row[-1]) & (sample_site['End_min'] >= row[-1]) ), 'Start'].tolist()[0]}-{sample_site.loc[(sample_site['Site_id'] == row[1]) & (sample_site['Day'] == row[-2]) & ((sample_site['Start_min'] <= row[-1]) & (sample_site['End_min'] >= row[-1]) ), 'End'].tolist()[0]}"

    if sample_site.loc[(sample_site['Site_id'] == row[0]) & (sample_site['Day'] == row[-2]) & ((sample_site['Start_min'] <= row[-1]) & (sample_site['End_min'] >= row[-1]) ), 'Start'].tolist() != []:
        sample_sch_change.loc[index, 'Origin_Start'] = sample_site.loc[(sample_site['Site_id'] == row[0]) & (sample_site['Day'] == row[-2]) & ((sample_site['Start_min'] <= row[-1]) & (sample_site['End_min'] >= row[-1]) ), 'Start'].tolist()[0]

    if sample_site.loc[(sample_site['Site_id'] == row[0]) & (sample_site['Day'] == row[-2]) & ((sample_site['Start_min'] <= row[-1]) & (sample_site['End_min'] >= row[-1]) ), 'End'].tolist() != []:
        sample_sch_change.loc[index, 'Origin_End'] = sample_site.loc[(sample_site['Site_id'] == row[0]) & (sample_site['Day'] == row[-2]) & ((sample_site['Start_min'] <= row[-1]) & (sample_site['End_min'] >= row[-1]) ), 'End'].tolist()[0]

    if sample_site.loc[(sample_site['Site_id'] == row[1]) & (sample_site['Day'] == row[-2]) & ((sample_site['Start_min'] <= row[-1]) & (sample_site['End_min'] >= row[-1]) ), 'Start'].tolist() != []:
        sample_sch_change.loc[index, 'Destination_Start'] = sample_site.loc[(sample_site['Site_id'] == row[1]) & (sample_site['Day'] == row[-2]) & ((sample_site['Start_min'] <= row[-1]) & (sample_site['End_min'] >= row[-1]) ), 'Start'].tolist()[0]
        
    if sample_site.loc[(sample_site['Site_id'] == row[1]) & (sample_site['Day'] == row[-2]) & ((sample_site['Start_min'] <= row[-1]) & (sample_site['End_min'] >= row[-1]) ), 'End'].tolist() != []:
        sample_sch_change.loc[index, 'Destination_End'] = sample_site.loc[(sample_site['Site_id'] == row[1]) & (sample_site['Day'] == row[-2]) & ((sample_site['Start_min'] <= row[-1]) & (sample_site['End_min'] >= row[-1]) ), 'End'].tolist()[0]

# Writing the imputed schedule to a CSV
sample_sch_change.to_csv('final_schedule.csv')