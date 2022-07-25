import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

excel_file = 'F:/SIZING/ratio.xlsx'
ratio = pd.read_excel(excel_file, sheet_name= 0)

fig = go.Figure(data=[
    go.Bar(name= 'blue count', x= ratio['date'], y= ratio['blue_count'], text= ratio['count_missing_joints_percentage']),
    go.Bar(name= 'white count', x= ratio['date'], y= ratio['white_count'], text= ratio['count_bow_percentage']),
    go.Bar(name= 'total', x= ratio['date'], y= ratio['total'], text= (100 - ratio['count_missing_joints_percentage']- ratio['count_bow_percentage']))
])
fig.update_layout(barmode='stack')
fig.write_html('F:/ratio.html')
# fig.show()
