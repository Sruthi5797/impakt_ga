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
df1 = data_frame[data_frame.duplicated()]
df1.fillna(0)
df1.to_csv("data.csv")
print(data_frame.drop_duplicates(["source","target"]))
df_bidirectional = data_frame.drop_duplicates(["source","target"],keep="first")
df_bidirectional.reset_index(inplace = True, drop = True)
df_bidirectional.to_csv("tg_data.csv")