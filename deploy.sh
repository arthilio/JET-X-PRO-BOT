#!/bin/bash

# Migration de la base de données
docker-compose exec db psql -U postgres -c "CREATE DATABASE gemdb;"
docker-compose exec bot python -m src.bot.database.migrations upgrade head

# Démarrage des services
docker-compose up -d --scale bot=3

# Surveillance
echo "Surveillance disponible sur :"
echo "- Prometheus: http://localhost:9090"
echo "- Grafana: http://localhost:3000"
