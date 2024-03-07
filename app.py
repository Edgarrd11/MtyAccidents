# By Edgar Ruiz Dorador
from functools import partial
import pandas as pd
from shiny import reactive
from shiny.express import input ,ui
from shinywidgets import render_pydeck
from shiny.ui import page_navbar
from scripts.dataclean import get_coord
import pydeck as pdk
import seaborn as sns

ui.page_opts(
    title="CITMOS",  
    page_fn=partial(page_navbar, id="page"),  
)


with ui.nav_panel("Planteamiento"):  
    with ui.div(class_="col-lg-6 py-5 mx-auto"):    
        ui.h2("Análisis de accidentes vehiculares en  Monterrey 2021 - 2023")
        ui.p("por Edgar Ruiz Dorador")
        @render_pydeck
        def map():
            df = pd.read_csv('/home/edgarrd11/Portafolio/Shiny/Python/MtyAccidents/data/accidentesMty2023_clean.csv')
            df = df.dropna()
            df = df[["Accident_Type", "Street","lng","lat"]]
            
            print(df)
            
            
            layer = pdk.Layer(
                "HeatmapLayer",  # `type` positional argument is here
                df,
                get_position=["lng", "lat"],
                auto_highlight=True,
                get_radius=300,          # Radius is given in meters
                get_fill_color=[255, 0, 0, 1],  # Set an RGBA value for fill
                pickable=True
            )

            # Set the viewport location
            view_state = pdk.ViewState(
                longitude=-100.3161,
                latitude=25.6866,
                zoom=11,
                min_zoom=5,
                max_zoom=15,
                pitch=50,
                bearing=0,
            )

            # Combined all of it and render a viewport
            return pdk.Deck(layers=[layer], initial_view_state=view_state)
        ui.p("Heatmap de accidentes en Monterrey, fuente: Datos Abiertos Nuevo León")
        
        ui.markdown(
            """
            ### Planteamiento
            Monterrey es una de las ciudades mas importantes de Mexico,
            con una población de 1.104 millones de habitantes, es sin duda una
            de las ciudades mas grandes de México.

            En este proyecto se busca analizar los accidentes de tránsito que
            ocurren en la ciudad de Monterrey para poder llegar a ciertas inferencias
            y comunicar al gobierno que se puede proponer como solución.

            Tomaremos en cuenta datos recopilados en el periodo 2021-2023.

            ### Objetivo
            El objetivo de este proyecto es analizar los accidentes de tránsito
            que ocurren en la ciudad de Monterrey y llegar a una conclución para
            las siguientes preguntas: 
            
            - ¿Qué tipo de accidente es mas común?
            - ¿En qué día de la semana se registran mas accidentes?
            - ¿Cual es la calle con mas accidentes?
            - ¿Cual es el mes con mas accidentes?
            
            """
    )
    

with ui.nav_panel("Análisis"):  
    with ui.div(class_="col-lg-6 py-5 mx-auto"):
        ui.h3("Tipo de accidente mas común")
        

with ui.nav_panel("Conclución"):  
    ""


