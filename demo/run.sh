#/bin/sh
# Script for docker container to run the routine

cd /app
echo "Running Genshin Impact Daily Check-in Bot..."
.env/bin/python src/main.py
