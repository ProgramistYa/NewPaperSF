Учебный проект новостного портала NewsPaper. Работа ведется в процессе выполнения домашнего задания на онлайн-курсе разработчика Python в ScillFacory.
<hr size=10>



pip install django   
django-admin startproject NewsPaper               -создание проекта джанго
python3 manage.py startapp news                   -создание нового приложения
python manage.py createsuperuser                  -создание суперюзера

python manage.py migrate
python manage.py makemigrations
python manage.py runserver

python -m pip install django-filter                          - доп библ
python -m pip install django-allauth                         - python -m А если вы уже находитесь в терминале, то эта приставка не нужна.
                                                             - загрузка библиотеки в виртуальное окружение      ( allauth для авторизации) 
python -m pip install django-filter                          - загузка фильра Джанго
