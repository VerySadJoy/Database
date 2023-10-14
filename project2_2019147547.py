import psycopg
from psycopg import sql
import os
from typing import Union


# problem 1
def entire_search(CONNECTION: str, table_name: str) -> list:
    with psycopg.connect(CONNECTION) as conn:
        with conn.cursor() as cursor:
            c = cursor.execute((""" SELECT * FROM myschema.{} """).format(table_name))
            records = c.fetchall()
            for i in records:
                print(i)
    pass


# problem 2
def search_by_studentID(CONNECTION: str, student_id: str) -> Union[list, None]:
    with psycopg.connect(CONNECTION) as conn:
        with conn.cursor() as cursor:
            c = cursor.execute((""" SELECT A."NAME", A."STUDENT_ID", A."ADMISSION_YEAR", A."GRADE",
	                                    B."MAJOR_NAME", B."COLLEGE_NAME", (A."GRADE" = 0) "GRADUATION"
                                    FROM myschema.students A, myschema.college B 
                                    WHERE A."STUDENT_ID" = CAST({} as CHAR(10)) and A."MAJOR_ID" = B."MAJOR_ID" """).format(student_id))
            records = c.fetchall()
            if (records == []):
                print("“Not Exist student with STUDENT ID : " + student_id + "”")
            else:
                for i in records:
                    print(i)
    pass


# problem 3
def search_by_studentname(CONNECTION: str, student_name: str) -> Union[list, None]:

    pass


# problem 4
def registration_history(CONNECTION: str, student_id: str) -> Union[list, None]:

    pass



# problem 5
def registration(CONNECTION: str, course_id: int, student_id: str) -> Union[list, None]:

    pass


# problem 6
def withdrawal_registration(CONNECTION: str, course_id: int, student_id: str) -> Union[list, None]:

    pass


# problem 7
def modify_lectureroom(CONNECTION: str, course_id: int, buildno: str, roomno: str) -> Union[list, None]:
    
    pass

# sql file execute ( Not Edit )
def execute_sql(CONNECTION, path):
    folder_path = '/'.join(path.split('/')[:-1])
    file = path.split('/')[-1]
    if file in os.listdir(folder_path):
        with psycopg.connect(CONNECTION) as conn:
            conn.execute(open(path, 'r', encoding='utf-8').read())
            conn.commit()
        print("{} EXECUTRED!".format(file))
    else:
        print("{} File Not Exist in {}".format(file, folder_path))