#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task2 Question 1

import pandas as pd
import networkx as nx

def calculate_distance_matrix(df):   
    
    G = nx.DiGraph()

    # Add edges with distance for dataframe
    for _, row in df.iterrows():
        G.add_edge(row['id_start'], row['id_end'], distance=row['distance'])
        G.add_edge(row['id_end'], row['id_start'], distance=row['distance'])  # Ensure symmetry

    # Get list of unique nodes
    nodes = list(G.nodes())

    # Initialize an empty matrix
    distance_matrix = pd.DataFrame(index=nodes, columns=nodes)

    # Calculate the distance and fill 0 in the matrix
    for start_node in nodes:
        for end_node in nodes:
            if start_node == end_node:
                distance_matrix.at[start_node, end_node] = 0
            else:
                try:
                    # Use networkx's shortest path length to calculate distance
                    distance = nx.shortest_path_length(G, start_node, end_node, weight='distance')
                    distance_matrix.at[start_node, end_node] = distance
                except nx.NetworkXNoPath:
                    # If no path, set distance NaN
                    distance_matrix.at[start_node, end_node] = float('nan')

    return distance_matrix

file_path = 'dataset-3.csv'
df_dataset3 = pd.read_csv(file_path)
result_matrix = calculate_distance_matrix(df_dataset3)
print(result_matrix)


# In[5]:


#Task2 Question 2

def unroll_distance_matrix(df):
    # Create empty list to store unrolled data
    unrolled_data = []

    # Iterate over the rows and columns of the distance matrix
    for id_start in df.index:
        for id_end in df.columns:
            if id_start != id_end:  # Exclude common id_start to id_end
                distance = df.at[id_start, id_end]
                unrolled_data.append({'id_start': id_start, 'id_end': id_end, 'distance': distance})

    # Create DataFrame from the unrolled data
    unrolled_df = pd.DataFrame(unrolled_data)

    return unrolled_df
result_unrolled_df = unroll_distance_matrix(result_matrix)
print(result_unrolled_df)


# In[6]:


#Task2 Question 3

def find_ids_within_ten_percentage_threshold(df, reference_id):
    
    
    
    # Calculate the average distance for reference id
    reference_avg_distance = df[df['id_start'] == reference_id]['distance'].mean()

    # Calculate the lower and upper bounds for the threshold (10%)
    lower_bound = reference_avg_distance - 0.1 * reference_avg_distance
    upper_bound = reference_avg_distance + 0.1 * reference_avg_distance

    # Filter the DataFrame based on the threshold
    filtered_df = df[(df['id_start'] != reference_id) & (df['distance'] >= lower_bound) & (df['distance'] <= upper_bound)]

    return filtered_df

reference_id = 1001472

# Replace with the desired reference id
result_filtered_df = find_ids_within_ten_percentage_threshold(result_unrolled_df, reference_id)
print(result_filtered_df)


# In[8]:


#Task2 Question 4

def calculate_toll_rate(df):
    
    # Rate coefficients for each vehicle type
    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}

    # Add columns for each vehicle type and calculate toll rate
    for vehicle_type, rate_coefficient in rate_coefficients.items():
        column_name = f'{vehicle_type}_tolls'
        df[column_name] = df['distance'] * rate_coefficient

    return df

result_with_toll_rates = calculate_toll_rate(result_unrolled_df)
print(result_with_toll_rates)


# In[ ]:




