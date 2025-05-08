#!/bin/bash
set -e

DB_PATH="../../db.sqlite3"
SQL_FILE="../../migrations/migration_down.sql"

# Sprawdź, czy plik bazy istnieje
if [ ! -f "$DB_PATH" ]; then
  echo "❌ Plik bazy danych nie istnieje: $DB_PATH"
  exit 1
fi

# Sprawdź, czy plik SQL istnieje
if [ ! -f "$SQL_FILE" ]; then
  echo "❌ Plik SQL nie istnieje: $SQL_FILE"
  exit 1
fi

echo "🚨 Usuwanie wszystkich tabel z bazy danych..."

sqlite3 "$DB_PATH" < "$SQL_FILE"

echo "✅ Wszystkie tabele zostały usunięte."
read -p "Press enter to exit..."
