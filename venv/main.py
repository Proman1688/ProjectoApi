from ui import UI

def principal():
    while(True):
        UI()
        print("¿Volver a hacer otra consulta?(s/n): ")
        if(input() != 's'):
            break

if __name__ == '__main__':
    principal()