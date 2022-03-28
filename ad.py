import pandas as pd

def question1(start_dt, end_dt, condition):
	out=pd.read_csv('out.csv')
	targets=pd.read_csv('targets.csv')

	output1=pd.merge(out, targets, 
					  how='inner', 
					  on='HASH')

	output1['UNIXTIME_GMT'] = pd.to_datetime(output1['UNIXTIME_GMT'], unit='s')

	#Note, I had to put it like this because there is no value in csv with time exactly at 12:00:00
	output1 = output1.loc[(output1.UNIXTIME_GMT >= start_dt) & (output1.UNIXTIME_GMT <= end_dt)] 

	for x in output1.index[:1]:	
	    print('The location of user at '+condition+' is: ', output1['CITY'][x], '-', output1['UNIXTIME_GMT'][x])


def question2(start_dt, condition):
	out=pd.read_csv('out.csv')
	targets=pd.read_csv('targets.csv')

	output1=pd.merge(out, targets, 
					  how='inner', 
					  on='HASH')

	output1['UNIXTIME_GMT'] = pd.to_datetime(output1['UNIXTIME_GMT'], unit='s')

	output1 = output1.loc[(output1.UNIXTIME_GMT < start_dt)] 
	output1 = output1.sort_values(by='UNIXTIME_GMT', ascending=False, kind='quicksort')

	for x in output1.index[:1]:	
	    print('The last location of user before '+condition+' is: ', output1['CITY'][x], '-', output1['UNIXTIME_GMT'][x])


question1(pd.to_datetime("2021-09-24 12:00:00"), pd.to_datetime("2021-09-24 12:00:01"), '12:00');
question1(pd.to_datetime("2021-09-24 14:10:00"), pd.to_datetime("2021-09-24 14:10:10"), '14:10');

question2(pd.to_datetime("2021-09-24 12:00:00"), '12:00');
question2(pd.to_datetime("2021-09-24 14:10:00"), '14:10');