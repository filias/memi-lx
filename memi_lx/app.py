"""Memi Lisboa - pratica a tua memória sobre Lisboa."""

import os

from memi_engine import MemiConfig, create_app

# Import providers to register them
import memi_lx.providers  # noqa: F401

config = MemiConfig(
    title="memi lisboa",
    subtitle="pratica a tua memória",
    favicon_color="#EE1C25",
    sponsor_url="https://github.com/sponsors/filias",
    sponsor_text="apoiar",
    related_sites=[
        {"name": "memi", "url": "https://memi.click"},
        {"name": "memi portugal", "url": "https://pt.memi.click"},
        {"name": "memi slovensko", "url": "https://sk.memi.click"},
        {"name": "memi US", "url": "https://us.memi.click"},
        {"name": "memi Mallorca", "url": "https://ml.memi.click"},
    ],
    label_related_sites="outros jogos memi",
    about_html="""
        <p>Memi Lisboa é um jogo de memória sobre a cidade de Lisboa.</p>
        <p>Escolhe uma categoria, olha para a imagem e tenta adivinhar
        o que é antes de revelar a resposta.</p>
        <p>Estações de metro, monumentos, freguesias — há sempre algo
        novo para descobrir.</p>
    """,
    label_theme="tema",
    label_about="sobre",
    label_report="reportar",
    label_reported="reportado",
    label_clues_on="pistas: sim",
    label_clues_off="pistas: não",
    label_show_letter="mostrar letra",
    label_pick_category="escolhe uma categoria",
    label_loading="a carregar...",
    label_all_done="tudo feito! clica para recomeçar",
    label_click_to_reveal="clica na imagem para revelar a resposta",
    label_click_for_new="clica novamente para outra",
    label_back="voltar a jogar",
)

instance_static = os.path.join(os.path.dirname(__file__), "..", "static")
app = create_app(config, instance_static=instance_static)

if __name__ == "__main__":
    app.run(debug=True, port=8086)
