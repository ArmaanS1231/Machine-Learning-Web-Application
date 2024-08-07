
<h1>Info</h1>
This program makes a web application machine learning model. The machine learning model is very basic and models a city's predicted heart disease percentage given a city's percentae of smokers and bikers. This is a base of a future web- machine learning project for me.

The model was made using flask: a python web framwork. It is similar to django. Using flask, the application opens a local server on your computer. So, this web-application is only available for personal use hoster on your computer. You can host the server publically by adding host="0.0.0.0" as an argument in the app.run() functio atthe very end of the app.py code. However, make sure debug mode is off in your termninal! Loop up a tutorial or see the Flask library on how to do this. A public server could possible allow other people to change your code so be careful. 


<h1>How to Run</h1>

- Download all files and keep them in one folder. Make sure you don't move any of them. 

- Don't run or change the html as that is not where the web-application is stored. 

- To make run it open up app.pym and simply run that code

- Depending on you code editor ( I use vs code), youshould see a local host server link pull up in your terminal. Click that link or copy and paste it in a browser and the web application should be up!

- Enter a percentage in both slots and click the predict button: the prediction will be under. 

<h1>Bugs/Future</h1>

Because of the simplicity of the machine learningh model, ther are some buggs. Adding a high biking population has very high (lik 90%-100%), will actually lead to a negative percentage. When the percentages start to deviate from a "normal" city's percent, then the predictions are inaccurate. For example no city has a 99$ smoker percentage, so a predicition would be inaccurate. 

Again, I  plan on improving on this aplpication on the future with a worked out financial machine learning program. This porject was just a basis and means of learning flask.
