import settings


def mysql_connection_string():
    return "mysql+pymysql://{username}:{password}@{host}:{port}/{database}?charset=utf8mb4".format(
        username=settings.DB_USERNAME,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_DATABASE
    )
