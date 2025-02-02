import plotly.graph_objects as go

x_data = [1, 2, 3, 4, 5]
y_data = [2, 1, 4, 3, 5]

fig = go.Figure()
fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines+markers', name='Demo'))

fig.update_layout(
    title="My Plotly Demo Chart",
    xaxis_title="X Axis",
    yaxis_title="Y Axis"
)

# Write to HTML snippet
fig.write_html("assets/plotly_demo.html", include_plotlyjs="cdn", full_html=False)
