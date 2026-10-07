"""Modelos Pydantic espejo del schema `collection` del indexer de cosmo-web.

Fuente: packages/database/src/indexer/schema.ts y apps/typesense-import
(espejo indexado en Typesense, colección "collections").
"""

from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


class Objekt(BaseModel):
    """Un objekt (colección COSMO) indexado por el indexer de Apollo."""

    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    id: Optional[str] = None
    contract: Optional[str] = None
    createdAt: Optional[str] = None
    slug: Optional[str] = None
    collectionId: Optional[str] = None
    season: Optional[str] = None
    member: Optional[str] = None
    artist: Optional[str] = None
    collectionNo: Optional[str] = None
    # `class` es palabra reservada en Python -> se expone con alias.
    cls: Optional[str] = Field(default=None, alias="class", serialization_alias="class")
    thumbnailImage: Optional[str] = None
    frontImage: Optional[str] = None
    backImage: Optional[str] = None
    backgroundColor: Optional[str] = None
    textColor: Optional[str] = None
    accentColor: Optional[str] = None
    comoAmount: Optional[int] = None
    onOffline: Optional[Literal["online", "offline"]] = None
    bandImageUrl: Optional[str] = None
    frontMedia: Optional[str] = None
    hasAudio: Optional[bool] = None
    frontImageVersion: Optional[str] = None
    backImageVersion: Optional[str] = None
    description: Optional[str] = None
    shortCode: Optional[str] = None
    edition: Optional[int] = None


class ObjektListResponse(BaseModel):
    """Respuesta paginada, compatible con ObjektResponse<> de cosmo-web."""

    total: int
    hasNext: bool
    nextStartAfter: Optional[int] = None
    objekts: list[Objekt]


class FacetValue(BaseModel):
    value: str
    count: int


class FacetCounts(BaseModel):
    values: list[FacetValue] = []


class SearchFacets(BaseModel):
    artists: list[FacetCounts] = []
    members: list[FacetCounts] = []
    seasons: list[FacetCounts] = []
    classes: list[FacetCounts] = []


class SearchResponse(BaseModel):
    query: str
    page: int
    perPage: int
    result: ObjektListResponse
    facets: SearchFacets = SearchFacets()
