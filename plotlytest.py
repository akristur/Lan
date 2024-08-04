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
fig.add_trace(go.Scatter(x=Nr[1:], y=A[1:,3], mode='lines', name='verðtr. jafnar afb.'), row=2, col=1)

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

# Create slider steps
H_slider = [
    dict(
        label=f'{i*1000000}',
        method='update',
        args=[{'visible': [False] * len(fig.data)}]
    )
    for i in range(5, 61)
]

for i, step in enumerate(H_slider):
    # Update each step with the corresponding data visibility and create a new data set
    H_value = (i + 5) * 1000000
    G, A, V, Eeg, Nr = update_loan_data(H_value, rN, rR, ir, L)
    
    step['args'][0]['visible'] = [True] * len(fig.data)
    step['args'][0]['x'] = [Nr] * len(fig.data)
    step['args'][0]['y'] = [
        Eeg[:,0], Eeg[:,1], Eeg[:,2], Eeg[:,3],
        G[1:,0], G[1:,1], G[1:,2], G[1:,3],
        A[1:,0], A[1:,1], A[1:,2], A[1:,3],
        V[1:,0], V[1:,1], V[1:,2], V[1:,3]
    ]

# Add slider to the layout
fig.update_layout(
    sliders=[{
        'active': 0,
        'currentvalue': {"prefix": "H: "},
        'pad': {"t": 50},
        'steps': H_slider
    }]
)

# Save and open in browser
fig.write_html('plot.html', auto_open=True)