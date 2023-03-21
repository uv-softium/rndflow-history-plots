#!/usr/bin/env python3
from rndflow import job
import numpy as np
import plotly.graph_objects as go

x = np.linspace(0,10,100)
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=np.sin(x), name='sin'))
fig.add_trace(go.Scatter(x=x, y=np.cos(x), name='cos'))

job.save_package(label='line', images=dict(line=fig))