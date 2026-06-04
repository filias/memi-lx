"""Lisbon category providers."""

from memi_engine import CategoryProvider, register
from memi_engine import images

from memi_lx.categories.metro import (
    STATIONS,
    COMMONS_FILES as METRO_FILES,
    LINES as METRO_LINES,
)
from memi_lx.categories.monuments import (
    MONUMENTS,
    WIKIPEDIA as MONUMENT_WIKI,
    PARISHES as MONUMENT_PARISHES,
)
from memi_lx.categories.parishes import PARISHES, MAPS as PARISH_MAPS
from memi_lx.categories.attractions import ATTRACTIONS, WIKIPEDIA as ATTRACTION_WIKI


class MetroProvider(CategoryProvider):
    key = "cultura:metro"
    items = STATIONS
    override_name = True

    def get_image(self, item):
        filename = METRO_FILES.get(item)
        if filename:
            return images.get_commons_file_image(filename)
        return None

    def get_tag(self, item):
        line = METRO_LINES.get(item)
        return f"Linha {line}" if line else None


class MonumentsProvider(CategoryProvider):
    key = "cultura:monumentos"
    items = MONUMENTS
    override_name = True
    # Parish tags are place names, not scientific names — render them plain so
    # single-word parishes (Alvalade, Ajuda…) don't get auto-styled as binomials.
    tag_style = "plain"

    def get_image(self, item):
        wiki = MONUMENT_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return MONUMENT_PARISHES.get(item)


class ParishesProvider(CategoryProvider):
    key = "geografia:freguesias"
    items = PARISHES
    override_name = True

    def get_image(self, item):
        url = PARISH_MAPS.get(item)
        if url:
            return {"name": item, "image": url}
        return None


class AttractionsProvider(CategoryProvider):
    key = "geografia:atracoes"
    items = ATTRACTIONS
    override_name = True

    def get_image(self, item):
        wiki = ATTRACTION_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)


register(MetroProvider())
register(MonumentsProvider())
register(ParishesProvider())
register(AttractionsProvider())
