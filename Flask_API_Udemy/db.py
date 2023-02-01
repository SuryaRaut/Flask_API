# Up until now, we've been storing data in an "in-memory database": a couple of Python dictionaries. When we stop 
# the app, the data is destroyed. This is obviously not great, so we want to move to a proper store that can keep 
# data around between app restarts!

# We'll be using a relational database for data storage, and there are many different options: SQLite, MySQL
# , PostgreSQL, and others.

# At this point we have two options regarding how to interact with the database:

# We can write SQL code and execute it ourselves. For example, when we want to add an item to the database we'd 
# write something like INSERT INTO items (name, price, store_id) VALUES ("Chair", 17.99, 1).
# We can use an ORM, which can take Python objects and turn them into database rows.

# we are going to use an ORM because it makes the code much cleaner and simpler. 
# Also, the ORM library (SQLAlchemy) helps us with many potential issues with using SQL, such as:

# Multi-threading support
# Handling creating the tables and defining the rows
# Database migrations (with help of another library, Alembic)
# Like mentioned, it makes the code cleaner, simpler, and shorter

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

