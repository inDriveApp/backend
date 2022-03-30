from src.core import database


def get_all(): 
    db = database.connect()
    usuarios = db.execute('SELECT id, name, status FROM public.user ORDER BY name').all()
    
    if not usuarios:
        return []
    
    retorno = []
    for usuario in usuarios:
        usr = {
            'id': usuario['id'],
            'name': usuario['name'],
            'status': usuario['status']
        }
        
        retorno.append(usr)
    
    return retorno
