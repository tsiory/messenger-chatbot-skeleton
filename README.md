# A FLOW-BASED MESSENGER CHATBOT PROJECT STRUCTURE USING PYTHON AND FLASK 

This is a simple project structure of a flow-based messenger chatbot using python and flask as a framework.
If you want to use this project structure , you need to have **better understanding how facebook's graph api works.**

## REQUIREMENTS
- **Python 3.5** installed in your computer of course.

- Your **Facebook page** linked to your **Facebook App.**

- Already **set up your webhooks and granted all necessary permissions** , if not read the [documentation](https://developers.facebook.com/docs/).

- Better **understanding how to use messenger's Send API and others API.**


## HOW TO USE ?
1 - Clone the repository

```bash
git clone git@github.com:krishna2206/messenger-chatbot-skeleton.git 
```

2 - Navigate to the cloned repo

```bash
cd messenger-chatbot-skeleton
```

3 - Install the requirements :

```bash
pip install -r requirements.txt
```

5 - To start the local server , use this command :

```bash
gunicorn --workers 4 --bind localhost:5566 chatbot.wsgi:flask_app
```

You can expose it publicly by using a tool like (**ngrok**)[https://ngrok.com/] or similar tool.
