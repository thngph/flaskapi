# Red Wine ML Flask API introduction

This project is a web application that can predict Wine quality based on its physicochemical properties using machine learning (Random Forest Classifier).

Input is a 1D array of 11 features, the output is 1 if the wine quality is predicted to be good (score from 6.5 to 8), zero is bad (score below 6.5).

Note that this project is for applying machine learning model as a web service/API. As a result of that, the model is not (and don't have to be) really good/optimized.

Data set: [https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009](https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009)

Model training: [https://colab.research.google.com/drive/1ajPS6w2Q3ZSWrodfsm1Smt8CG3hcCE5L?usp=sharing](https://colab.research.google.com/drive/1ajPS6w2Q3ZSWrodfsm1Smt8CG3hcCE5L?usp=sharing)

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| 0            | 0.90      | 0.97   | 0.93     | 273     |
| 1            | 0.67      | 0.38   | 0.49     | 47      |
| accuracy     |           |        | 0.88     | 320     |
| macro avg    | 0.78      | 0.68   | 0.71     | 320     |
| weighted avg | 0.87      | 0.88   | 0.87     | 320     |
# Heroku deployment
Available at [https://x28-flaskapi.herokuapp.com/](https://x28-flaskapi.herokuapp.com/)
