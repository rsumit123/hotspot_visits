
def stream_generator(raw_data):
    '''A generator which takes dataframe as an input and 
    returns each row in a json format'''
    
    for i, data_point in raw_data.iterrows():
        yield data_point["x"], data_point["y"], data_point["time_stamp"]