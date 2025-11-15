<h1 align="center">
    🤖 MovieBot
</h1>
<h2 align="center">
    🔧 Built Using
    <br></br>
    <p align="center">
        <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
        <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
        <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" />
        <img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" />
        <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
        <img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" />
    </p>
</h2>
Code repository for MovieBot – an NLP-powered movie recommendation chatbot.


## 🖥 Running this locally 
To run this program locally, follow these steps:

1. Download the repo with `git clone https://github.com/Sania555/movie-recommendation-system.git`
2. Create a virtual environment with `python3 -m venv venv`
3. Activate your virtual environment with `source venv/bin/activate`
4. Then, install all the required libraries with `pip install -r requirements.txt`
5. Next, export the Flask app route with `export FLASK_APP=index.py`
6. You will also need to export the Flask environment with `export FLASK_ENV=development`
7. Download the .csv files to the root of the project (the dataset needs to be downloaded from Kaggle)
- https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=credits.csv
- https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=keywords.csv
- https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=movies_metadata.csv
8. Lastly, execute `flask run --port 8000` and your program should be running at `http://127.0.0.1:8000/`


