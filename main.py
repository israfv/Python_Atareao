import os
from pathlib import Path

def listado_descargas():
    user = os.getlogin()
    path = Path('C:\\Users\\' + str(user) + '\\Downloads')

    print ("Directorio de descargas: " + str(path))

    for p in Path(path).iterdir():
        if not p.is_dir():
            print (p)

listado_descargas()