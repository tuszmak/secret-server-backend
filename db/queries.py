insert_query = "INSERT INTO secrets (hash, secret_text, created_at, expires_at, remaining_views) VALUES (%s, %s, %s, %s, %s);"
getQuery = "SELECT * FROM secrets WHERE hash = %s;"
updateQuery = "UPDATE secrets SET remaining_views = %s WHERE hash = %s"
deleteQuery = "DELETE secret FROM secrets WHERE hash = %s;"