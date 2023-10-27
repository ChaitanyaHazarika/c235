import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

dataset = pd.read_csv('projectC234_EPL.csv')

footballClub = dataset['Club'].value_counts().head(20)

print(footballClub)

clubFig = go.Figure(data = [go.Pie(label= footballClub.index, values = footballClub.values, hole= .5 )])
clubFig.show()


