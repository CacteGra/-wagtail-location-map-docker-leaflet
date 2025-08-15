FILE=manage.production.py
if test -f "$FILE"; then
echo 'Start removed manage added prod'
rm manage.py && mv manage.production.py manage.py
rm mysite/wsgi.py && mv mysite/wsgi.production.py mysite/wsgi.py
fi
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn mysite.wsgi:application
