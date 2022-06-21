# fastapiform

Proyecto de sistema de login con FastAPI y SQLite3 realizado en el canal de [Gregory Vicent Code][gvc].

## Tecnologías usadas:
- **Python**
- **FastAPI**
- **Jinja2**
- **HTML**

## ¿Como correr el proyecto?
**1:** Clonar el repositorio con el comando de git:
```
git clone <dirección del repo>
```
**2:** Ingresar desde la terminal dentro de la carpeta del proyecto. Ejemplo en linux:
```
cd <nombre del directorio>
```
**3:** Crear un entorno virtual:
```
python -m venv venv
```
**4:** Ingresar en el entorno virtual:
- Para linux y Mac:
```
source venv/bin/activate
```
- Para Window:
```
venv\Scripts\activate.bat
```
**5:** Descargar las dependencias del archivo 'requirements.txt' con el comando:
```
pip install -r requirements.txt   
```
**6:** Correr el servidor web de uvicorn:
```
uvicorn <nombre del archivo principal>:<nombre de la instancia de FastAPI> --reload
```
*ejemplo:*
```
uvicorn main:app --reload
```
**7:** En el navegador ir al localhost:8000.

[gvc]:https://www.youtube.com/watch?v=ctTVGqjzBCw
