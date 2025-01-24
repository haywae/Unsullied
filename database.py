from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.getenv('DATABASE_URL')

engine = create_engine(str(db_url), pool_pre_ping=True)

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  result_all = result.all()
  print(result_all)