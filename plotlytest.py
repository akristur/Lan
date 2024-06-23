import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Basic Plotly Figure"
)

fig.write_html('plot.html', auto_open=True)
