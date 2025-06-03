#!/bin/bash
set -e

DB_PATH="../../db.sqlite3"
SQL_DIR="../../migrations"

for file in $(ls $SQL_DIR/*.sql | sort); do
  # Pomijaj migration_down.sql
  if [[ "$file" == *"migration_down.sql" ]]; then
    continue
  fi

  echo "▶ Executing $file..."
  sqlite3 "$DB_PATH" < "$file"
  sleep 3
done

echo "✅ All migrations applied."
read -p "Press enter to exit..."