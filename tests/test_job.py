from unittest.mock import patch

from app.job import Job
from app.models import Coordinates

MOCK_DATA = [
    {
        "type": "Feature",
        "properties": {
            "mag": 1.3,
            "place": "Kenai Peninsula, Alaska",
            "time": 1691220764942,
            "updated": 1691220905045,
            "tz": None,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ak0239yzzary",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak0239yzzary.geojson",
            "felt": None,
            "cdi": None,
            "mmi": None,
            "alert": None,
            "status": "automatic",
            "tsunami": 0,
            "sig": 26,
            "net": "ak",
            "code": "0239yzzary",
            "ids": ",ak0239yzzary,",
            "sources": ",ak,",
            "types": ",origin,phase-data,",
            "nst": None,
            "dmin": None,
            "rms": 0.51,
            "gap": None,
            "magType": "ml",
            "type": "earthquake",
            "title": "M 1.3 - Kenai Peninsula, Alaska",
        },
        "geometry": {"type": "Point", "coordinates": [-150.731, 59.7516, 40.4]},
        "id": "ak0239yzzary",
    },
    {
        "type": "Feature",
        "properties": {
            "mag": 4.5,
            "place": "38 km ENE of Khandagayty, Russia",
            "time": 1691220144209,
            "updated": 1691221250040,
            "tz": None,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000ky1z",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us6000ky1z.geojson",
            "felt": None,
            "cdi": None,
            "mmi": None,
            "alert": None,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 312,
            "net": "us",
            "code": "6000ky1z",
            "ids": ",us6000ky1z,",
            "sources": ",us,",
            "types": ",origin,phase-data,",
            "nst": 34,
            "dmin": 5.597,
            "rms": 0.43,
            "gap": 67,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 4.5 - 38 km ENE of Khandagayty, Russia",
        },
        "geometry": {"type": "Point", "coordinates": [92.5095, 50.9182, 10]},
        "id": "us6000ky1z",
    },
    {
        "type": "Feature",
        "properties": {
            "mag": 6.2,
            "place": "Santiago Del Estero, Argentina",
            "time": 1691220007272,
            "updated": 1691221429327,
            "tz": None,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000ky1y",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us6000ky1y.geojson",
            "felt": None,
            "cdi": None,
            "mmi": 2.134,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 591,
            "net": "us",
            "code": "6000ky1y",
            "ids": ",us6000ky1y,",
            "sources": ",us,",
            "types": ",ground-failure,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": 111,
            "dmin": 4.29,
            "rms": 0.9,
            "gap": 33,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.2 - Santiago Del Estero, Argentina",
        },
        "geometry": {"type": "Point", "coordinates": [-63.1854, -28.2143, 597.681]},
        "id": "us6000ky1y",
    },
]


def test_process_data():
    coord = Coordinates(latitude=80, longitude=80)
    job = Job(coord)
    job.features = MOCK_DATA
    job.process_data()
    assert len(job.results) > 0


@patch("app.job.requests")
def test_get_data(mock_request):
    mock_request.get.return_value.json.return_value = {"features": MOCK_DATA}
    coord = Coordinates(latitude=80, longitude=80)
    job = Job(coord)
    job.get_data()
    assert len(job.features) > 0
