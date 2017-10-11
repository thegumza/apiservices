__author__ = 'chonnimit'


class DB:
    @staticmethod
    def web_db() -> str:
        server = 'localhost'
        username = 'root'
        database = 'rubber_price'
        password = ''

        return 'mysql+pymysql://{username}:{password}@{server}/{database}?charset=utf8mb4'.format(
            server=server,
            username=username,
            password=password,
            database=database
        )
