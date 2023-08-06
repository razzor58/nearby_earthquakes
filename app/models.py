from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class MaxInputAttemptsExceeded(Exception):
    pass


class Coordinates(BaseModel):
    latitude: Optional[float] = Field(None, ge=-90, le=90)
    longitude: Optional[float] = Field(None, ge=-180, le=180)

    @property
    def point(self):
        return self.latitude, self.longitude

    @classmethod
    def read_from_input(cls):
        coordinates = None
        attempts = 0
        while True:
            try:
                coordinates = cls(
                    latitude=input("Enter latitude [-90:90]: "),
                    longitude=input("Enter longitude [-180:180]:"),
                )
            except ValidationError as exc:
                attempts += 1
                if attempts > 5:
                    raise MaxInputAttemptsExceeded("Too many wrong inputs")
                for err in exc.errors():
                    print("{}: {}".format(err["loc"][0], err["msg"]))
                continue

            else:
                break
        return coordinates
