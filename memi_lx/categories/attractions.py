"""Attractions: iconic Lisbon places, buildings, museums, parks and zones.

Includes traditional bairros (Alfama, Chiado, Bairro Alto), historic
squares (Rossio, Restauradores), modern landmarks (MEO Arena, Torre
Vasco da Gama), parks (Monsanto) and museums.
"""

ATTRACTIONS = [
    "Alfama",
    "Bairro Alto",
    "Chiado",
    "Baixa",
    "Santos",
    "Avenida da Liberdade",
    "Rossio",
    "Restauradores",
    "Marquês de Pombal",
    "Praça da Figueira",
    "Largo de Camões",
    "Monsanto",
    "Torre Vasco da Gama",
    "MEO Arena",
    "Fundação Calouste Gulbenkian",
    "Casa Fernando Pessoa",
    "Casa-Museu Dr. Anastácio Gonçalves",
    "Museu da Carris",
]

# Map to English Wikipedia article titles (where the bare name doesn't resolve)
WIKIPEDIA = {
    "Baixa": "Lisbon Baixa",
    "Santos": "Santos-o-Velho, Lisbon",
    "Restauradores": "Restauradores Square",
    "Marquês de Pombal": "Marquis of Pombal Square",
    "Largo de Camões": "Praça Luís de Camões",
    "Monsanto": "Monsanto Forest Park",
    "Torre Vasco da Gama": "Vasco da Gama Tower",
    "Fundação Calouste Gulbenkian": "Calouste Gulbenkian Museum",
    "Museu da Carris": "Carris Museum",
}

# English names, for the game in English (/en/). Neighbourhoods, streets and
# squares English keeps in Portuguese (Alfama, Rossio, Avenida da
# Liberdade…) stay as they are.
EN = {
    "Marquês de Pombal": "Marquis of Pombal Square",
    "Monsanto": "Monsanto Forest Park",
    "Torre Vasco da Gama": "Vasco da Gama Tower",
    "Fundação Calouste Gulbenkian": "Calouste Gulbenkian Foundation",
    "Casa Fernando Pessoa": "Fernando Pessoa House",
    "Casa-Museu Dr. Anastácio Gonçalves": "Anastácio Gonçalves House-Museum",
    "Museu da Carris": "Carris Museum",
}
