<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ongaroandrea/SoundSense">
    <img src="https://github.com/ongaroandrea/SoundSense_Client/SoundSense/Image/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">SoundSense SERVER</h3>
  <p align="center">
    Aumentare la consapevolezza sul benessere digitale: Data Visualization e Sonification in un’applicazione mobile
    <br />
    <br />
    <a href="https://github.com/ongaroandrea/SoundSense_Server"><strong>Esplora la documentazione »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ongaroandrea/SoundSense_Server">Visualizza Demo</a>
    ·
    <a href="https://github.com/ongaroandrea/SoundSense_Server/issues">Reporta un Bug</a>
    ·
    <a href="https://github.com/ongaroandrea/SoundSense_Server/issues">Richiedi una funzionalità</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabella dei contenuti</summary>
  <ol>
    <li>
      <a href="#il-progetto">Il Progetto</a>
    </li>
    <li>
      <a href="#realizzato-con">Realizzato con</a>
    </li>
    <li>
      <a href="#per-iniziare">Per iniziare</a>
      <ul>
        <li><a href="#prerequisiti">Prerequisiti</a></li>
        <li><a href="#api">API</a></li>
      </ul>
    </li>
    <li><a href="#screenshot">Screenshot</a></li>
    <li><a href="#licenza">Licenza</a></li>
    <li><a href="#contatti">Contatti</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Il Progetto


<b>Relatore</b>:  Dott.ssa Prandi Catia <br />
<b>Correlatore</b>: Dott.ssa Chiara Ceccarini

Aumentare la consapevolezza sul benessere digitale: Data Visualization e Sonification in un’applicazione mobile

La tecnologia gioca un ruolo importante nella vita della maggior parte delle persone, ma come possiamo assicurarci che migliori effettivamente la vita piuttosto che distrarci da essa?
Con gli smartphone di oggi, i social media e i flussi infiniti di contenuti, molte persone sono pronte a condannare la tecnologia sulla base della loro convinzione che questi prodotti siano dannosi per la salute mentale e il benessere. Ma concentrarsi solo su questi effetti potenzialmente dannosi non ci aiuta a raccogliere tutti i vantaggi che questi strumenti hanno da offrire, gestendo anche i loro rischi. Da qui nasce il digital wellbeing: un termine utilizzato per descrivere l’impatto delle tecnologie e dei servizi digitali sulla salute mentale, fisica, sociale ed emotiva delle persone.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python 3.9]
* [![flask][flask]][Flask]
* [![midiutil][midiutil]][midiutil]
* [![music21][music21]][music21]
* [![audiolazy][audiolazy]][audiolazy]
* [![numpy][numpy]][numpy]
* [![SQLAlchemy][SQLAlchemy]][SQLAlchemy]
* [![midi2audio][midi2audio]][flask_marshmallow]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Per iniziare

``` python

pip install -r requirements.txt
python main.py

```
NON COMPATIBILE CON Python 3.10+

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## API

#### / 
* `GET` : Creazione Database e Account test

#### /audio/new
* `POST` : Generazione Audio


#### /audio/all
* `GET` : Lista con tutte le informazioni delle sonificazioni

#### /audio/:id
* `GET` : Ottenimento audio flac

#### /audio/:id
* `DELETE` : Rimozione audio

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## Licenza

Distribuito con licenza MIT. Vedere `LICENSE.txt` per ulteriori informazioni.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contatti

Andrea Ongaro  - andreaongaro103@yahoo.it | andrea.ongaro2@studio.unibo.it

Project Link: [https://github.com/ongaroandrea/SoundSense_Server](https://github.com/ongaroandrea/SoundSense_Server)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/ongaroandrea/SoundSense_Server/contributors

[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/ongaroandrea/SoundSense_Server/members

[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/ongaroandrea/SoundSense_Server/stargazers

[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/ongaroandrea/SoundSense_Server/issues

[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/ongaroandrea/SoundSense_Server/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/ongaro-andrea/

[product-screenshot]: images/screenshot.png

[Python]: https://www.python.org/
[Flask]: https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/
[midiutil]: https://github.com/MarkCWirt/MIDIUtil
[music21]: http://web.mit.edu/music21/
[audiolazy]: https://github.com/danilobellini/audiolazy
[numpy]: https://numpy.org/
[SQLAlchemy]: https://www.sqlalchemy.org/
[flask_marshmallow]: https://flask-marshmallow.readthedocs.io/en/latest/
[FuildSynth]: https://www.fluidsynth.org/