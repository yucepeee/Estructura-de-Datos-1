  # este es un ejemplo de representacion estatica

catalogo_peliculas = {} # catalogo de informacion de peliculas


def add_peliculas(titulo, director, mov_id, genero, year, clasificacion):
  catalogo_peliculas[mov_id]  = {'titulo': titulo, 'director': director, 'genero': genero, 'year': year, 'clasificacion': clasificacion }


def search_peliculas(busqueda):
  results = []
  for mov_id, peliculas_data in catalogo_peliculas.items():
    if (
       busqueda in peliculas_data['titulo'].lower() or 
       busqueda in peliculas_data['director'].lower() or 
       busqueda in str(peliculas_data['year']).lower() or 
       busqueda in peliculas_data['genero'].lower() or 
       busqueda in peliculas_data['clasificacion'].lower() or 
       busqueda == mov_id.lower()
       ):
       results.append(peliculas_data)
  return results


def display_peliculas():
  for mov_id, peliculas_data in catalogo_peliculas.items():
    print(f"mov_id: {mov_id}, titulo: {peliculas_data['titulo']}, director: {peliculas_data['director']}, year: {peliculas_data['year']}, genero: {peliculas_data['genero']}, clasificacion: {peliculas_data['clasificacion']}")
  

#ejemplo del uso
add_peliculas("Inception", "Christopher Nolan", "M001", "Ciencia ficción", 2010, "PG-13")
add_peliculas("The Dark Knight", "Christopher Nolan", "M002", "Acción", 2008, "PG-13")


search_results = search_peliculas("Superman")
print(search_results)

display_peliculas()

