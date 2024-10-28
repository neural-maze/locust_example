DB_FILE = database/chinook.db
SQL_FILE = database/Chinook_Sqlite.sql

all: create-database

create-database: download-sql
	@echo "Creating database $(DB_FILE) using $(SQL_FILE)..."
	sqlite3 $(DB_FILE) < $(SQL_FILE)
	@echo "Database $(DB_FILE) created successfully."

download-sql: 
	@echo "Downloading $(SQL_FILE)..."
	curl -o $(SQL_FILE) https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_Sqlite.sql
	@echo "$(SQL_FILE) downloaded successfully."

clean:
	@echo "Cleaning up database file $(DB_FILE)..."
	rm -f $(DB_FILE)
	@echo "Cleanup complete."

.PHONY: create-database download-sql all clean
