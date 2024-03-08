# By Edgar Ruiz Dorador
from functools import partial
from matplotlib import pyplot as plt
from shiny import reactive
from shiny.express import input ,ui, render
from shinywidgets import render_pydeck
from shiny.ui import page_navbar
from scripts.dataclean import get_coord
import seaborn as sns
import pydeck as pdk
import pandas as pd


ui.page_opts(
    title="CITMOS",  
    page_fn=partial(page_navbar, id="page"),  
)


with ui.nav_panel("Planteamiento"):
    with ui.div(class_="col-lg-6 py-5 mx-auto"):    
        ui.h2("Análisis de accidentes vehiculares en  Monterrey 2021 - 2023")
        ui.p("por Edgar Ruiz Dorador")
        ui.hr()
        with ui.card():  
            @render_pydeck
            async def map():
                df = get_coord()
                layer = pdk.Layer(
                    "HeatmapLayer",  
                    df,
                    get_position=["lng", "lat"],
                    auto_highlight=True,
                    get_radius=300,         
                    get_fill_color=[255, 0, 0, 1],  
                    pickable=True,
                    
                )

        
                view_state = pdk.ViewState(
                    longitude=-100.3161,
                    latitude=25.6866,
                    zoom=11,
                    min_zoom=5,
                    max_zoom=15,
                    pitch=50,
                    bearing=0,
                )

                return pdk.Deck(layers=[layer], initial_view_state=view_state)
        
        ui.p("Fuente: Datos Abiertos Nuevo León")
        ui.hr()
        ui.markdown(
            """
            ### Planteamiento
            Monterrey es una de las ciudades mas importantes de Mexico,
            con una población de 1.104 millones de habitantes, es sin duda una
            de las ciudades mas grandes de México.

            En este proyecto se busca analizar los accidentes de tránsito que
            ocurren en la ciudad de Monterrey para poder llegar a ciertas inferencias
            y comunicar a las autoridades sobre los factores.

            Tomaremos en cuenta datos recopilados en el periodo 2021-2023.
            
            ***

            ### Objetivo
            El objetivo de este pequeño proyecto es análizar la frecuencia de accidentes de trafico
            que ocurren en la ciudad de Monterrey y llegar a una conclución para
            las siguientes preguntas: 
            
            - ¿Qué tipo de accidente es mas común?
            - ¿En qué día de la semana se registran mas accidentes?
            - ¿Cual es la calle con mas accidentes?
            - ¿Cual es el mes con mas accidentes?
            
            """
    )
    # Habilitar boton de siguiente
    #ui.input_action_button("action_button", "Siguiente")
    @reactive.event(input.action_button)
    def action_button():
        ui.nav_set("Análisis")

with ui.nav_panel("Análisis"):  
    with ui.div(class_="col-lg-6 py-5 mx-auto"):

        ui.h3("Tipo de accidente más común")
        with ui.layout_columns():
            @render.data_frame
            def common_accidents():
                df = pd.read_csv("data/accidentesMty2023_clean.csv")
                word_counts = df["Accident_Type"].value_counts()
                word_counts_df = word_counts.to_frame().reset_index()
                word_counts_df.columns = ['Accident_Type', 'Frequency']
                return render.DataTable(word_counts_df)
        
            @render.plot
            def common_accidents_plot():
                df = pd.read_csv("data/accidentesMty2023_clean.csv")
                word_counts = df["Accident_Type"].value_counts()
                word_counts_df = word_counts.to_frame().reset_index()
                word_counts_df.columns = ['Accident_Type', 'Frequency']
                # Select the top 8 rows
                word_counts_df = word_counts_df.head(8)
                # Plot
                plt.figure(figsize=(8, 8))
                plt.pie(word_counts_df["Frequency"], labels=word_counts_df["Accident_Type"], autopct='%1.1f%%')
                plt.axis('equal') 
                plt.title('Accidentes mas comunes')

        with ui.card():
            ui.markdown(
                """
                ### Choque por alcance, el más común
                Un choque por alcance, también conocido como colisión trasera, es un tipo de accidente de tráfico en el cual un vehículo 
                choca contra la parte trasera de otro vehículo que va delante de él en la misma dirección.\n
                Es importante tomar en cuenta tambien el choque lateral, ya que esta en segundo lugar por una diferencia de 2000 accidentes.
                
                Los factores que pueden causar este tipo de accidentes son:
                - Distancia inadecuada
                - Velocidad inapropiada
                - Distracciones al conducir
                - Fatiga al volante
                - Condiciones climáticas y del camino
                - Fallas mecánicas
                - Conducción agresiva
                - Falta de señalización

                Cabe resaltar que Monterrey tiene la fama de tener una cultura vial muy agresiva, cosa que tiene que tomarse en cuenta a la
                hora de realizar una prueba de hipotesis.

                """
            )

        ui.hr()
        ui.h3("Día de la semana con más accidentes")
        with ui.layout_columns():
            @render.data_frame
            def common_day():
                df = pd.read_csv("data/accidentesMty2023_clean.csv")
                word_counts = df["Day"].value_counts()
                word_counts_df = word_counts.to_frame().reset_index()
                word_counts_df.columns = ['Day', 'Frequency']
                return render.DataTable(word_counts_df)
            
            @render.plot
            def common_days_plot():
                df = pd.read_csv("data/accidentesMty2023_clean.csv")
                word_counts = df["Day"].value_counts()
                word_counts_df = word_counts.to_frame().reset_index()
                word_counts_df.columns = ['Day', 'Frequency']
                # Select the top 8 rows
                word_counts_df = word_counts_df.head(8)
                # Plot
                plt.figure(figsize=(8, 8))
                plt.pie(word_counts_df["Frequency"], labels=word_counts_df["Day"], autopct='%1.1f%%')
                plt.axis('equal') 
                plt.title('Días con más accidentes')


        ui.hr()
        ui.h3("Calle con más accidentes")
        with ui.layout_columns():
            @render.data_frame
            def common_street():
                df = pd.read_csv("data/accidentesMty2023_clean.csv")
                word_counts = df["Street"].value_counts()
                word_counts_df = word_counts.to_frame().reset_index()
                word_counts_df.columns = ['Street', 'Frequency']
                return render.DataTable(word_counts_df)
            
            @render.plot
            def common_streets_plot():
                df = pd.read_csv("data/accidentesMty2023_clean.csv")
                word_counts = df["Street"].value_counts()
                word_counts_df = word_counts.to_frame().reset_index()
                word_counts_df.columns = ['Street', 'Frequency']
                # Select the top 8 rows
                word_counts_df = word_counts_df.head(8)
                # Plot
                plt.figure(figsize=(8, 8))
                plt.pie(word_counts_df["Frequency"], labels=word_counts_df["Street"], autopct='%1.1f%%')
                plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                plt.title('Top 10 Calles con mas accidentes')
        
        ui.hr()
        ui.h3("Mes con más accidentes")
        with ui.layout_columns():
            @render.data_frame
            def common_month():
                df = pd.read_csv("data/accidentesMty2023_clean.csv")
                word_counts = df["Month"].value_counts()
                word_counts_df = word_counts.to_frame().reset_index()
                word_counts_df.columns = ['Month', 'Frequency']
                return render.DataTable(word_counts_df)
            
            @render.plot
            def common_months_plot():
                df = pd.read_csv("data/accidentesMty2023_clean.csv")
                word_counts = df["Month"].value_counts()
                word_counts_df = word_counts.to_frame().reset_index()
                word_counts_df.columns = ['Month', 'Frequency']
                # Plot
                plt.figure(figsize=(8, 8))
                plt.pie(word_counts_df["Frequency"], labels=word_counts_df["Month"], autopct='%1.1f%%')
                plt.axis('equal') 
                plt.title('Meses con más accidentes')



with ui.nav_panel("Conclusión"):  
    ""


