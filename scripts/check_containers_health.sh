#!/bin/bash

echo "🔎 Verificando estado de saúde dos containers Docker..."
echo "-------------------------------------------------------"

containers=$(docker ps --format "{{.Names}}" )

for container in $containers; do
  health=$(docker inspect --format='{{if .State.Health}}{{.State.Health.Status}}{{else}}no healthcheck{{end}}' "$container")
  if [ "$health" = "healthy" ]; then
    echo "✅ $container está healthy"
  elif [ "$health" = "unhealthy" ]; then
    echo "❌ $container está UNHEALTHY ⚠️"
  elif [ "$health" = "starting" ]; then
    echo "⏳ $container ainda está iniciando..."
  else
    echo "⚠️ $container não tem healthcheck definido"
  fi
done

echo "-------------------------------------------------------"
