import pandas as pd
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine("sqlite:///../db/source_db.db")
    scans_df = pd.read_csv("../data/scans_and_viz_results_de (3).csv", parse_dates=["first_acquired", "patient_first_acquired"])
    scans_df.to_sql("scans_and_viz_results_de", engine, index=False)
    users_df = pd.read_csv("../data/users_de (3).csv")
    users_df.to_sql("users_de", engine, index=False)
    noti_df = pd.read_csv("../data/notifications_de (3).csv", parse_dates=["notification_time"])
    noti_df.to_sql("notifications_de", engine, index=False)
