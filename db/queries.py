insert_query = "INSERT INTO secrets (link, secret, rem_visits, expiry_date) VALUES (%s, %s, %s, %s);"
getQuery = "SELECT secret FROM secrets WHERE link = %s;"
