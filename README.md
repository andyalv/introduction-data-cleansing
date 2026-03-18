# Introduction Data Cleansing

This repository contains a coursework project for an introductory Data Science class. The project takes the cafeteria customer dataset stored in `src/data/dataset_clientes_cafeteria.csv`, loads it into a normalized PostgreSQL schema, and can export the resulting relational tables back to CSV files.

The codebase currently supports the full workflow for the first stage of the assignment:

1. Initialize the relational database schema.
2. Import the original CSV dataset into normalized PostgreSQL tables.
3. Export the resulting tables back to CSV format.

## What The Project Does

The repository is organized as a small Python ETL-style workflow around PostgreSQL.

- `src/init_database.py` creates the relational schema.
- `src/import_dataset.py` loads the original CSV into a staging table and inserts it into the final tables.
- `src/export_database.py` exports the normalized tables to CSV files.
- `kickstart-python.ipynb` mirrors the script workflow in an interactive notebook so you can inspect each step as it runs.

Supporting code handles configuration, logging, file loading, SQL execution, and shared project paths.

## Current Workflow

The current implementation follows this sequence:

1. Run `src/init_database.py` to create the main tables.
2. Run `src/import_dataset.py` to import `src/data/dataset_clientes_cafeteria.csv`.
3. Run `src/export_database.py` to write exported CSV files under `src/data/export/`.

The export step currently writes one CSV file per normalized table:

- `src/data/export/clientes.csv`
- `src/data/export/visitas_mensuales.csv`
- `src/data/export/compra_restaurante.csv`

## Relational Model

The current schema normalizes the cafeteria dataset into three tables:

- `clientes`: client identity and demographic information.
- `visitas_mensuales`: monthly visit count for each client.
- `compra_restaurante`: purchase amount and payment method for each client.

The import flow uses a temporary staging table before inserting clean values into the final relational tables.

## Project Structure

```text
.
|- .env.example
|- docker-compose.yaml
|- kickstart-python.ipynb
|- notebook-shell.ipynb
|- pyproject.toml
|- README.md
`- src/
   |- config/
   |  |- __init__.py
   |  |- logging.py
   |  `- settings.py
   |- data/
   |  |- dataset_clientes_cafeteria.csv
   |  `- export/
   |     |- clientes.csv
   |     |- compra_restaurante.csv
   |     `- visitas_mensuales.csv
   |- sql/
   |  |- copy_command.sql
   |  |- init.sql
   |  |- insert_imports.sql
   |  `- temp_stage_table.sql
   |- utils/
   |  |- __init__.py
   |  |- files.py
   |  |- render.py
   |  `- sql.py
   |- export_database.py
   |- import_dataset.py
   |- init_database.py
   `- paths.py
```

## Technologies Used

### Core Stack

- `Python 3.14+`
- `PostgreSQL`
- `Docker Compose`
- `Poetry`

### Python Dependencies

Defined in `pyproject.toml`:

- `psycopg2`: PostgreSQL connection support.
- `pydantic-settings`: environment-based settings loading.
- `rich`: formatted logging and terminal rendering.
- `ipykernel`: Jupyter kernel support for `kickstart-python.ipynb` and other notebooks in the repo.

## Environment Variables

Database settings are loaded from `.env`.

Create the file from the example template:

```bash
copy .env.example .env
```

On macOS or Linux:

```bash
cp .env.example .env
```

Expected variables:

- `PGHOST`
- `PGPORT`
- `PGDATABASE`
- `PGUSER`
- `PGPASSWORD`

These values are used both by the Python scripts and by `docker-compose.yaml` for the local PostgreSQL container.

## Setup

Poetry is the primary workflow for this repository.

### 1. Install dependencies

```bash
poetry install
```

### 2. Create the environment file

```bash
copy .env.example .env
```

Then update `.env` with the database values you want to use.

### 3. Start PostgreSQL

```bash
docker compose up -d db
```

## How To Run

### Initialize the database schema

```bash
poetry run python -m src.init_database
```

This reads `src/sql/init.sql` and creates the main relational tables.

### Import the source dataset

```bash
poetry run python -m src.import_dataset
```

This script:

- creates a temporary staging table with `src/sql/temp_stage_table.sql`,
- loads `src/data/dataset_clientes_cafeteria.csv` with `src/sql/copy_command.sql`,
- inserts normalized records into the final tables with `src/sql/insert_imports.sql`.

### Export the normalized tables

```bash
poetry run python -m src.export_database
```

This exports the three main tables to `src/data/export/`.

## Notebook

`kickstart-python.ipynb` is the interactive notebook version of the script workflow. It contains the same logic as `src/init_database.py`, `src/import_dataset.py`, and `src/export_database.py`, but split into notebook cells so you can see what happens step by step while importing and exporting the dataset.

To register the Poetry environment as a notebook kernel:

```bash
poetry run python -m ipykernel install --user --name introduction-data-cleansing --display-name "introduction-data-cleansing"
```

After that, open `kickstart-python.ipynb` in Jupyter or VS Code and select the `introduction-data-cleansing` kernel.

## Verification

Validate the Poetry configuration:

```bash
poetry check
```

Run a Python syntax smoke check:

```bash
poetry run python -m compileall src
```

Run the current workflow manually in order:

```bash
poetry run python -m src.init_database
poetry run python -m src.import_dataset
poetry run python -m src.export_database
```

## Quick Start

If you want the shortest path to run the full current workflow:

```bash
poetry install
copy .env.example .env
docker compose up -d db
poetry run python -m src.init_database
poetry run python -m src.import_dataset
poetry run python -m src.export_database
```

## Running Without Poetry

If you prefer not to use Poetry, you can still run the project with a regular virtual environment and install the dependencies declared in `pyproject.toml`.

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate it

On Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies from `pyproject.toml`

```bash
python -m pip install .
```

### 4. Create the environment file

```bash
copy .env.example .env
```

On macOS or Linux:

```bash
cp .env.example .env
```

### 5. Start PostgreSQL

```bash
docker compose up -d db
```

### 6. Run each script

Initialize the schema:

```bash
python -m src.init_database
```

Import the dataset:

```bash
python -m src.import_dataset
```

Export the normalized tables:

```bash
python -m src.export_database
```
