import pandas as pd
from process_visits import process_visits_pythogoras, process_visits_divisive
from generate_input_stream import stream_generator

# reading the raw_data csv file with pandas
raw_data = pd.read_csv("files/raw_data.csv")

# reading the hotspot csv file with pandas

hotpot_data = pd.read_csv("files/hotpot_data.csv")

# generate a stream of input data using raw data csv
input_stream = stream_generator(raw_data)

# calculate the output dictionary for storing the timestamps each hotspots were visited on

all_visits_pythogoras, time_taken_pythogoras = process_visits_pythogoras(
    raw_data, hotpot_data, input_stream
)

print(
    f"Time taken for processing {raw_data.shape[0]} datapoints using the pythogoras approach is {time_taken_pythogoras}"
)

# write output to a csv file

output_pythogoras = pd.DataFrame.from_dict(
    all_visits_pythogoras, orient="index", columns=["timestamps"]
)

output_pythogoras.to_csv("files/output_pythgoras.csv")

# generate a stream of input data using raw data csv
input_stream = stream_generator(raw_data)

# calculate the output dictionary for storing the timestamps each hotspots were visited on

all_visits_divisive, time_taken_divisive = process_visits_divisive(
    raw_data, hotpot_data, input_stream
)

print(
    f"Time taken for processing {raw_data.shape[0]} datapoints using the divisive approach is {time_taken_divisive}"
)

# Write output to csv

output_divisive = pd.DataFrame.from_dict(
    all_visits_divisive, orient="index", columns=["timestamps"]
)

output_divisive.to_csv("files/output_divisive.csv")
