from adapters import *

# Select the desired Data Adapter Interface

# Custom in-memory "Database" (for development)
adapter = MemoryAdapter()

# MongoDB NoSQL Database
# adapter = MongoDbAdapter("mongodb://localhost:27017/")

# PostgreSQL SQL Database
# adapter = PostgresqlAdapter(dbname='unhcr', user='unhcr', passwd='unhcr')
