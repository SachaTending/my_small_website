set -x
gunicorn main:app --log-level debug -b 0.0.0.0:80