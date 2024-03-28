Problem Statement: 
We have prepared a schedule which is provided in sample_data.zip folder called sample_schedule which is a masked representation of where the trucks would be moving and on which date and which time. Also there’s another file in same folder called sample_site_opening_times which has the information of hours at which sites operate on a specific day of week. The task is to print the values from sample_site_opening_times file to sample_schedule file for all the columns that are highlighted in yellow (Column P to Q in case of any formatting error).

 

Sample:
Check the first load as :
ORIGN is DNE2 and DESTINATION is NCL1.
Check the pickup date from DNE2 in column Scheduled Truck Arrival - 1 date and pickup time from column Scheduled Truck Arrival - 1 time  and then identify the day of week i.e. Monday and then go to sample_site_opening_times file and check its opening times for Monday as below:
The scheduled pickup from DNE2 falls in 0:00-9:00 bucket and hence you have to print 0:00-9:00 in column Origin_band and then 3/18/2024 0:00 in column Origin_Start and 3/18/2024 9:00 in column Origin_End
Repeat the same process for destinations

Outputs required: 
You are expected to share the updated excel files (all highlighted columns filled and python code in .py file along with comments explaining the thought process behind)
