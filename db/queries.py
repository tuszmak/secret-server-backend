insert_query = "INSERT INTO secrets (hash, secretText, createdAt, expiresAt, remainingViews) VALUES (%s, %s, %s, %s, %s);"
getQuery = "SELECT * FROM secrets WHERE hash = %s;"
updateQuery = "UPDATE secrets SET remainingViews = %s WHERE hash = %s"
deleteQuery = "DELETE FROM secrets WHERE hash = %s;"