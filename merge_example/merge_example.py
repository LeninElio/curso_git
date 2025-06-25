from funciones import *

lista_cursos = [
    'Python',
    'Java',
    'JavaScript',
    'C++',
    'C#',
    'Ruby',
    'PHP',
    'Swift',
    'Go',
    'Rust',
    'Kotlin',
    'TypeScript',
    'Scala',
    'Perl', # Curso añadido por frenzy
    'Dart', # Curso añadido por frenzy
    'Elixir', # Curso añadido por parallel
    'Haskell' # Curso añadido por parallel
]

for curso in lista_cursos:
    primera_letra = obtener_primera_letra(curso)
    ultima_letra = obtener_ultima_letra(curso)
    letra_aleatoria = obtener_letra_aleatoria(curso)

    if primera_letra:
        print(f"La primera letra del curso '{curso}' es: {primera_letra}")
    if ultima_letra:
        print(f"La última letra del curso '{curso}' es: {ultima_letra}")
    if letra_aleatoria:
        print(f"Una letra aleatoria del curso '{curso}' es: {letra_aleatoria}")
