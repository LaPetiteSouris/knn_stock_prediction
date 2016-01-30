import knn
import sqlite3
import datetime

p = knn.predictor()
tomorrow_prediction = p.predict()

conn = sqlite3.connect('database.db')
c = conn.cursor()
tmr = datetime.date.today() + datetime.timedelta(days=1)
tmr_str = tmr.strftime('%m/%d/%Y')
# Insert a row of data
true_val = 0
c.execute("INSERT INTO stock VALUES (?, ?, ?);",
          (tomorrow_prediction, true_val, tmr_str))

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
