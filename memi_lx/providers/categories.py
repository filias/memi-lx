"""Lisbon category providers."""

from memi_engine import CategoryProvider, register
from memi_engine import images

from memi_lx.categories.metro import (
    STATIONS,
    COMMONS_FILES as METRO_FILES,
    LINES as METRO_LINES,
)
from memi_lx.categories.monumentos import (
    MONUMENTS,
    WIKIPEDIA as MONUMENT_WIKI,
    FREGUESIAS as MONUMENT_FREGUESIAS,
)
from memi_lx.categories.freguesias import (
    FREGUESIAS,
    WIKIPEDIA as FREGUESIA_WIKI,
    MAP_FILES as FREGUESIA_MAPS,
)


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

    def get_image(self, item):
        wiki = MONUMENT_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)

    def get_tag(self, item):
        return MONUMENT_FREGUESIAS.get(item)


class FreguesiasProvider(CategoryProvider):
    key = "geografia:freguesias"
    items = FREGUESIAS
    override_name = True

    def get_image(self, item):
        map_file = FREGUESIA_MAPS.get(item)
        if map_file:
            result = images.get_wikipedia_file_image(map_file)
            if result and result.get("image"):
                return result
        wiki = FREGUESIA_WIKI.get(item, item)
        return images.get_wikipedia_image(wiki)


register(MetroProvider())
register(MonumentsProvider())
register(FreguesiasProvider())
