# Создать шаблон с формой Имя, фамилия, возраст.
# Передать данные на вью,дописать эти данные в файл

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
  return 'welcome %s' % name

@app.route('/write_data',methods = ['POST', 'GET'])
def login():
  if request.method == 'POST':
     user_surname = request.form['surname']
     user_name = request.form['name']
     user_patronymic = request.form['patronymic']
     user_age = request.form['age']
     with open('text.txt','a') as f:
         f.write(f'{user_surname}-{user_name}-{user_age}')
     # return redirect(url_for('success', surname=user_surname, name=user_name, patronymic=user_patronymic, age=user_age))
     return 'Saved'
  else:
     user_surname = request.args.get('surname')
     user_name = request.args.get('name')
     user_patronymic = request.args.get('patronymic')
     user_age = request.args.get('age')
     return redirect(url_for('success',surname=user_surname, name=user_name, patronymic=user_patronymic, age=user_age))




