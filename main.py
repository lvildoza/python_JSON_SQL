from database import get_connection

def main():
    connection = get_connection()
    if connection:
        print("Conexión exitosa")

        # Crea un cursor para ejecutar consultas
        cursor = connection.cursor()

        # Ejecuta una consulta de ejemplo
        cursor.execute("SELECT @@version;")
        row = cursor.fetchone()
        while row:
            print(row)
            row = cursor.fetchone()

        # Cierra la conexión
        connection.close()
    else:
        print("No se pudo establecer la conexión")

if __name__ == "__main__":
    main()
