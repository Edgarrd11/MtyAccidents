import pandas as pd
csv_path = "/home/edgarrd11/Portafolio/Shiny/Python/MtyTraffic/data/accidentesMty2023.csv"
collumns = [' Ejercicio',' Mes',' Dia', ' Hora',' Fecha',' Tipo_de_accidente',
            ' Resolución',' Nombre_de_asentamiento',' Nombre_de_la_Vialidad','lng','lat']

renamed_col = {' Ejercicio' : 'Year',' Mes': 'Month',' Fecha': 'Date',' Dia': 'Day', ' Hora': 'Hour',' Tipo_de_accidente': 'Accident_Type',
            ' Resolución': 'Resolution',' Nombre_de_asentamiento': 'Neighborhood',' Nombre_de_la_Vialidad': 'Street'}
# Limpiar la data del csv
def clean_data():
    df = pd.read_csv(csv_path)
    df[['lat','lng']] = df[" Georreferencia"].str.split(', ', expand=True)
    df = df[collumns]
    df.dropna()
    clean_df = df.rename(columns=renamed_col)
    df['Date'] = pd.to_datetime
    return clean_df

# Get coordinates
def get_coord():
    df = clean_data()
    coord = df[['lng','lat']]
    return coord

# Main statement in python
if __name__ == "__main__":
    print(get_coord())

def maps():
    MTY_ACCIDENTS_DATA = get_coord()

    layer = pdk.Layer(
            "HexagonLayer",
            MTY_ACCIDENTS_DATA,
            get_position=["lng", "lat"],
            auto_highlight=True,
            elevation_scale=50,
            pickable=True,
            elevation_range=[0, 3000],
            extruded=True,
            coverage=1
    
    )
    zmm = pdk.ViewState(
            longitude=-100.3161,
            latitude=25.6866,
            zoom=6,
            min_zoom=5,
            max_zoom=40.5,
            bearing= -27.36
    )
    return pdk.Deck(layers=[layer], initial_view_state=zmm)
