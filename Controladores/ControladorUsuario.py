from Modelos.Usuario import Usuario
from Repositorios.RepositorioUsuario import RepositorioUsuario
import hashlib

class ControladorUsuario():
    def __init__(self):
        self.repositorioUsuario = RepositorioUsuario()

    def index(self):
        return self.repositorioUsuario.findAll()

    def create(self, infoUsuario):
        nuevoUsuario = Usuario(infoUsuario)
        if(self.uniqueUser(infoUsuario["nickname"])==False):
            nuevoUsuario.password = self.encrypt_string(infoUsuario["password"])
            return self.repositorioUsuario.save(nuevoUsuario)
        else:
            return {
                "status": "not created",
                "message": "El nombre de usuario ya existe"
            }

    def show(self, id):
        elUsuario = Usuario(self.repositorioUsuario.findById(id))
        return elUsuario.__dict__

    def delete(self, id):
        try:
            elUsuario = Usuario(self.repositorioUsuario.findById(id))
        except:
            elUsuario = None
        if(elUsuario is not None):
            self.repositorioUsuario.delete(id)
            return {
                "status": "user deleted",
                "message": "Usuario eliminado correctamente"
            }
        else:
            return {
                "status": "User not deleted",
                "message": "El usuario no fue eliminado"
            }

    def uniqueUser(self, nickName):
        usuarios = self.repositorioUsuario.findAll()
        for usuario in usuarios:
            if(nickName == usuario["nickname"]):
                return True
        return False

    def encrypt_string(self, hash_string):
        sha_signature = \
            hashlib.sha256(hash_string.encode()).hexdigest()
        return sha_signature