import os

conn_params = {
    "OPENAI_API_KEY": os.environ.get("OPENAI_API_KEY"),
    "account": os.environ.get("SNOWFLAKE_ACCOUNT"),
    "region": os.environ.get("SNOWFLAKE_REGION"),
    "user": os.environ.get("SNOWFLAKE_USER"),
    "password": os.environ.get("SNOWFLAKE_PASSWORD"),
    "database": os.environ.get("SNOWFLAKE_DATABASE"),
    "db_schema": os.environ.get("SNOWFLAKE_DB_SCHEMA")
}
