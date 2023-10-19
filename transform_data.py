import pandas as pd 

def transform_data():
    
    df = pd.read_csv('bike_data_velib.csv')

    # Feature Engineering
    occupancy_rate = df['empty_slots'] / df['slots'] * 100
    df['occupancy_rate'] = occupancy_rate

    #epoch time 
    df['last_updated'] = pd.to_datetime((df['last_updated']), utc=True)
    df['timestamp'] = pd.to_datetime((df['timestamp']), utc=True)
    
    #drop column
    df.drop('station_id', axis=1, inplace=True)

    
    df.to_csv('transformed_bike_data.csv', index=False) 

    return df

transformed_df = transform_data()

