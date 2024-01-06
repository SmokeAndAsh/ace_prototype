# map.py
import os
from pathlib import Path

# For debugging
# CURRENT DIRECTORY
print(os.getcwd())

# PROJECT ROOT
# Define base directory
BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

# ROOT PATHS
# Define paths relative to BASE_DIR
CONFIG_DIR = BASE_DIR / 'config'
print(CONFIG_DIR)

DB_DIR = BASE_DIR / 'db'
print(DB_DIR)

SCRIPT_DIR = BASE_DIR / 'script'
print(SCRIPT_DIR)

SRC_DIR = BASE_DIR / 'src'
print(SRC_DIR)

TEST_DIR = BASE_DIR / 'tests'
print(TEST_DIR)

# CONFIGURATION PATHS
# Define paths relative to CONFIG_DIR
DEV_CON_DIR = CONFIG_DIR / 'development'
print(DEV_CON_DIR)

PROD_CON_DIR = CONFIG_DIR / 'production'
print(PROD_CON_DIR)

TEST_CON_DIR = CONFIG_DIR / 'testing'
print(TEST_CON_DIR)

# DATABASE PATHS
# Define paths relative to DB_DIR
MIG_DB_DIR = DB_DIR / 'migrations'
print(MIG_DB_DIR)

SEED_DB_DIR = DB_DIR / 'seeds'
print(SEED_DB_DIR)

# SOURCE PATHS
# Define paths relative to SRC_DIR
API_SRC_DIR = SRC_DIR / 'api'
print(API_SRC_DIR)

APP_SRC_DIR = SRC_DIR / 'app'
print(APP_SRC_DIR)

MODEL_SRC_DIR = SRC_DIR / 'model'
print(MODEL_SRC_DIR)

SRV_SRC_DIR = SRC_DIR / 'services'
print(SRV_SRC_DIR)

# TEST PATHS
# Define paths relative to TEST_DIR
INT_TEST_DIR = TEST_DIR / 'integration'
print(INT_TEST_DIR)

UNIT_TEST_DIR = TEST_DIR / 'unit'
print(UNIT_TEST_DIR)

# COMMON FILES
# Common Configuration Files
CONFIG_FILE = CONFIG_DIR / 'config.py'
print(CONFIG_FILE)

# Common Database Files

# Common Source Files
APP_FILE = APP_SRC_DIR / 'app.py'
print(APP_FILE)

# Common Test Files
DB_TEST_FILE = UNIT_TEST_DIR / 'test_database.py'
print(DB_TEST_FILE)
