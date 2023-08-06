from typing import Generator

import geopy.distance
import requests

from app.config import settings
from app.models import Coordinates
from app.tools import timing


class Job:
    def __init__(self, input_coordinates: Coordinates) -> None:
        self.start_coordinates: Coordinates = input_coordinates
        self.features: dict = {}
        self.results: dict = {}
        self.processed_point: dict = {}

    def get_data(self) -> None:
        print("\nGetting latest data from external source")
        try:
            response = requests.get(str(settings.API_URL))
            response.raise_for_status()
            data = response.json()
            self.features = data["features"]
        except Exception as e:
            print(f"Error while getting an external data: {e}")

    def point_is_already_processed(self, point: tuple) -> bool:
        point_key = "{}{}".format(point[0], point[1])
        if point_key in self.processed_point:
            return True
        else:
            self.processed_point[point_key] = 1
            return False

    def read_history(self) -> Generator[tuple, None, None]:
        for item in self.features:
            point = item["geometry"]["coordinates"]
            yield (point[1], point[0]), item["properties"]["mag"], item["properties"][
                "place"
            ]

    def process_data(self) -> None:
        print("Processing data")
        for record in self.read_history():
            current_point, mag, place = record

            if self.point_is_already_processed(current_point):
                continue

            raw_distance = geopy.distance.geodesic(
                current_point, self.start_coordinates.point
            )
            distance = round(raw_distance.km, 2)

            self.results[distance] = {"mag": mag, "place": place, "distance": distance}

        sort_keys = sorted([key for key in self.results])

        print("Results:")
        for key in sort_keys[:10]:
            row = self.results[key]
            print("M {:<5} - {:<40} || {:<12}".format(row["mag"], row["place"], key))

    @timing
    def run(self) -> None:
        self.get_data()
        self.process_data()


def exec_job():
    coordinates = Coordinates.read_from_input()
    job = Job(coordinates)
    job.run()
