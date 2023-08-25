class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

lista_libros = []

def limpiar():
    #Esta función la "reacomodé" a partir de su similar creada en 2019 por 
    # Ariel Garcia Traba quien es mi profesor de Python, en ISTEA
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def agregar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    puntuacion = float(input("Ingrese la puntuación del libro: "))
    
    libro = Libro(titulo, autor, genero, puntuacion)
    lista_libros.append(libro)
    print("Libro agregado con éxito.")

def buscar_libros_por_genero():
    ''' Se que esta función se podría haber hecho más compacta por comprension pero todavía
        no tengo un buen manejo del tema'''
    genero_buscar = input("Ingrese el género que desea buscar: ")
    libros_en_genero = []
    for libro in lista_libros:
        if libro.genero == genero_buscar:
            libros_en_genero.append(libro.titulo)  
    
    if libros_en_genero:
        print(f"Libros en el género '{genero_buscar}':")
        for titulo in libros_en_genero:
            print("- " + titulo)
    else:
        print("No se encontraron libros en ese género.")
    input("\nPulse ENTER para continuar")

def recomendar_libro():
    ''' Y, en esta otra además de comprension también se podría haber usado alguna instrucción
        lambda, pero tampoco las manejo del todo bien, así que prefiero ir por lo seguro que,
        al menos en estos pequeños programas funciona sin 'quemarle' el cerebro a la PC'''
    genero_interes = input("Ingrese su género de interés: ")
    
    libros_en_genero = []
    for libro in lista_libros:
        if libro.genero == genero_interes:
            libros_en_genero.append(libro)
    
    if libros_en_genero:
        libro_recomendado = None
        max_puntuacion = float('-inf')  # Valor inicial muy pequeño
        
        for libro in libros_en_genero:
            if libro.puntuacion > max_puntuacion:
                max_puntuacion = libro.puntuacion
                libro_recomendado = libro
        
        print(f"Libro recomendado en el género '{genero_interes}': {libro_recomendado.titulo}")
    else:
        print("No se encontraron libros en ese género.")
    
    input("\nPulse ENTER para continuar")

while True:
    limpiar()
    print('''\n¿Qué acción desea realizar?
          
              1. Agregar Libro
              2. Buscar Libros por Género
              3. Recomendar Libro
              4. Salir
            ''')
    
    opcion = input("Ingrese el número de la opción: ")
    
    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        buscar_libros_por_genero()
    elif opcion == "3":
        recomendar_libro()
    elif opcion == "4":
        print("Saliendo de la aplicación.")
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")



