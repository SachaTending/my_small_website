set -x
gunicorn main:app --log-level debug -t 2348929 -b 0.0.0.0:80
