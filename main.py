import os

import numpy as np
import pandas as pd
import holoviews as hv
import hvplot.pandas
from bokeh.io import curdoc
from matplotlib.cm import YlGnBu_r
import geoviews as gv
import cartopy
import datashader
from holoviews.operation.datashader import rasterize, shade, datashade


hv.extension("bokeh")


# Data:
datos_airbnb = pd.read_parquet(os.path.join("datos_airbnb", "airbnb_listings.parquet"), 
                           engine="fastparquet"
                          )


# Charts:

tiles_carto_oscuras = gv.tile_sources.CartoDark

scatter_airbnb = datos_airbnb.hvplot(kind="scatter",
                                     x="long_mercator",
                                     y="lat_mercator",
                                     c="precio diario",
                                     size=5,
                                     clabel="$/día",
                                     alpha=0.3,
                                     cmap=YlGnBu_r,
                                     colorbar=True,
                                     logz=True
                                    )

scatter_datashadeado = datashade(scatter_airbnb, 
                                 aggregator=datashader.reductions.mean("precio diario"),
                                 cmap=YlGnBu_r
                                )

plot_final = tiles_carto_oscuras * scatter_datashadeado
plot_final.opts(responsive=True)

# Convertir en figura de Bokeh:
bokeh_renderer = hv.renderer("bokeh").instance(mode='server')
plot_final_bokeh = bokeh_renderer.get_plot(plot_final).state

# Hacer la figura de bokeh de tamaño responsive:
plot_final_bokeh.sizing_mode="stretch_both"

# Añadir la figura de Bokeh al documento de Bokeh Server:
curdoc().add_root(plot_final_bokeh)

curdoc().title = "Ejemplo Datashader 1"
