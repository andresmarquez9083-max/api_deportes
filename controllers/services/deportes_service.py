import requests

class DeportesService:

    def obtener_ligas_futbol(self):
        url = "https://www.thesportsdb.com/api/v1/json/3/search_all_leagues.php?s=Soccer"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("Error al consumir la API deportiva")

        return response.json()
