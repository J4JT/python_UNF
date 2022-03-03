import numpy as np

#Make numpy array and display shape
data_array=np.genfromtxt('brfss-cdc.csv', skip_header= 1, delimiter=',')



sliced_array=data_array[:5,0:]
print('First Five Rows of the Data:')
print (sliced_array)
print('shape of the data: ',end='')
print(data_array.shape)

print('Descriptive Statistices for Weight Change Data:')

#get the required array which is the change in weight

data_array_curr=data_array[:,[2]]
data_array_past=data_array[:,[3]]
data_array_change=data_array_curr-data_array_past

weight_change=np.mean(data_array_change)
weight_median_change=np.median(data_array_change)
weight_standard_dev=np.std(data_array_change)
q75, q25 = np.percentile(data_array_change, [75, 25], axis=0)
iqr = float(q75 - q25)
print('')
print('Mean: ',end='')
print(weight_change)
print('Median: ',end='')
print(weight_median_change)
print('Standard_dev: ' ,end='')
print ('%.2f' % weight_standard_dev)
print('Interquartile Range: ',end='')
print(iqr)
#appending arrays
weight_appended_data=np.append(data_array, data_array_change, axis=1)
print('')
print(weight_appended_data[:5,0:])
print('Shape of the data: ',end='')
print(weight_appended_data.shape)

#target male attribute
print('\n')
male_weight=weight_appended_data[weight_appended_data[:,5]==1]
print('First Five Rows Relevant to Males')
print(male_weight[:5,0:])
print('Shape of the data: ',end='')
print(male_weight.shape)
print('\n')
print('Descriptive Statistices for Data relevant to Males')
data_array_curr_male=male_weight[:,[2]]
data_array_past_male=male_weight[:,[3]]
data_array_change_male=data_array_curr_male-data_array_past_male

weight_change_male=np.mean(data_array_change_male)
weight_median_change_male=np.median(data_array_change_male)
weight_standard_dev_male=np.std(data_array_change_male)
q75, q25 = np.percentile(data_array_change_male, [75, 25], axis=0)
iqr_male = float(q75 - q25)

print('Mean: ',end='')
print('%.2f' % weight_change_male)
print('Median: ',end='')
print(weight_median_change_male)
print('Standard_dev: ' ,end='')
print ('%.2f' % weight_standard_dev_male)
print('Interquartile Range: ',end='')
print(iqr_male)
print('\n')
#target female attribute
female_weight=weight_appended_data[weight_appended_data[:,5]==2]
print('First Five Rows Relevant to Females')
print(female_weight[:5,0:])
print('Shape of the data: ', end='')
print(female_weight.shape)

print('\n')

print('Descriptive Statistices for Data relevant to Females')
data_array_curr_female=female_weight[:,[2]]
data_array_past_female=female_weight[:,[3]]
data_array_change_female=data_array_curr_female-data_array_past_female

print('\n')
weight_change_female=np.mean(data_array_change_female)
weight_median_change_female=np.median(data_array_change_female)
weight_standard_dev_female=np.std(data_array_change_female)
q75, q25 = np.percentile(data_array_change_male, [75, 25], axis=0)
iqr_female = float(q75 - q25)


print('Mean: ',end='')
print('%.2f' % weight_change_female)
print('Median: ',end='')
print(weight_median_change_female)
print('Standard_dev: ' ,end='')
print('%.2f' % weight_standard_dev_female)
print('Interquartile Range: ',end='')
print(iqr_female)