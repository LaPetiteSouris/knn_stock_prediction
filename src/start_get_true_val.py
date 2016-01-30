import sqlite3
import datetime
import fetch_data

conn = sqlite3.connect('database.db')
c = conn.cursor()
today = datetime.date.today()
today_str = today.strftime('%m/%d/%Y')

# Insert a row of data
true_val = fetch_data.get_today_data()
if true_val is not 0:
    c.execute("UPDATE stock SET true=? WHERE date_val=?;",
              (true_val, today_str))

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
