<h1 align="center">Hedge Fund Management System API</h1>

  <p align="left">
    This project aims to solve an organization's issue. Nubia's HedgeFund lacks coordination and centralization of employees and data. She asked me to find a quick yet long term solution to her company's problems. 
    <br />
    <a href="https://github.com/daniellondono777/HedgeFundManagementSystem/tree/main/backend/hfma_app"><strong>Explore the docs ยป</strong></a>
    <br />
    <br />
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

We addressed Nubia's Hedge Fund issues by developing a REST API capable of centralizing data, managing permissions, and some other functional requirements specified by the client.



### Built With

* ๐ Django
* ๐ ๏ธ Django Rest Framework 
* ๐พ SQLite
* ๐ฅฃ BeautifulSoup




<!-- GETTING STARTED -->
## Getting Started

In order to run the project, I advise you to follow the following steps. 

### Prerequisites

This project was developed using Python3.10.4. You can download it from here: https://www.python.org/downloads/

* Once you cloned the repository, on the project's root folder, run:
  ```sh
  pip install -r requirements.txt
  ```

* To start the server, run:
  ```sh
  python manage.py runserver
  ```

* To start the CLI (not necessary), run:
  ```sh
  python clients/client.py
  -username: hatem
  -password: H4t.3m78!
  ```
  Please note these credentials are needed when performing CRUD operations, if you don't want to use them, go to ```setting.py``` and comment the default and authentication classes. Also, there are some models that don't have permissions to be accessed, you can change this in the Django Admin Panel. 



<!-- USAGE EXAMPLES -->
## Usage

You may use the CLI to perform CRUD operations on the API as follows, or simply by requesting using your browser or creating a new client. 

[<img src="https://github.com/daniellondono777/HedgeFundManagementSystem/blob/main/usage.gif" width="300"/>](usage.gif)

Note that you can close the prompt with ```Ctrl+C```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Daniel Londoรฑo - [@LinkedIn](https://www.linkedin.com/in/daniel-londo%C3%B1o-60189a132/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
