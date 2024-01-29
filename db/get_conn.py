import psycopg2
# This function only exists to reduce code duplication.

def get_conn(env_variables : dict):
    """Create connection with PostgreSQL"""
    conn = psycopg2.connect(
              host=env_variables.get('DB_HOST'),
              database=env_variables.get('DB_NAME'),
              user=env_variables.get('DB_USERNAME'),
              password=env_variables.get('DB_PASSWORD'),
              port=env_variables.get("DB_PORT")
              )
    return conn