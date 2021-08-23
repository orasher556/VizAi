import pandas as pd

from config import settings
from dal import source_engine, dest_engine
from hash_contents import hash_df_columns


def main():
    for table_config in settings.table_configs:
        source_df = pd.read_sql_table(table_config.table_name, source_engine)
        hash_df_columns(source_df, table_config.hashed_columns)
        source_df.to_sql(table_config.table_name, dest_engine, index=False)


if __name__ == '__main__':
    main()
