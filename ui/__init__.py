from api import API

def UI():
    departamento = input("Nombre del departamento: ")
    while(True):
        try:
            lim = int(input("Limite de registros: "))
            if(lim < 1000):
                break
            print("Error (Limite de registros:1000)")
        except ValueError:
            print("Error (solo 'int')")
            
    df = API(lim,departamento.upper())
    df = df[["Estado","Edad", "Tipo", "Ciudad de ubicacion", "Departamento", "Pais de Procedencia",]]
    df['Edad'] = df['Edad'].apply(lambda x: '{:.2f}'.format(x))
    print(df.to_string(index = False))
