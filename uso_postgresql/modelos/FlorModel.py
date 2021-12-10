from Conexion import Conexion

class FlorModel:

    def listarTodos(self):
        """Retorna una lista de ciudad
        Retorna:
        items -- tupla
        """
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("SELECT * FROM flores")
            items = cursor.fetchall()        
            cursor.close()
            con.close()                
            return items
        except con.Error as e:
            print(e.pgerror)  