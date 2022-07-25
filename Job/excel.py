import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

excel_file = 'F:/SIZING/find_error.xlsx'
shrimp = pd.read_excel(excel_file, sheet_name= 0)

fig = make_subplots(rows=2, cols=2, shared_yaxes=False)

df = shrimp.groupby('Focus').agg('count').reset_index()
fig.add_trace(go.Bar(x=df["Focus"], y=df["Name picture"], name='Focus', marker=dict(color=[2, 3], coloraxis="coloraxis")), 1, 1)

df = shrimp.groupby("Water level").agg('count').reset_index()
fig.add_trace(go.Bar(x=df["Water level"], y=df["Name picture"], name='Water level', marker=dict(color=[4, 5, 6], coloraxis="coloraxis")), 2, 1)

df = shrimp.groupby("Skew").agg('count').reset_index()
fig.add_trace(go.Bar(x=df["Skew"], y=df["Name picture"], name='Skew', marker=dict(color=[2, 3], coloraxis="coloraxis")), 1, 2)

df = shrimp.groupby("Density").agg('count').reset_index()
fig.add_trace(go.Bar(x=df["Density"], y=df["Name picture"], name='Density', marker=dict(color=[4, 5, 6], coloraxis="coloraxis")), 2, 2)

fig.update_layout(coloraxis=dict(colorscale='Bluered_r'), showlegend=False)
fig.write_html('D:/error_picture_sizing.html')
fig.show()

