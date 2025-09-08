FROM python:3.11-slim

# İş qovluğunu təyin et
WORKDIR /app

# Tələb olunan paketləri köçür və quraşdır
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Bütün layihəni konteynerə köçür
COPY . /app/

# Django portunu aç
EXPOSE 8000

# Run komandası
CMD ["gunicorn", "guvenlux.wsgi:application", "--bind", "0.0.0.0:8000"]
