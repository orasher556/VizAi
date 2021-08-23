from sqlalchemy import create_engine

from config import settings

source_engine = create_engine(settings.source_db_cs)
dest_engine = create_engine(settings.dest_db_cs)
