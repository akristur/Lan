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
fig.add_trace(go.Scatter(x=Nr[1:], y=A[1:], mode='lines', name='óverðtr. jafnar afb.'), row=2, col=1)
fig.add_trace(go.Scatter(x=Nr[1:], y=A[1:], mode='lines', name='verðtr. jafnar gr.'), row=2, col=1)
fig.add_trace(go.Scatter(x=Nr[1:], y=A[1:], mode='lines', name='verðtr. jafnar afb.'), row=2, col=1)

fig.add_trace(go.Scatter(x=Nr[1:], y=V[1:], mode='lines', name='óverðtr. jafnar gr.'), row=2, col=2)
fig.add_trace(go.Scatter(x=Nr[1:], y=V[1:], mode='lines', name='óverðtr. jafnar afb.'), row=2, col=2)
fig.add_trace(go.Scatter(x=Nr[1:], y=V[1:], mode='lines', name='verðtr. jafnar gr.'), row=2, col=2)
fig.add_trace(go.Scatter(x=Nr[1:], y=V[1:], mode='lines', name='verðtr. jafnar afb.'), row=2, col=2)

# Update layout and titles
fig.update_layout(
    title_text="Loan Analysis with Interactive Sliders",
    height=1000,  # Adjusted height
    width=1200,  # Adjusted width
    showlegend=False,
    margin=dict(l=50, r=50, t=50, b=300)  # Adjusted margins for slider space
)

# Create slider steps
def create_slider_steps(parameter_range, parameter_name):
    steps = [
        dict(
            label=f'{value}',
            method='update',
            args=[{'visible': [False] * len(fig.data)}]
        )
        for value in parameter_range
    ]

    for step in steps:
        if parameter_name == 'H':
            H_value = int(step['label'])
            G, A, V, Eeg, Nr = update_loan_data(H_value, rN, rR, ir, L)
        elif parameter_name == 'rN':
            rN_value = float(step['label'])
            G, A, V, Eeg, Nr = update_loan_data(H, rN_value, rR, ir, L)
        elif parameter_name == 'rR':
            rR_value = float(step['label'])
            G, A, V, Eeg, Nr = update_loan_data(H, rN, rR_value, ir, L)
        elif parameter_name == 'ir':
            ir_value = float(step['label'])
            G, A, V, Eeg, Nr = update_loan_data(H, rN, rR, ir_value, L)
        elif parameter_name == 'L':
            L_value = int(step['label'])
            G, A, V, Eeg, Nr = update_loan_data(H, rN, rR, ir, L_value)
        
        step['args'][0]['visible'] = [True] * len(fig.data)
        step['args'][0]['x'] = [Nr] * len(fig.data)
        step['args'][0]['y'] = [
            Eeg[:,0], Eeg[:,1], Eeg[:,2], Eeg[:,3],
            G[1:,0], G[1:,1], G[1:,2], G[1:,3],
            A[1:,0], A[1:,1], A[1:,2], A[1:,3],
            V[1:,0], V[1:,1], V[1:,2], V[1:,3]
        ]
    return steps

# Define the parameter ranges for sliders
H_range = [i * 1000000 for i in range(5, 61)]
rN_range = [i for i in range(1, 11)]
rR_range = [i / 10 for i in range(1, 101)]
ir_range = [i for i in range(0, 11)]
L_range = [i for i in range(5, 41)]

# Create sliders for each parameter
sliders = [
    dict(
        active=0,
        currentvalue={"prefix": "", "visible": False},  # Hide current value display
        pad={"b": 20},
        steps=create_slider_steps(H_range, 'H'),
        len=0.7,
        x=0.5,
        y=-0.1,  # Position below the graph
        xanchor="center"
    ),
    dict(
        active=0,
        currentvalue={"prefix": "", "visible": False},  # Hide current value display
        pad={"b": 20},
        steps=create_slider_steps(rN_range, 'rN'),
        len=0.7,
        x=0.5,
        y=-0.2,  # Position below the graph
        xanchor="center"
    ),
    dict(
        active=0,
        currentvalue={"prefix": "", "visible": False},  # Hide current value display
        pad={"b": 20},
        steps=create_slider_steps(rR_range, 'rR'),
        len=0.7,
        x=0.5,
        y=-0.3,  # Position below the graph
        xanchor="center"
    ),
    dict(
        active=0,
        currentvalue={"prefix": "", "visible": False},  # Hide current value display
        pad={"b": 20},
        steps=create_slider_steps(ir_range, 'ir'),
        len=0.7,
        x=0.5,
        y=-0.4,  # Position below the graph
        xanchor="center"
    ),
    dict(
        active=0,
        currentvalue={"prefix": "", "visible": False},  # Hide current value display
        pad={"b": 20},
        steps=create_slider_steps(L_range, 'L'),
        len=0.7,
        x=0.5,
        y=-0.5,  # Position below the graph
        xanchor="center"
    )
]

# Add sliders to the layout with labels and value boxes as annotations
annotations = [
    dict(x=0.45, y=-0.1 - i * 0.1, text=label, showarrow=False, xanchor="right", yanchor="middle", font=dict(size=16, color="#000"))
    for i, label in enumerate(["H", "rN", "rR", "ir", "L"])
]

value_boxes = [
    dict(x=0.46, y=-0.1 - i * 0.1, text=f"{value}", showarrow=False, xanchor="left", yanchor="middle", font=dict(size=16, color="#000"))
    for i, value in enumerate([H, rN, rR, ir, L])
]

fig.update_layout(
    sliders=sliders,
    height=1000,  # Adjusted height for better slider positioning
    annotations=annotations + value_boxes
)

# Save and open in browser
fig.write_html('plot.html', auto_open=True)
