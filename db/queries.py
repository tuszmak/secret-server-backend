INSERT_QUERY = "INSERT INTO secrets (hash, secretText, createdAt, expiresAt, remainingViews) VALUES (%s, %s, %s, %s, %s);"
GET_QUERY = "SELECT * FROM secrets WHERE hash = %s;"
UPDATE_QUERY = "UPDATE secrets SET remainingViews = %s WHERE hash = %s"
DELETE_QUERY = "DELETE FROM secrets WHERE hash = %s;"