import os

import dotenv
from langchain_core.tools import tool
from mysql.connector import connect, Error

from api.monitor import monitor

dotenv.load_dotenv()

def get_db_config():
    config = {
        "host": os.getenv("MYSQL_HOST", "localhost"),
        "port": int(os.getenv("MYSQL_PORT", "3306")),
        "user": os.getenv("MYSQL_USER"),
        "password": os.getenv("MYSQL_PASSWORD"),
        "database": os.getenv("MYSQL_DATABASE"),
        "charset": os.getenv("MYSQL_CHARSET", "utf8mb4"),
        "collation": os.getenv("MYSQL_COLLATION", "utf8mb4_unicode_ci"),
        "autocommit": True,
        "sql_mode": os.getenv("MYSQL_SQL_MODE", "TRADITIONAL")
    }
    #移除值为None的字段
    # config={k:v for k,v in config.items() if v is not None}
    #列出关键字段
    required_keys=["user", "password", "database"]
    #循环遍历找出缺少的关键字段
    missing_keys=[k for k in required_keys if config.get(k) is None]
    # missing_keys=[k for k in required_keys if k not in config]
    #如果有则抛出异常
    if missing_keys:
        raise ValueError(f"缺失数据库核心配置：{', '.join(missing_keys)}")
    #没有缺失则返回
    return config

@tool
def list_sql_tables():
    """
    获取可用表
    :return: 可用表
    """
    monitor.report_tool(tool_name="搜索表名工具")
    try:
        #创建链接对象
        with connect(**get_db_config()) as conn:
            #创建可以执行sql语句的游标对象
            with conn.cursor() as cursor:
                #执行sql语句
                cursor.execute("SHOW TABLES")
                #获取执行结果
                select_result=cursor.fetchall()
                if not select_result:
                    return "没有可用表"
                table_name_list=[iterm[0] for iterm in select_result]
                return f"可用表:{",".join(table_name_list)}"
    except Error as e:
        return "数据库连接失败: " + str(e)

@tool
def get_table_data(table_name):
    """
    读取指定表的前100行数据，用于快速预览数据内容。
    :param table_name: 要查询的表名
    :return: 返回查询出来的数据
    """
    monitor.report_tool(tool_name="搜索指定表名的数据工具", args={"table_name": table_name})
    try:
        with connect(**get_db_config()) as conn:
            with conn.cursor() as cursor:
                sql=f"select * from {table_name} limit 100"
                cursor.execute(sql)
                #获取表头（所有字段）
                description=cursor.description#[('drug_id', 3, None, None, None, None, 0, 49667, 63), ('generic_name', 253, None, None, None, None, 0, 4097, 224)]
                table_header_str=",".join([header[0] for header in description])
                if not description:
                    return f"当前表{table_name}没有数据"
                result_list=cursor.fetchall()
                data_list=[",".join(map(str,row_tuple)) for row_tuple in result_list]
                data_list_str="\n".join(data_list)
                return table_header_str + "\n" + data_list_str
    except Error as e:
        return "数据库连接失败: " + str(e)

@tool
def execute_sql_query(sql: str) -> str:

    """
    执行自定义SQL查询
    :param sql: 自定义SQL查询语句
    :return: 查询数据 表格形式
    """
    monitor.report_tool(tool_name="执行自定义SQL查询工具", args={"sql": sql})
    try:
        with connect(**get_db_config()) as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                # 获取结果 [1.判断有没有数据 2. 获取表头  3. 获取表数据]
                # description获取表的元数据 (表头)  1. 判断是不是有效表或者有数据  2. 获取表头信息
                # [
                #   (id , 第一列的描述 , ....) ,
                #   (name , 第一列的描述 , ....)
                # ]
                description = cursor.description
                if  not description:
                    return f"当前语句{sql}没有数据"
                table_header = [column_tuple[0] for column_tuple in description]
                # [(1,name,18),(),()]
                result = cursor.fetchall()
                # (1,name,18) -> "1,name,18"
                # [(1,name,18),(),()] -> ["1,name,18","2,hehe,20"]
                data_list = [ ",".join(map(str ,row_tuple)) for row_tuple in result]
                # id,name,age
                table_header_str = ",".join(table_header)
                # "1,name,18"\n"2,hehe,20\n
                data_list_str = "\n".join(data_list)
                return table_header_str + "\n" + data_list_str
    except Error as e:
        return "数据库连接失败: " + str(e)

if __name__ == "__main__":
    # print(get_db_config())
    #print(list_sql_tables())
    print(get_table_data("drugs"))