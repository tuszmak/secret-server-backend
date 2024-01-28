
<a name="readme-top"></a>


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Build status](https://github.com/tuszmak/secret-server/actions/workflows/node-build.yml/badge.svg?)](https://github.com/tuszmak/secret-server/actions/workflows/node-build.yml)
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/tuszmak/secret-server">
    <img src="images/logo.png" alt="Logo" width="130" height="70">
  </a>

<h3 align="center">Secret Server</h3>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>

  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

Do you have a secret that you don't want to leak? Use this website to store and retrieve your secrets securely! 
This is the backend of a full stack web application.
If you want to see the frontend, visit <a href="https://github.com/tuszmak/secret-server-frontend">this link</a>.
<p align="right">(<a href="#readme-top">Back to top</a>)</p>



### Built With

* ![Python][Python]
* ![Flask][Flask]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Prerequisites

* python 3 (developed and tested on Python 3.10.11)
* PostgreSQL


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/tuszmak/secret-server-backend.git
   ```
2. Create a virtual environment for pip packages
```sh
python -m venv .venv
```
3. Install pip packages
```sh
  \.venv\Scripts\activate
  pip install -r requirements.txt
```
4. Create an empty PostgreSQL database.
5. In your backend/db folder you can find a ".env.template" file. 
<br />
It contains the properties of your database.
Replace that for your own .env file. <br />The structure of the .env is also displayed there.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
1. Start the Flask backend
```sh
\.venv\Scripts\activate
flask --app server run
``` 


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/tuszmak/secret-server.svg?style=for-the-badge
[contributors-url]: https://github.com/tuszmak/secret-server/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/tuszmak/secret-server.svg?style=for-the-badge
[forks-url]: https://github.com/tuszmak/secret-server/network/members
[stars-shield]: https://img.shields.io/github/stars/tuszmak/secret-server.svg?style=for-the-badge
[stars-url]: https://github.com/tuszmak/secret-server/stargazers
[issues-shield]: https://img.shields.io/github/issues/tuszmak/secret-server.svg?style=for-the-badge
[issues-url]: https://github.com/tuszmak/secret-server/issues
[license-shield]: https://img.shields.io/github/license/tuszmak/secret-server.svg?style=for-the-badge
[license-url]: https://github.com/tuszmak/secret-server/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/pinter-daniel/
[product-screenshot]: images/screenshot.jpg
[Python]: https://img.shields.io/badge/Python-3.10-3776AB?style=flat&logo=python&logoColor=white
[Flask]: https://img.shields.io/badge/Flask-web%20framework-000000?style=flat&logo=flask&logoColor=white

