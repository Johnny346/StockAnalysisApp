import plotly.graph_objects as go

def atr_chart(imc):
    color="gray"
    if imc<10:
        color="red"
    elif (imc>=11 and imc<22):
        color="orange"
    elif imc>= 23:
        color="green"
    fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = imc,
    mode = "gauge+number",
    title = {'text': "ATR"},
    gauge = {'axis': {'range': [None, 80]},
             'bar': {'color': color},
             'steps' : [
                 {'range': [0, 16], 'color': "white"},
                 {'range': [16, 18.5], 'color': "white"},
                 {'range': [18.5, 25], 'color': "white"},
                 {'range': [25, 30], 'color': "white"},
                 {'range': [30, 80], 'color': "white"}],
             'threshold' : {'line': {'color': color, 'width': 8}, 'thickness': 0.75, 'value': imc}}))

    
    return fig
