# Создать сайт. При запросе на домашнюю страницу отображается текущая дата.

from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route('/')
def date_now():
    time_today = datetime.today()
    date = str(time_today.date())
    return date

if __name__ == '__main__':
   app.run()

