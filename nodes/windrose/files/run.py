#!/usr/bin/env python3
from rndflow import job
import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, r="frequency", theta="direction",
                   color="strength", template="plotly_dark",
                   color_discrete_sequence= px.colors.sequential.Plasma_r)

job.save_package(label='windrose', images=dict(windrose=fig))