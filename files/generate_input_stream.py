import pandas as pd



def stream_generator(raw_data):
    '''A generator which reads data from the csv 
    and returns one row at a time'''

    for i, data_point in raw_data.iterrows():

        yield data_point["x"], data_point["y"], data_point["time_stamp"]