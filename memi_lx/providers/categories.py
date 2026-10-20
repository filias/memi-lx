"""Lisbon category providers."""

from memi_engine import CategoryProvider, register
from memi_engine import images

from memi_lx.categories.metro import (
    EN as METRO_EN,
    STATIONS,
    COMMONS_FILES as METRO_FILES,
    LINES as METRO_LINES,
    WIKIPEDIA as METRO_WIKI,
)
from memi_lx.categories.monuments import (
    EN as MONUMENT_EN,
    MONUMENTS,
    WIKIPEDIA as MONUMENT_WIKI,
    PARISHES as MONUMENT_PARISHES,
)
from memi_lx.categories.parishes import (
    PARISHES,
    MAPS as PARISH_MAPS,
    WIKIPEDIA as PARISH_WIKI,
)
from memi_lx.categories.attractions import (
    ATTRACTIONS,
    EN as ATTRACTION_EN,
    WIKIPEDIA as ATTRACTION_WIKI,
)

# Greater Lisbon. Wikidata coordinates outside it belong to something other
# than the place on the card, so they get no map.
LISBON_BOUNDS = ((38.6, 38.85), (-9.5, -9.0))


class MetroProvider(CategoryProvider):
    key = "cultura:metro"
    items = STATIONS
    override_name = True
    translations = {"en": METRO_EN}
    map_zoom = 16
    map_bounds = LISBON_BOUNDS

    def get_image(self, item):
        filename = METRO_FILES.get(item)
        if filename:
            return images.get_commons_file_image(filename)
        return None

    def get_tag(self, item):
        line = METRO_LINES.get(item)
        return f"Linha {line}" if line else None

    def get_wikipedia_title(self, item):
        # The card is a Commons photo; the panel describes the station.
        title = METRO_WIKI.get(item)
        return ("pt", title) if title else None


class MonumentsProvider(CategoryProvider):
    key = "cultura:monumentos"
    items = MONUMENTS
    override_name = True
    translations = {"en": MONUMENT_EN}
    map_zoom = 16
    map_bounds = LISBON_BOUNDS
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
    map_zoom = 14
    map_bounds = LISBON_BOUNDS

    def get_image(self, item):
        url = PARISH_MAPS.get(item)
        if url:
            return {"name": item, "image": url}
        return None

    def get_wikipedia_title(self, item):
        # The card is a locator map with no article link.
        title = PARISH_WIKI.get(item)
        return ("pt", title) if title else None


class AttractionsProvider(CategoryProvider):
    key = "geografia:atracoes"
    items = ATTRACTIONS
    override_name = True
    translations = {"en": ATTRACTION_EN}
    map_zoom = 16
    map_bounds = LISBON_BOUNDS

    def get_image(self, item):
        wiki = ATTRACTION_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)


register(MetroProvider())
register(MonumentsProvider())
register(ParishesProvider())
register(AttractionsProvider())
