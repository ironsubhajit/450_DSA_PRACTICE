import pandas as pd
import pymysql.cursors
from pathlib import Path


# Getting file from project folder
file_path = Path(Path(__file__).parent, "AlokAbc.xlsx")

# Creating dataframes from sheets
data_frame = pd.read_excel(file_path, sheet_name=['Sheet1', 'Sheet2', 'Sheet3'])


def create_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='@Subha2000',
        database='alokdb',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection


def xls_to_mysqldb():
    try:
        # Creating Mysql DataBase connection
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                for sheet in data_frame.keys():
                    # create table name from sheet name
                    table_name = 'table_' + sheet

                    # get each sheet data as dataframe
                    df = data_frame[sheet]
                    # print(f"\nDataframe: {df}")

                    # Loop over each row in the Dataframe
                    for row in range(len(df)):
                        col_vals = []
                        for col in range(len(df.columns)):
                            # getting each column value
                            col_vals.append(df.iloc[row, col])

                        # assume all table has 3 col and generate query
                        insert_query = f"INSERT INTO {table_name} VALUES (%s, %s, %s)"
                        print(f"\nTable: {table_name} Query: {insert_query}")
                        cursor.execute(insert_query, (col_vals[0], col_vals[1], col_vals[2]))
                        connection.commit()
                print("\ndata insert complete.")

    except Exception as err:
        print(f"\nCreation Error: {err}")


def fetch_all_data():
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                for sheet in data_frame.keys():
                    select_query = f"SELECT * FROM table_{sheet}"
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    print(f"\nData Fetched from table_{sheet}\n")
                    print(result)
    except Exception as err:
        print(f"\nFetch Error: {err}")


def erase_data_from_table():
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM table_sheet1")
                connection.commit()
                cursor.execute("DELETE FROM table_sheet2")
                connection.commit()
                cursor.execute("DELETE FROM table_sheet3")
                connection.commit()
    except Exception as err:
        print(f"\nDeletion Error: {err}")


xls_to_mysqldb()
fetch_all_data()
erase_data_from_table()