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
  <h3 align="center">SoundSense SERVER</h3>
  <p align="center">
    Raising Awareness of Digital Wellbeing: Data Visualization and Sonification in a Mobile Application
    <br />
    <br />
    <a href="https://github.com/ongaroandrea/SoundSense_Server"><strong>Explore Documentation </strong></a>
    <br />
    <br />
    <a href="https://github.com/ongaroandrea/SoundSense_Server">View Demo</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabella dei contenuti</summary>
  <ol>
    <li>
      <a href="#il-progetto">Project</a>
    </li>
    <li>
      <a href="#realizzato-con">Built with</a>
    </li>
    <li>
      <a href="#per-iniziare">To start</a>
      <ul>
        <li><a href="#prerequisiti">Prerequisities</a></li>
        <li><a href="#api">API</a></li>
      </ul>
    </li>
    <li><a href="#screenshot">Screenshot</a></li>
    <li><a href="#licenza">License</a></li>
    <li><a href="#contatti">Contacts</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Projects


<b>Supervisor</b>:  Dott.ssa Prandi Catia <br />
<b>Co-Supervisor</b>: Dott.ssa Chiara Ceccarini

Technology plays a significant role in most people’s lives, but how can we ensure it enhances our lives rather than distracting us from them?

With today’s smartphones, social media, and endless streams of content, many are quick to condemn technology based on the belief that these products harm mental health and overall wellbeing. However, focusing solely on these potentially harmful effects prevents us from fully harnessing the benefits these tools offer while also managing their risks.

This is where digital wellbeing comes in: a term used to describe the impact of digital technologies and services on individuals’ mental, physical, social, and emotional health.

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
## To start

``` python

pip install -r requirements.txt
python main.py

```
Not compatible with Python 3.10+

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## API

#### / 
* `GET` : Creation of the db and test account

#### /audio/new
* `POST` : Sound generation


#### /audio/all
* `GET` : List of all generations created

#### /audio/:id
* `GET` : Get flac audio

#### /audio/:id
* `DELETE` : Audio removal

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

[license-shield]: https://img.shields.io/github/license/ongaroandrea/SoundSense_Client.svg?style=for-the-badge
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
