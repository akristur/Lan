import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from lanareikn import reiknalan

# Initial parameters
H = 38000000
rN = 10
rR = 2.6
ir = 4
L = 40

def update_loan_data(H, rN, rR, ir, L):
    G, A, V, Eeg, Nr = reiknalan(H, rN, rR, ir, L)
    return G, A, V, Eeg, Nr

# Initial loan data
G, A, V, Eeg, Nr = update_loan_data(H, rN, rR, ir, L)

# Create figure with subplots
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Eftirstöðvar höfuðstóls', 'Mánaðarleg greiðsla', 'Afborgun af höfuðstól', 'Vextir af greiðslu')
)

# Add initial traces to the figure
fig.add_trace(go.Scatter(x=Nr, y=Eeg[:,0], mode='lines', name='óverðtr. jafnar gr.'), row=1, col=1)
fig.add_trace(go.Scatter(x=Nr, y=Eeg[:,1], mode='lines', name='óverðtr. jafnar afb.'), row=1, col=1)
fig.add_trace(go.Scatter(x=Nr, y=Eeg[:,2], mode='lines', name='verðtr. jafnar gr.'), row=1, col=1)
fig.add_trace(go.Scatter(x=Nr, y=Eeg[:,3], mode='lines', name='verðtr. jafnar afb.'), row=1, col=1)

fig.add_trace(go.Scatter(x=Nr[1:], y=G[1:,0], mode='lines', name='óverðtr. jafnar gr.'), row=1, col=2)
fig.add_trace(go.Scatter(x=Nr[1:], y=G[1:,1], mode='lines', name='óverðtr. jafnar afb.'), row=1, col=2)
fig.add_trace(go.Scatter(x=Nr[1:], y=G[1:,2], mode='lines', name='verðtr. jafnar gr.'), row=1, col=2)
fig.add_trace(go.Scatter(x=Nr[1:], y=G[1:,3], mode='lines', name='verðtr. jafnar afb.'), row=1, col=2)

fig.add_trace(go.Scatter(x=Nr[1:], y=A[1:,0], mode='lines', name='óverðtr. jafnar gr.'), row=2, col=1)
fig.add_trace(go.Scatter(x=Nr[1:], y=A[1:,1], mode='lines', name='óverðtr. jafnar afb.'), row=2, col=1)
fig.add_trace(go.Scatter(x=Nr[1:], y=A[1:,2], mode='lines', name='verðtr. jafnar gr.'), row=2, col=1)
fig.add_trace(go.Scatter(x=Nr[1:], y=A[1:], mode='lines', name='verðtr. jafnar afb.'), row=2, col=1)

fig.add_trace(go.Scatter(x=Nr[1:], y=V[1:,0], mode='lines', name='óverðtr. jafnar gr.'), row=2, col=2)
fig.add_trace(go.Scatter(x=Nr[1:], y=V[1:,1], mode='lines', name='óverðtr. jafnar afb.'), row=2, col=2)
fig.add_trace(go.Scatter(x=Nr[1:], y=V[1:,2], mode='lines', name='verðtr. jafnar gr.'), row=2, col=2)
fig.add_trace(go.Scatter(x=Nr[1:], y=V[1:,3], mode='lines', name='verðtr. jafnar afb.'), row=2, col=2)

# Update layout and titles
fig.update_layout(
    title_text="Loan Analysis with Interactive Sliders",
    height=700,
    showlegend=False
)

# Function to update graph
def create_update_figure(H, rN, rR, ir, L):
    G, A, V, Eeg, Nr = update_loan_data(H, rN, rR, ir, L)
    new_data = [
        Eeg[:,0], Eeg[:,1], Eeg[:,2], Eeg[:,3],
        G[1:,0], G[1:,1], G[1:,2], G[1:,3],
        A[1:,0], A[1:,1], A[1:,2], A[1:,3],
        V[1:,0], V[1:,1], V[1:,2], V[1:,3]
    ]
    return new_data

# Sliders
sliders = [
    dict(
        active=0,
        currentvalue={"prefix": "H: "},
        pad={"t": 50},
        steps=[dict(label=f'{i*1000000}', method='update', args=[{'args': [create_update_figure(i*1000000, rN, rR, ir, L)], 'mode': 'immediate', 'frame': {'duration': 0, 'redraw': True}}]) for i in range(5, 61)]
    ),
    #dict(
    #   active=0,
    #    currentvalue={"prefix": "ir: "},
    #    pad={"t": 50},
    #    steps=[dict(label=f'{i}', method='update', args=[{'args': [create_update_figure(H, rN, rR, i, L)], 'mode': 'immediate', 'frame': {'duration': 0, 'redraw': True}}]) for i in range(0, 11)]
    #),
    #dict(
    #    active=0,
    #    currentvalue={"prefix": "rN: "},
    #    pad={"t": 50},
    #    steps=[dict(label=f'{i}', method='update', args=[{'args': [create_update_figure(H, i, rR, ir, L)], 'mode': 'immediate', 'frame': {'duration': 0, 'redraw': True}}]) for i in range(1, 11)]
    #),
    #dict(
    #    active=0,
    #    currentvalue={"prefix": "rR: "},
    #    pad={"t": 50},
    #    steps=[dict(label=f'{i/10}', method='update', args=[{'args': [create_update_figure(H, rN, i/10, ir, L)], 'mode': 'immediate', 'frame': {'duration': 0, 'redraw': True}}]) for i in range(1, 101)]
    #),
    #dict(
    #    active=0,
    #    currentvalue={"prefix": "L: "},
    #    pad={"t": 50},
    #    steps=[dict(label=f'{i}', method='update', args=[{'args': [create_update_figure(H, rN, rR, ir, i)], 'mode': 'immediate', 'frame': {'duration': 0, 'redraw': True}}]) for i in range(5, 41)]
    #)
]

fig.update_layout(
    sliders=sliders
)

# Save and open in browser
fig.write_html('plot.html', auto_open=True)