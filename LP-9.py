# Data Analysis on Covid Data Set , Part - 1 (Aggregated Data)

# Open the data set in excel and explain the use of each column

# Import the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Plotly is same as Matplotlib but with higher graphic standards
import plotly
import plotly.express as px
import plotly.graph_objects as go   
from plotly.subplots import make_subplots

data = pd.read_csv("Datasets/covid_data.csv")
data = data[['Province_State', 'Country_Region', 'Last_Update', 'Lat', 'Long_', 'Confirmed', 'Recovered', 'Deaths', 'Active']]
data.columns = ('State','Country','Last Update','Lat','Long','Confirmed','Recovered','Deaths','Active')
#Print 
print(data.info())

data['State'].fillna(value = '', inplace = True)
# Top 10 most affected countries (Bubble Plot)

top10_confirmed = pd.DataFrame(data.groupby('Country')['Confirmed'].sum().nlargest(10).sort_values(ascending = False))

fig1 = px.scatter(top10_confirmed, x = top10_confirmed.index, y = 'Confirmed', size = 'Confirmed', size_max = 120, color = top10_confirmed.index, title = "Top 10 Countries by Confirmed Cases" )
fig1.write_html('Fig1.html', auto_open=True)
# This will generate the HTML file in Repl, Download the HTML File and run it with browser (preferably chrome)

# Top 10 most affected countries (Bubble Plot)

top10_deaths = pd.DataFrame(data.groupby('Country')['Deaths'].sum().nlargest(10).sort_values(ascending = False))
fig2 = px.bar(top10_deaths, x = 'Deaths', y = top10_deaths.index, height = 600, color = 'Deaths', orientation = 'h', color_continuous_scale = ['deepskyblue','red'], title = 'Top 10 Death Cases Countries')
fig2.write_html('Fig2.html', auto_open=True)

# Top 10 recovered countries (Bar plot)

top10_recovered = pd.DataFrame(data.groupby('Country')['Recovered'].sum().nlargest(10).sort_values(ascending = False))
fig3 = px.bar(top10_recovered, x = top10_recovered.index, y = 'Recovered', height = 600, color = 'Recovered', title = 'Top 10 Recovered Cases Countries', color_continuous_scale = px.colors.sequential.Viridis)
fig3.write_html('Fig3.html', auto_open=True)


# Doing the analysis 
# Do the analysis for one country give the other countries as homework prefarably taking the country name by user input
# USA
topstates_us = data['Country'] == 'US'
topstates_us = data[topstates_us].nlargest(5, 'Confirmed')
# Brazil
topstates_brazil = data['Country'] == 'Brazil'
topstates_brazil = data[topstates_brazil].nlargest(5, 'Confirmed')
# India
topstates_india = data['Country'] == 'India'
topstates_india = data[topstates_india].nlargest(5, 'Confirmed')
# Russia
topstates_russia = data['Country'] == 'Russia'
topstates_russia = data[topstates_russia].nlargest(5, 'Confirmed')

# USA 
fig4 = go.Figure(data = [
    go.Bar(name = 'Confirmed Cases', x = topstates_us['Confirmed'], y = topstates_us['State'], orientation = 'h'),
    go.Bar(name = 'Death Cases', x = topstates_us['Deaths'], y = topstates_us['State'], orientation = 'h')
])
fig4.update_layout(title = 'Most Affected States in USA', height = 600)
fig4.write_html('Fig4.html', auto_open=True)

fig5 = go.Figure(data = [
    go.Bar(name = 'Recovered Cases', x = topstates_brazil['State'], y = topstates_brazil['Recovered']),
    go.Bar(name = 'Confirmed Cases', x = topstates_brazil['State'], y = topstates_brazil['Confirmed']),
    go.Bar(name = 'Death Cases', x = topstates_brazil['State'], y = topstates_brazil['Deaths'])
])
fig5.update_layout(title = 'Most Affected States in Brazil', barmode = 'stack', height = 600)
fig5.write_html('Fig5.html', auto_open=True)
