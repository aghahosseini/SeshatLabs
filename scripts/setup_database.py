if __name__  == '__main__':


    import sqlite3

    # ایجاد اتصال به پایگاه داده
    conn = sqlite3.connect('names.sqlite')

    # ایجاد یک کرسر برای اجرای دستورات SQL
    cursor = conn.cursor()

    # ساخت جدول names
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS names (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    ''')

    # افزودن 5 نام به جدول
    names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
    for name in names:
        cursor.execute('INSERT INTO names (name) VALUES (?);', (name,))

    # ذخیره تغییرات و بستن اتصال
    conn.commit()
    conn.close()

    print("Database created and names added successfully!")
