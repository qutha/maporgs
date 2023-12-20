from typing import Annotated, Any

from geopy import Nominatim
from geopy.location import Location

Address = str
Longitude = str
Latitude = str

_geolocator = Nominatim(user_agent="maporgs")


def coords_by_address(
    address: str,
) -> Location | None:
    """
    https://geopy.readthedocs.io/en/stable/index.html#nominatim
    Return type
        None, geopy.location.Location or a list of them, if exactly_one=False.
    """
    location = _geolocator.geocode(address, exactly_one=True, addressdetails=True)
    return _to_location(location)


def extract_location(location: Location) -> tuple[Address, Longitude, Latitude]:
    return location.address, location.longitude, location.latitude


def _to_location(geocode: Annotated[Any, "Location from .geocode"]) -> Location | None:
    if not geocode:
        return None
    return Location(address=geocode.address, point=geocode.point, raw=geocode.raw)
