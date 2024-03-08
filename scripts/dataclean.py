import pandas as pd
csv_path = "/home/edgarrd11/Portafolio/Shiny/Python/MtyAccidents/data/accidentesMty2023.csv"
collumns = [' Ejercicio',' Mes',' Dia', ' Hora',' Fecha',' Tipo_de_accidente',
            ' Resolución',' Nombre_de_asentamiento',' Nombre_de_la_Vialidad','lng','lat']

renamed_col = {' Ejercicio' : 'Year',' Mes': 'Month',' Fecha': 'Date',' Dia': 'Day', ' Hora': 'Hour',' Tipo_de_accidente': 'Accident_Type',
            ' Resolución': 'Resolution',' Nombre_de_asentamiento': 'Neighborhood',' Nombre_de_la_Vialidad': 'Street'}
# Limpiar la data del csv
def clean_data():
    df = pd.read_csv(csv_path)
    df[['lat','lng']] = df[" Georreferencia"].str.split(', ', expand=True)
    df['Date'] = pd.to_datetime
    df = df[collumns]
    clean_df = df.rename(columns=renamed_col)
    clean_df.dropna()
    #clean_df.to_csv('data/accidentesMty2023_clean.csv', index=False)
    return clean_df

# Get coordinates
def get_coord():
    df = pd.read_csv('/home/edgarrd11/Portafolio/Shiny/Python/MtyAccidents/data/accidentesMty2023_clean.csv')
    df = df.dropna()
    df = df[["Accident_Type", "Street","lng","lat"]]
    #coord.to_csv('data/mty_heatmap.csv', index=False)
    return df