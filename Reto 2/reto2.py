class Usuario:
    def __init__(self, user, password, rol):
        self.usuario = user
        self.contraseña = password
        self.rol = rol

    def comprobar_password(self, password):
        return self.contraseña == password

    def menu(self):
        pass


class Admin(Usuario):
    def menu(self):
        while True:
            print(
                f"\n--- Menú ADMIN ({self.usuario}) ---\n"
                "1. Ver usuarios\n"
                "2. Crear usuario\n"
                "3. Eliminar usuario\n"
                "4. Cerrar sesión\n"
            )
            opcion = input("Elige una opción: ")

            if opcion == "1":
                print("\nUsuarios registrados:")
                for nombre, obj in usuarios.items():
                    print(f"- {nombre} ({obj.rol})")

            elif opcion == "2":
                registrar_usuario()

            elif opcion == "3":
                nombre = input("Usuario a eliminar: ")
                if nombre in usuarios:
                    if nombre == self.usuario:
                        print("❌ No puedes eliminarte a ti mismo.")
                    else:
                        del usuarios[nombre]
                        print("✅ Usuario eliminado.")
                else:
                    print("❌ Usuario no encontrado.")

            elif opcion == "4":
                print("🔒 Sesión cerrada.")
                break
            else:
                print("❌ Opción inválida.")


class Cliente(Usuario):
    def menu(self):
        while True:
            print(
                f"\n--- Menú CLIENTE ({self.usuario}) ---\n"
                "1. Ver productos (simulado)\n"
                "2. Comprar (simulado)\n"
                "3. Cerrar sesión\n"
            )
            opcion = input("Elige una opción: ")

            if opcion == "1":
                print("🛒 Productos: Producto A, Producto B, Producto C")

            elif opcion == "2":
                print("💳 Compra realizada (simulada)")

            elif opcion == "3":
                print("🔒 Sesión cerrada.")
                break
            else:
                print("❌ Opción inválida.")


# =========================
# DICCIONARIO DE USUARIOS
# =========================

usuarios = {}
usuarios["admin"] = Admin("admin", "admin123", "admin")  # admin inicial


# =========================
# FUNCIONES DEL SISTEMA
# =========================

def registrar_usuario():
    user = input("Nombre de usuario: ")
    if user in usuarios:
        print("❌ Ese usuario ya existe.")
        return

    password = input("Contraseña: ")
    rol = input("Rol (admin/cliente): ").lower()

    if rol == "admin":
        usuarios[user] = Admin(user, password, rol)
    elif rol == "cliente":
        usuarios[user] = Cliente(user, password, rol)
    else:
        print("❌ Rol inválido.")
        return

    print("✅ Usuario registrado correctamente.")


def login():
    user = input("Usuario: ")
    password = input("Contraseña: ")

    if user not in usuarios:
        print("❌ El usuario no existe.")
        return

    usuario_obj = usuarios[user]

    if not usuario_obj.comprobar_password(password):
        print("❌ Contraseña incorrecta.")
        return

    print(f"✅ Bienvenido/a {user}")
    usuario_obj.menu()  # POLIMORFISMO


# =========================
# MENÚ PRINCIPAL
# =========================

def main():
    while True:
        print(
            "\n---- Sistema de Autenticación ----\n"
            "1. Registrar nuevo usuario\n"
            "2. Iniciar sesión\n"
            "3. Salir\n"
        )
        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            login()
        elif opcion == "3":
            print("👋 Hasta luego")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()