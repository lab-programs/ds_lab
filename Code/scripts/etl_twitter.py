import pandas as pd
import json

def get_big_df( file_name ):
  file = open( file_name )
  data = json.loads(file.read())
  
  df = pd.DataFrame.from_dict(data, orient='index')

  df.head()

  data['--']
  del data['--']
  dates = list(data.keys())

  dfs = {}
  for i in dates:
    df = pd.DataFrame.from_dict(data[i], orient='index')
    ids = []
    epi_dates = []
    for j, r in df.iterrows():
      ids.append(r.name)
      epi_dates.append(i)
    df['id'] = ids
    df['date'] = epi_dates
    df.columns = ['content', 'id', 'date']
    dfs[i] = df

  big_df = dfs[dates[0]]
  for i in range(1, len(dates)):
    big_df = big_df.append(dfs[dates[i]])

  big_df = big_df[['id', 'date', 'content']]
  return big_df


