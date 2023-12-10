#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Task1 Question 1


import pandas as pd

def generate_car_matrix(dataset):
    # Assuming dataset is a DataFrame read from dataset-1.csv
    df = pd.read_csv('dataset-1.csv')

    # Extract unique values from id_1 and id_2 columns
    id_1_values = df['id_1'].unique()
    id_2_values = df['id_2'].unique()

    # Create a new DataFrame with id_2 values as columns and id_1 values as index
    result_df = pd.DataFrame(index=id_1_values, columns=id_2_values)

    # Fill the DataFrame with values from the car column
    for i, row in df.iterrows():
        result_df.at[row['id_1'], row['id_2']] = row['car']

    # Fill diagonal values with 0
    result_df = result_df.fillna(0)

    return result_df




dataset_path = pd.read_csv('dataset-1.csv')
result_matrix = generate_car_matrix(dataset_path)
print(result_matrix)


# In[8]:


#Task1 Question 2
import pandas as pd

def get_type_count(dataset, output_file):
    df = pd.read_csv(dataset)
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')],
                            labels=['low', 'medium', 'high'], right=False)
    type_counts = df['car_type'].value_counts().to_dict()
    sorted_type_counts = dict(sorted(type_counts.items()))

    # Convert to DataFrame for better formatting
    result_df = pd.DataFrame(list(sorted_type_counts.items()), columns=['Car Type', 'Count'])

    # Save to Excel file
    result_df.to_excel(output_file, index=False)

# Example usage
dataset_path = 'dataset-1.csv'
output_excel_path = 'output_file.xlsx'
get_type_count(dataset_path, output_excel_path)


print(result_type_count)   


# In[11]:


#Task1 Question 3

def get_bus_indexes(dataset):
    df1 = pd.read_csv(dataset)
    mean_bus_value = df1['bus'].mean()
    bus_indexes = df1[df1['bus'] > 2 * mean_bus_value].index.tolist()
    bus_indexes.sort()
    return bus_indexes


result_bus_indexes = get_bus_indexes('dataset-1.csv')
print(result_bus_indexes)


# In[5]:


#Task1 Question 4

def filter_routes(dataset):
    df = pd.read_csv(dataset)
    filtered_routes = df.groupby('route')['truck'].mean().loc[lambda x: x > 7].index.tolist()
    return sorted(filtered_routes)


result_filtered_routes = filter_routes('dataset-1.csv')
print(result_filtered_routes)


# In[10]:


#Task1 Question 5

def multiply_matrix(df):
    modified_df = df.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    modified_df = modified_df.round(1)
    return modified_df

# Example usage
modified_result_matrix = multiply_matrix(result_matrix)
print(modified_result_matrix)


# In[6]:


#Task1 Question 6

def time_completeness_check(dataset):
    df = pd.read_csv(dataset)

    # Mapping day names to numerical values (Monday: 0, Tuesday: 1, ..., Sunday: 6)
    day_mapping = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6
    }

    # Convert 'startDay' and 'endDay' to numerical values
    df['startDay_numeric'] = df['startDay'].map(day_mapping)
    df['endDay_numeric'] = df['endDay'].map(day_mapping)

    # Combine 'startDay_numeric' and 'startTime' to create 'start_timestamp'
    df['start_timestamp'] = pd.to_datetime(df['startDay_numeric'].astype(str) + ' ' + df['startTime'], errors='coerce')

    # Combine 'endDay_numeric' and 'endTime' to create 'end_timestamp'
    df['end_timestamp'] = pd.to_datetime(df['endDay_numeric'].astype(str) + ' ' + df['endTime'], errors='coerce')

    # Combine 'start_timestamp' and 'end_timestamp' to create 'timestamp'
    df['timestamp'] = pd.concat([df['start_timestamp'], df['end_timestamp']], axis=1).max(axis=1)

    # Create a boolean series indicating if each (id, id_2) pair has incorrect timestamps
    completeness_check = df.groupby(['id', 'id_2']).apply(
        lambda group: (
            group['timestamp'].dt.hour.nunique() == 24 and
            set(group['timestamp'].dt.dayofweek.unique()) == set([0, 1, 2, 3, 4, 5, 6])
        )
    )

    return completeness_check


result_time_completeness_check = time_completeness_check('dataset-2.csv')
print(result_time_completeness_check)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




