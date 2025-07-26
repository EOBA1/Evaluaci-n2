def clasificar_acl_ipv4(numero_acl):
    """
    Clasifica un número de ACL IPv4 como Estándar, Extendida o No Corresponde.

    Args:
        numero_acl (int): El número entero de la ACL IPv4.

    Returns:
        str: Un mensaje indicando el tipo de ACL o si no corresponde.
    """
    # Rangos de ACL Estándar IPv4
    # Las ACL Estándar normalmente van del 1 al 99 y del 1300 al 1999.
    if (1 <= numero_acl <= 99) or (1300 <= numero_acl <= 1999):
        return f"El número {numero_acl} corresponde a una ACL Estándar IPv4."
    # Rangos de ACL Extendida IPv4
    # Las ACL Extendida normalmente van del 100 al 199 y del 2000 al 2699.
    elif (100 <= numero_acl <= 199) or (2000 <= numero_acl <= 2699):
        return f"El número {numero_acl} corresponde a una ACL Extendida IPv4."
    # Si el número no cae en ninguno de los rangos anteriores
    else:
        return f"El número {numero_acl} no corresponde a un rango conocido de ACL IPv4."






if __name__ == "__main__":
    print("--- Clasificador de ACL IPv4 ---")
    print("Introduce el número de la ACL para determinar su tipo.")

    while True: # Bucle para permitir al usuario probar múltiples números
        entrada_usuario = input("Por favor, introduce el número de ACL (o 'salir' para terminar): ")

        if entrada_usuario.lower() == 'salir':
            print("Saliendo del clasificador. ¡Hasta luego!")
            break # Sale del bucle

        try:
            # Intentamos convertir la entrada del usuario a un número entero
            numero_acl_introducido = int(entrada_usuario)

            # Llamamos a la función para clasificar el número
            resultado = clasificar_acl_ipv4(numero_acl_introducido)
            print(resultado)
            print("-" * 30) # Separador para la siguiente entrada

        except ValueError:
            # Capturamos el error si la entrada no es un número válido
            print("Entrada no válida. Por favor, introduce un número entero o 'salir'.")
            print("-" * 30) # Separador
        except Exception as e:
            # Capturamos cualquier otro error inesperado
            print(f"Ocurrió un error inesperado: {e}")
            print("-" * 30  ) 