import pandas as pd
import dash_express_components as dxc

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
df_meta = dxc.get_meta(df)