# -*- coding: utf-8 -*-
"""Stelt index.html samen: vaste shell + voorstelling uit Word + gegenereerde secties."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

VOORSTELLING = r"""    <section id="voorstelling" class="section section--intro">
      <div class="intro-banner">
        <h1 class="visually-hidden">1 · Voorstelling — Portfolio I-Talent, Jelle Oeyen</h1>
        <img
          class="intro-banner__img"
          src="voorstelling-header.png"
          alt="1 · Voorstelling — Portfolio I-Talent, Jelle Oeyen"
          width="1200"
          height="400"
          loading="eager"
          decoding="async"
        />
      </div>

      <div class="intro-grid intro-grid--mosaic">
        <div class="intro-card intro-card--snippet intro-q1">
          <p>
            Mijn naam is Jelle Oeyen. Mijn interesses liggen vooral bij alles wat met
            computers en technologie te maken heeft, maar daarnaast ben ik ook veel bezig
            met fitness. Op mijn vijfde verjaardag kreeg ik een Nintendo. Vanaf dat
            moment is mijn interesse in games en technologie echt begonnen. Later maakte
            de Nintendo plaats voor een laptop, waarop ik veel tijd doorbracht. Een
            computer fascineerde mij enorm, omdat je er zoveel verschillende dingen mee
            kan doen.
          </p>
        </div>

        <div class="intro-card intro-card--snippet intro-q2">
          <p>
            Tijdens de middelbare school liep niet alles altijd even gemakkelijk, maar
            mijn computer was voor mij steeds een veilige plek waar ik tot rust kon
            komen. Uiteindelijk spendeerde ik er zoveel tijd aan dat het niet meer echt
            gezond was. Daarom besloot ik om naar de fitness te gaan. Ondertussen train
            ik al meer dan drie jaar, vijf dagen per week, om een gezonder persoon te
            worden. Dit toont aan dat ik kan doorzetten en discipline heb. Daarnaast speel
            ik graag competitieve teamgames. Hierdoor heb ik geleerd om beter te
            communiceren en samen te werken met anderen.
          </p>
        </div>

        <div class="intro-card intro-card--snippet intro-q3">
          <p>
            Mijn studietraject is niet altijd even vlot verlopen. Eerst studeerde ik
            Elektronica-ICT aan PXL, maar dat bleek niet helemaal mijn ding te zijn.
            Daarna ben ik Informatica gaan studeren aan UHasselt. Dat was inhoudelijk meer
            wat ik wilde doen, maar het niveau lag voor mij iets te hoog. Uiteindelijk
            kwam ik terecht bij Toegepaste Informatica aan PXL, en vanaf het eerste
            moment voelde ik dat dit de juiste richting voor mij was.
          </p>
        </div>

        <div class="intro-card intro-card--snippet intro-q4">
          <p>
            Er waren momenten waarop het moeilijker was, onder andere omdat mijn ouders
            niet altijd even goed te been zijn en ik thuis soms moet inspringen. Daardoor
            heb ik wel geleerd om verantwoordelijkheid op te nemen en rekening te houden
            met anderen.
          </p>
        </div>

        <div class="intro-card intro-card--snippet intro-q5">
          <p>
            Over enkele jaren wil ik werken in een omgeving waar ik een zelfstandigere
            rol kan opnemen en meer verantwoordelijkheid krijg binnen projecten. Ik wil
            kunnen tonen dat ik goed ben in wat ik doe, dat ik betrouwbaar ben en dat ik
            zelfstandig kwalitatieve oplossingen kan uitwerken. Tegelijk wil ik blijven
            bijleren en mezelf verder ontwikkelen als IT-professional.
          </p>
        </div>

        <div class="intro-card intro-card--snippet intro-q6">
          <p>
            Volgens mijn Thalento-rapport ben ik een meewerkend persoon, en dat komt goed
            overeen met hoe ik mezelf zie. Ik vind het belangrijk om actief mee te denken
            en samen met anderen tot een goede oplossing te komen. Door goed samen te
            werken, kunnen problemen vaak sneller en efficiënter worden opgelost.
          </p>
        </div>

        <div class="intro-card intro-card--snippet intro-q7">
          <p>
            Op dit moment beschik ik vooral over de kennis en vaardigheden die ik tijdens
            mijn opleiding heb opgebouwd. Daarnaast blijf ik actief bijleren, bijvoorbeeld
            tijdens mijn stage. Ik vind het belangrijk om mezelf voortdurend te blijven
            ontwikkelen, omdat IT geen stilstaande sector is. Technologie verandert en
            vernieuwt constant, en daarom moeten wij als IT’ers ook blijven groeien.
          </p>
        </div>

        <figure class="intro-card intro-card--stage">
          <img
            src="stage.jpg"
            alt="Jelle tijdens de stage"
            loading="lazy"
            decoding="async"
          />
          <figcaption>Stage — praktijk buiten de schoolbanken</figcaption>
        </figure>
      </div>

      <p class="scroll-hint">
        <span>Verder naar overzicht &amp; verslag</span>
        <span class="scroll-hint__arrow" aria-hidden="true">↓</span>
      </p>
    </section>
"""

SHELL_TOP = """<!DOCTYPE html>
<html lang="nl">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>I-Talent — Portfolio Jelle Oeyen</title>
    <meta
      name="description"
      content="I-Talent portfolio Jelle Oeyen: voorstelling, activiteitenoverzicht, selectie en eindreflectie."
    />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=Syne:wght@500;600;700;800&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="css/style.css" />
  </head>
  <body>
    <div class="noise" aria-hidden="true"></div>

    <header class="site-header">
      <a class="logo" href="#voorstelling">I-Talent</a>
      <nav class="nav" aria-label="Hoofdnavigatie">
        <a href="#inhoud">Inhoud</a>
        <a href="#voorstelling">Voorstelling</a>
        <a href="#overzicht">Overzicht</a>
        <a href="#selectie">Selectie</a>
        <a href="#eindreflectie">Eindreflectie</a>
      </nav>
    </header>

    <div class="page-wrap">
      <aside class="toc" aria-label="Inhoudsopgave">
        <p class="toc__title">Inhoud</p>
        <ol class="toc__list">
          <li><a href="#voorstelling">1 · Voorstelling</a></li>
          <li>
            <a href="#overzicht">2 · Overzicht activiteiten</a>
            <ul>
              <li><a href="#oz-seminaries">Seminaries</a></li>
              <li><a href="#oz-innovatie">Innovatie</a></li>
              <li><a href="#oz-persoonlijk">Persoonlijke ontwikkeling</a></li>
              <li><a href="#oz-international">Internationalisering</a></li>
            </ul>
          </li>
          <li>
            <a href="#selectie">3 · Selectie (samenvattingen)</a>
            <ul>
              <li><a href="#sel-codebash">Codebash</a></li>
              <li><a href="#sel-duitsland">Studiereis</a></li>
              <li><a href="#sel-vpw">Programmeerwedstrijd</a></li>
            </ul>
          </li>
          <li>
            <a href="#eindreflectie">4 · Eindreflectie</a>
            <ul>
              <li><a href="#xf-passie">(Em)passie</a></li>
              <li><a href="#xf-ondernemen">Ondernemend</a></li>
              <li><a href="#xf-multi">Multidisciplinair</a></li>
              <li><a href="#xf-samen">Samenwerken</a></li>
            </ul>
          </li>
        </ol>
      </aside>

    <main id="inhoud">
"""

SHELL_BOTTOM = """    </main>
    </div>

    <footer class="site-footer">
      <p>
        I-Talent portfolio · Jelle Oeyen · <span data-year></span> ·
        <a href="#voorstelling">Terug naar boven</a>
      </p>
    </footer>

    <script src="js/main.js"></script>
  </body>
</html>
"""


def main() -> None:
    sections = (ROOT / "includes" / "report-sections.html").read_text(encoding="utf-8")
    out = SHELL_TOP + "\n" + VOORSTELLING + "\n" + sections + "\n" + SHELL_BOTTOM
    (ROOT / "index.html").write_text(out, encoding="utf-8")
    print("Wrote index.html")


if __name__ == "__main__":
    main()
