import sqlite3

def dbform():

    conn = sqlite3.connect('jobs')

    c = conn.cursor()

    try:
        c.execute('''CREATE TABLE jobs(
        id                  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        position_id         varchar(255)                        DEFAULT '',
        position_name       varchar(255)                        DEFAULT '',
        position_lables     varchar(255)                        DEFAULT '',
        work_year           varchar(255)                        DEFAULT '',
        salary              varchar(255)                        DEFAULT NULL,
        city                varchar(255)                        DEFAULT '',
        education           varchar(255)                        DEFAULT '',
        company_name        varchar(255)                        DEFAULT '',
        industry_field      varchar(255)                        DEFAULT '',
        finance_stage       varchar(255)                        DEFAULT '',
        company_size        varchar(255)                        DEFAULT '',
        updated_at          varchar(255)                        DEFAULT '',
        time                varchar(255)                        DEFAULT '',
        platform            varchar(255)                        DEFAULT '',
        avg_salary          float(6,3)                          DEFAULT '0.000'); ''')
    except sqlite3.OperationalError as OperationalError:
        print("sqlite3.OperationalError",end="")
        print(OperationalError)
    finally:
        conn.commit()
        conn.close()