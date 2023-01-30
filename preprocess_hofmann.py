import pandas as pd
import glob
path = "C:/Users/sradhakrishnan/Music/impakt_ga/data/hofmann2/process graph/*.csv"
files = glob.glob(path)
print(files)
print("Resultant CSV after joining all CSV files at a particular location...")

# joining files with concat and read_csv
content = []
for i in range(len(files)):
    df = pd.read_csv(files[i], sep=";")
    content.append(df)
# converting content to data frame
data_frame = pd.concat(content)
print(data_frame)
data_frame.to_csv("hoffman_v1_rflp.csv")