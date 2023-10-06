from sodapy import Socrata
import pandas as pd


def API(num_registros,departamento):
    client = Socrata("www.datos.gov.co", None)
    results = client.get("gt2j-8ykr", limit = num_registros, departamento_nom = departamento)
    df = pd.DataFrame.from_records(results)
    data = {"Ciudad de ubicacion":[], "Departamento":[], "Edad":[], "Tipo":[], "Estado":[], "Pais de Procedencia":[]}
    for MiniDatos in results:
        data['Ciudad de ubicacion'].append(MiniDatos['ciudad_municipio_nom'])
        data['Departamento'].append(MiniDatos['departamento_nom'])
        data['Edad'].append(MiniDatos['edad'])
        data['Tipo'].append(MiniDatos['fuente_tipo_contagio'])
        data['Estado'].append(MiniDatos['estado'])
        if ("pais_viajo_1_nom" in MiniDatos):
            data['Pais de Procedencia'].append(MiniDatos['pais_viajo_1_nom'])
        else:
            data['Pais de Procedencia'].append("")

    df = pd.DataFrame.from_records(data)
    return df