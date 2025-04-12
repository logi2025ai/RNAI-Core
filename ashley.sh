#!/bin/bash

# Ashley CLI - Centro de control RNAI
source ./ashley-engine.sh

echo "
-------------------------------
Ashley AI   -   RNAI-Core CLI
-------------------------------
Comando recibido: $1
"

case "$1" in
  deploy)
    echo "[✓] Iniciando despliegue del sistema..."
    auto_tasks
    ;;

  purge)
    echo "[!] Eliminando bots inactivos..."
    echo "[✓] Purga completada"
    ;;

  sync)
    echo "[✓] Sincronizando Gamma + Convergence..."
    ;;

  help)
    echo "Comandos disponibles:"
    echo " - deploy   → Desplegar sistema"
    echo " - purge    → Eliminar bots inactivos"
    echo " - sync     → Sincronizar flujos"
    echo " - help     → Mostrar esta ayuda"
    ;;

  *)
    echo "[x] Comando no reconocido. Usa 'ashley help' para ver opciones."
    ;;
esac

# Create ashley.sh - Módulo central de Ashley CLI
