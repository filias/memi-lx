"""Freguesias (civil parishes) of Lisbon — the 24 parishes after the 2012 reform."""

FREGUESIAS = [
    "Ajuda",
    "Alcântara",
    "Alvalade",
    "Areeiro",
    "Arroios",
    "Avenidas Novas",
    "Beato",
    "Belém",
    "Benfica",
    "Campo de Ourique",
    "Campolide",
    "Carnide",
    "Estrela",
    "Lumiar",
    "Marvila",
    "Misericórdia",
    "Olivais",
    "Parque das Nações",
    "Penha de França",
    "Santa Clara",
    "Santa Maria Maior",
    "Santo António",
    "São Domingos de Benfica",
    "São Vicente",
]

# Map to English Wikipedia article titles
WIKIPEDIA = {
    "Ajuda": "Ajuda (Lisbon)",
    "Alcântara": "Alcântara (Lisbon)",
    "Alvalade": "Alvalade (Lisbon)",
    "Areeiro": "Areeiro (Lisbon)",
    "Arroios": "Arroios (Lisbon)",
    "Avenidas Novas": "Avenidas Novas",
    "Beato": "Beato (Lisbon)",
    "Belém": "Belém (Lisbon)",
    "Benfica": "Benfica (Lisbon)",
    "Campo de Ourique": "Campo de Ourique",
    "Campolide": "Campolide",
    "Carnide": "Carnide (Lisbon)",
    "Estrela": "Estrela (Lisbon)",
    "Lumiar": "Lumiar",
    "Marvila": "Marvila (Lisbon)",
    "Misericórdia": "Misericórdia (Lisbon)",
    "Olivais": "Olivais (Lisbon)",
    "Parque das Nações": "Parque das Nações (Lisbon)",
    "Penha de França": "Penha de França (Lisbon)",
    "Santa Clara": "Santa Clara (Lisbon)",
    "Santa Maria Maior": "Santa Maria Maior (Lisbon)",
    "Santo António": "Santo António (Lisbon)",
    "São Domingos de Benfica": "São Domingos de Benfica",
    "São Vicente": "São Vicente (Lisbon)",
}

# Wikimedia Commons location maps (parish highlighted within Lisbon).
# Fill these with verified file names to show maps instead of article photos.
MAP_FILES: dict[str, str] = {}
