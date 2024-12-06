from pydantic import BaseModel
from typing import List, Tuple


class MainPage(BaseModel):
    genre: str = None
    netflix_selected: bool = None
    tving_selected: bool = None
    coupang_selected: bool = None
    watcha_selected: bool = None
    wavve_selected: bool = None


class SearchPage(BaseModel):
    searchString: str = None
    netflix_selected: bool = None
    tving_selected: bool = None
    coupang_selected: bool = None
    watcha_selected: bool = None
    wavve_selected: bool = None


class ReturnMovie(BaseModel):
    title: str = None
    titleEn: str = None
    genre: List[str] = None
    age_rating: str = None
    country: List[str] = None
    year: str = None
    running_time: int = None
    description: str = None
    poster_url: str = None
    actor: List[str] = None
    staff: List[str] = None
    ott_provider: List[List[str]] = None
    releases: List[List[str]] = None
