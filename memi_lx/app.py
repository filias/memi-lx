"""Memi Lisboa - practise your memory of Lisbon."""

import os

from memi_engine import MemiConfig, create_app

# Import providers to register them
import memi_lx.providers  # noqa: F401

# The home page opens on the menu, and its empty card shows Lisbon's municipal limits in the city flag above
# "escolhe uma categoria". The engine has no setting for that, so this rides on
# analytics_html (raw HTML at the bottom of every page, after app.js); loading
# a category replaces the card's text, so the map goes with it.
# static/flag-map-lisboa.svg: the boundary from OpenStreetMap (ODbL), the flag from Wikimedia Commons (public domain).
HOME_CARD_HTML = """
<style>
    #status.home { width: 100%; text-align: center; }
    #status .home-map { display: block; max-width: 80%; max-height: calc(min(500px, 90vw) * 0.6); margin: 0 auto 1.5rem; }
</style>
<script>
(function () {
    var status = document.getElementById('status');
    if (status && status.textContent.trim() === 'escolhe uma categoria') {
        status.classList.add('home');
        status.insertAdjacentHTML('afterbegin', '<img class="home-map" src="/static/flag-map-lisboa.svg" alt="Lisboa">');
    }
})();
</script>
"""

config = MemiConfig(
    analytics_html=(
        '<script data-goatcounter="https://memi-lx.goatcounter.com/count"'
        ' async src="//gc.zgo.at/count.js"></script>'
    ) + HOME_CARD_HTML,
    # What the page tells Google and screen readers it is: this game
    # is Portuguese, not the engine's default English.
    html_lang="pt",
    # Details panel beside the card on reveal: the Wikipedia intro (in
    # Portuguese where it exists) and a map.
    layout="enriched",
    title="memi lisboa",
    subtitle="pratica a tua memória",
    favicon_color="#EE1C25",
    sponsor_url="https://github.com/sponsors/filias",
    sponsor_text="apoiar",
    related_sites=[
        {"name": "memi", "url": "https://world.memi.games"},
        {"name": "memi portugal", "url": "https://pt.memi.games"},
        {"name": "memi slovensko", "url": "https://sk.memi.games"},
        {"name": "memi united states", "url": "https://us.memi.games"},
    ],
    label_related_sites="outros jogos memi",
    about_html="""
        <p>Memi Lisboa é um jogo de memória sobre a cidade de Lisboa.
        Estações de metro, monumentos, freguesias &mdash; há sempre algo
        novo para descobrir.</p>

        <h2>Como jogar</h2>
        <p>Escolhe uma categoria, olha para a imagem e tenta adivinhar
        o que é antes de revelar a resposta. Sem contas, sem pontuação,
        sem limite de tempo.</p>
        <p>Na barra inferior tens alguns auxiliares:</p>
        <ul>
            <li><strong>pistas:</strong> ativa pistas progressivas de
            letras &mdash; revela a primeira letra, depois a seguinte, e
            assim por diante. Útil quando o nome está na ponta da
            língua.</li>
            <li><strong>saber mais:</strong> aparece ao revelar e abre o
            artigo da Wikipédia (ou a página da fonte) do item, para que
            possas ler mais.</li>
            <li><strong>reportar:</strong> marca uma carta se a imagem não
            corresponder à resposta (imagem errada, miniatura partida,
            etc.).</li>
        </ul>
        <p>Podes jogar de duas formas:</p>
        <ul>
            <li><strong>Para aprender:</strong> quando não reconheces um
            item, revela a resposta e segue o link <em>saber mais</em>
            para ler sobre ele. Cada exposição reforça a associação entre
            a imagem e o nome.</li>
            <li><strong>Para te testares:</strong> quando uma categoria já
            te é familiar, percorre-a e vê quantas consegues nomear sem
            revelar.</li>
        </ul>

        <h2>Porque funciona</h2>
        <p>Esta é uma forma simples de <em>recordação ativa</em> &mdash;
        recuperar informação da memória em vez de a reler. O <em>efeito
        de teste</em>, bem documentado em psicologia cognitiva, mostra
        que a prática de recuperação cria memórias mais duradouras do que
        a simples re-exposição.</p>
        <p>Como cada estímulo é uma imagem, o jogo aproveita também o
        <em>efeito de superioridade da imagem</em>: as imagens são
        codificadas de forma mais rica do que as palavras e mais fáceis
        de recuperar depois. Nomear o item é uma forma de
        <em>recordação com pista</em>, situada entre o reconhecimento
        simples (&ldquo;já vi isto antes?&rdquo;) e a
        <em>recordação livre</em> sem ajuda.</p>
        <p>Sessões curtas e frequentes funcionam melhor do que sessões
        longas &mdash; o <em>efeito de espaçamento</em>. Alguns minutos
        por dia chegam.</p>
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
    label_more="saber mais",
    label_all="todos",
    label_open_map="abrir mapa",
    label_listen="ouvir",
)

instance_static = os.path.join(os.path.dirname(__file__), "..", "static")
app = create_app(config, instance_static=instance_static)

if __name__ == "__main__":
    app.run(debug=True, port=8086)
