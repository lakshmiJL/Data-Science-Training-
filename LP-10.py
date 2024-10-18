# Data Analysis on Covid Data Set (Part - 2 Time Series Data Analysis)

# Open the data in excel and explain the data and columns data
# Explain what is time-series data, Special Emphasis on Date_reported column present

# Import the data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Plotly is same as Matplotlib but with higher graphic standards
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#time_series = pd.read_csv('Datasets/WHO-COVID-19-global-data.csv', encoding = 'ISO-8859-1')
time_series = pd.read_csv('Datasets/WHO-COVID-19-global-data.csv')
time_series.columns = ("Date_reported","Country_code","Country","WHO_region","New_cases","Cumulative_cases","New_deaths","Cumulative_deaths")

# Date_Reported column is string, typecast it to datatime format
time_series["Date_reported"] = pd.to_datetime(time_series["Date_reported"])
print(time_series["Date_reported"].dtype)
time_series_dates = time_series.groupby('Date_reported').sum()

# Plot the basic graphs below and explain the results
fig6 = go.Figure()
fig6.add_trace(go.Scatter(x = time_series_dates.index, y = time_series_dates['Cumulative_cases'], fill = 'tonexty', line_color = 'blue'))
fig6.update_layout(title = 'Cumulative Cases Worldwide')
fig6.write_html('Fig6.html', auto_open=True)


fig7 = go.Figure()
fig7.add_trace(go.Scatter(x = time_series_dates.index, y = time_series_dates['Cumulative_deaths'], fill = 'tonexty', line_color = 'red'))
fig7.update_layout(title = 'Cumulative Deaths Worldwide')
fig7.write_html('Fig7.html', auto_open=True)

fig8 = go.Figure()
fig8.add_trace(go.Scatter(x = time_series_dates.index, y = time_series_dates['New_cases'], fill = 'tonexty', line_color = 'gold'))
fig8.update_layout(title = 'Daily New Cases Worldwide')
fig8.write_html('Fig8.html', auto_open=True)


fig9 = go.Figure()
fig9.add_trace(go.Scatter(x = time_series_dates.index, y = time_series_dates['New_deaths'], fill = 'tonexty', line_color = 'hotpink'))
fig9.update_layout(title = 'Daily Death Cases Worldwide')
fig9.write_html('Fig9.html', auto_open=True)

# Ask the student for taking a country as homework and draw the same graphs again showing the trend for the particular country as homework