<h1 align="center">✒️ Welcome to deploy-proust 
🤖</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/kefranabg/readme-md-generator#readme" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/kefranabg/readme-md-generator/graphs/commit-activity" target="_blank">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" />
  </a>
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/github/license/HarryPommier/proust-generator" />
  </a>
</p>

> API for Text generation by AI in the style of Marcel Proust.

## Usage

##### Configure Python Virtual Environnement 

```sh
virtualenv venv --python=/path/to/python3
```
(You can use the command "which python3" to find your Python path)

##### Activate Environnement

```sh
source /venv/bin/activate
```

##### Install Requirements 

```sh
pip install -r requirements.txt
```

##### Launch App 

```sh
uvicorn main:app --reloads
```

Request /predict endpoint with a POST method and a JSON payload:
```json
{
  "data": "Longtemps je ne suis couché tard,"
}
```

Response:
```json
{
  "data": "A ce jour, là comme la première fois chez nous dans sa bouche en retard pour la même façon que les autres hommes « bon moment."
}
```




## Author

👤 **Harry Pommier**

* Website: https://nantes.zenika.com/
* Github: [@HarryPommier](https://github.com/HarryPommier)
* LinkedIn: [@harry-pommier-phd-a3911145](https://linkedin.com/in/harry-pommier-phd-a3911145)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/HarryPommier/deploy-proust/issues). 

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
