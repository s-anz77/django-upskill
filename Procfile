web: python -m courseswebsite.manage migrate --noinput && python -m courseswebsite.manage collectstatic --noinput && gunicorn courseswebsite.courseswebsite.wsgi:application --bind 0.0.0.0:$PORT
