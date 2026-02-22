import sqlite3
from datetime import datetime

DB_NAME = "pos_database.db"

def inspect_database():
    print(f"--- 🔍 INSPECCIÓN DE BASE DE DATOS: {DB_NAME} ---")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        
        print("\n[1] Estructura de la tabla 'expenses':")
        cursor.execute("PRAGMA table_info(expenses)")
        for col in cursor.fetchall():
            print(f"Columna: {col[1]} | Tipo: {col[2]}")
            
        print("\n[1] Estructura de la tabla 'products':")
        cursor.execute("PRAGMA table_info(products)")
        for col in cursor.fetchall():
            print(f"Columna: {col[1]} | Tipo: {col[2]}")
        
        print("\n[1] Estructura de la tabla 'users':")
        cursor.execute("PRAGMA table_info(users)")
        for col in cursor.fetchall():
            print(f"Columna: {col[1]} | Tipo: {col[2]}")
        
        # 1. Ver estructura de la tabla sales
        print("\n[1] Estructura de la tabla 'sales':")
        cursor.execute("PRAGMA table_info(sales)")
        for col in cursor.fetchall():
            print(f"Columna: {col[1]} | Tipo: {col[2]}")

        # 2. Ver las últimas 5 ventas para chequear datos y fechas
        print("\n[2] Últimas 5 ventas registradas:")
        cursor.execute("SELECT * FROM sales ORDER BY id DESC LIMIT 5")
        rows = cursor.fetchall()
        if not rows:
            print("⚠️ ¡La tabla 'sales' está VACÍA!")
        else:
            for row in rows:
                print(row)

        # 3. Probar el filtro de fecha que usa el servidor
        today = datetime.now().strftime('%Y-%m-%d')
        print(f"\n[3] Buscando ventas con fecha de hoy ({today}):")
        cursor.execute("SELECT COUNT(*) FROM sales WHERE date(date) = ?", (today,))
        count_today = cursor.fetchone()[0]
        print(f"Ventas encontradas para hoy: {count_today}")

        # 4. Ver rango de fechas existente
        print("\n[4] Rango de fechas en la BD:")
        cursor.execute("SELECT MIN(date), MAX(date) FROM sales")
        min_date, max_date = cursor.fetchone()
        print(f"Desde: {min_date} | Hasta: {max_date}")

        # 5. Suma total sin filtros (para ver si hay dinero registrado)
        cursor.execute("SELECT SUM(CAST(price AS REAL)) FROM sales")
        total_historico = cursor.fetchone()[0] or 0
        print(f"\n[5] Total histórico de ventas (todas las fechas): ${total_historico}")

    except Exception as e:
        print(f"❌ Error inspeccionando: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    inspect_database()
