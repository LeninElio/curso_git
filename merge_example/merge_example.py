from funciones import obtener_primera_letra

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
    if primera_letra:
        print(f"La primera letra del curso '{curso}' es: {primera_letra}")
