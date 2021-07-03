# A FLOW-BASED MESSENGER CHATBOT PROJECT STRUCTURE USING PYTHON AND FLASK 

This is a simple project structure of a flow-based messenger chatbot using python and flask as a framework.
If you want to use this project structure , you need to have **better understanding how facebook's graph api works.**

## REQUIREMENTS
**A recent version of python interpreter** installed in your computer of course.

Your **Facebook page** linked to your **Facebook App.**

Already **set up your webhooks and granted all necessary permissions** , if not read the [documentation](https://developers.facebook.com/docs/).

Better **understanding how to use messenger's Send API and others API.**


## HOW TO USE ?
1 - Clone this repository

2 - Navigate to the cloned repo

3 - Install the requirements :

```
pip install -r requirements.txt
```

4 - And that's it , you can start using this project now.

5 - To start the local server , use this command :

```
gunicorn --workers 4 --bind localhost:5566 chatbot.wsgi:flask_app
```

You can expose it by using **ngrok** or another similar tool.