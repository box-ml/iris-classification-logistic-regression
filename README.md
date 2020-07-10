# Logistic Regression models in Box.ml
[Box.ml](https://box.ml/login) is the easiest and fastest way to put machine learning models in the hands of your users. It takes a simple drag and drop and your model is ready-to-use; In a matter of seconds you can call your model from anywhere including Excel, blogs and apps.

In this short tutorial, your are going to train a [Logistic Regression](https://en.wikipedia.org/wiki/Logistic_regression) model using the classic [Iris Dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set). After dropping it in box.ml, the tutorial walks you through the simple steps to start using it.

You will use the popular [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) libray to train the Machine learning model that you will need to complete this tutorial.

# Setup
Please, feel free to skip the steps that you don't need.
```
brew install python3
pip3 install virtualenv
```

Create a local copy of this git repository in your computer:
```
git clone https://github.com/box-ml/iris-classification-logistic-regression.git
cd iris-classification-logistic-regression
```

Create a virtual environment and activate it:
```
virtualenv -p python3 venv
source venv/bin/activate
```

Install scikit-learn and other necessary packages:
```
pip install -r requirements.txt
```

# Train
To train the Machine Learning model just execute the following line:
```
python train.py
```

The trained model will be exported to the file: *iris_logistic_regression.pkl*

# Box.ml
In order to make your model available from anywhere: 1) login into [box.ml](https://box.ml/login), 2) select or create a new Deployment, 3) drag and drop the file *iris_logistic_regression.pkl* in the box, like shown in the image below. 

![Box.ml drop model box](img/drop.png)

Your model will be ready-to-use in a second.

![Box.ml predicting](img/predict.png)

You can click the Predict button in the Test tab, and the result of the prediction will be shown next to the last variable value.

You can change the name of the variables in the table. You can set the names of your choice, but the order must match the order of the columns of the training dataset.



For the [Iris Dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set) you could set the variables and test your trained model as follow: 

| Sepal Length | Sepal Width | Petal Length | Petal Width |     |
| ------------ | ----------- | ------------ | ----------- | --- |
| 1.0          | 1.0         | 1.0          | 1.0         | [0] |
| 6.0          | 2.0         | 4.0          | 1.0         | [1] |
| 4.0          | 4.0         | 2.0          | 6.0         | [2] |

* [0] Corresponds to Iris-setosa class
* [1] Corresponds to Iris-versicolor class
* [2] Corresponds to Iris-virginica class

## Code snippets
![Box.ml predicting](img/code.png)

The code snippet provided in the *cURL* and *Python* tabs are ready-to-use. You can copy and test it from your terminal. You should see the predictions coming from your model that is now live in [box.ml](https://box.ml).

You can use the code in the HTML tab to show a prediction box in your website or blog like shown in the image below. Your readers will be able to enter the values and make predictions by themselves.

![Box.ml predicting widget](img/blog.png)

Lastly, from the Excel tab, you can download an Excel file that is ready-to-use as well. You can distribute the Excel file among your users, and they will be able to predict with your model.

![Box.ml predicting from Excel](img/excel.png)

# How it works
Every time you drop a trained model in [box.ml](https://box.ml/login) you receive:  
- A Unique Identifier for your model
- A Client Id and a Client Secret

With these three things you can call your model from anywhere. 

# Security
Technically speaking, your model is made available via a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer), a very standard and secure practice.

The combination of the model's Unique Identifier, the Client Id and the Client Secret provide enough security to keep the use of your models safe of intruders.

You will have to share the model's Unique Identifier among your users but as a good practice, create a different Client Id and Client Secret for each one.
