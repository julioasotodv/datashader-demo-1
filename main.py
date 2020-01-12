import os

import numpy as np
import pandas as pd
import hvplot.pandas
import holoviews as hv
from bokeh.io import curdoc
from matplotlib.cm import YlGnBu_r
import geoviews as gv
import cartopy
import datashader

hv.extension("bokeh")

current_dir = os.path.abspath(os.curdir)

existe = os.path.exists(os.path.join(current_dir, "datos_airbnb", "listings.csv.bz2"))


# Data:
datos_airbnb = pd.read_parquet(os.path.join(current_dir, "datos_airbnb", "airbnb_listings.parquet"), 
                           engine="fastparquet"
                          )

"""
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

from holoviews.operation.datashader import rasterize, shade, datashade

scatter_datashadeado = datashade(scatter_airbnb, 
                                 aggregator=datashader.reductions.mean("precio diario"),
                                 cmap=YlGnBu_r
                                )

scatter_datashadeado.opts(responsive=True)

doc = hv.renderer("bokeh").server_doc(tiles_carto_oscuras * scatter_datashadeado)
"""
from bokeh.models.widgets import Paragraph

curdoc().add_root(Paragraph(text=current_dir + str(existe)))

curdoc().title = "Ejemplo Datashader 1"

