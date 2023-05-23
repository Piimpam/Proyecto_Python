from pygments.lexers import get_lexer_by_name
from pygments.token import Token
import os

def contar_comentarios(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        source_code = file.readlines()

    contador_comentarios = 0
    contador_lineas_codigo = 0

    for linea in source_code:
        linea = linea.strip()
        if linea.startswith('//') or linea.startswith('/*') or linea.startswith('*') or linea.startswith('*/'):
            contador_comentarios += 1
        elif linea:
            contador_lineas_codigo += 1

    return contador_comentarios, contador_lineas_codigo

def calcular_porcentaje_comentado(ruta_carpeta):
    total_comentarios = 0
    total_lineas_codigo = 0

    for root, _, files in os.walk(ruta_carpeta):
        for file_name in files:
            if file_name.endswith('.ts'):
                file_path = os.path.join(root, file_name)
                comentarios, lineas_codigo = contar_comentarios(file_path)
                total_comentarios += comentarios
                total_lineas_codigo += lineas_codigo

    porcentaje_comentarios = (total_comentarios / (total_comentarios + total_lineas_codigo)) * 100
    
    print(f"Total de comentarios en la carpeta: {total_comentarios}")
    print(f"Total de líneas de código en la carpeta: {total_lineas_codigo}")
    
    return porcentaje_comentarios

# Ruta a la carpeta que contiene los archivos TypeScript
ruta_carpeta = 'N:\Python_Scripts\src'

porcentaje_comentarios = calcular_porcentaje_comentado(ruta_carpeta)

print(f"Porcentaje de código comentado en la carpeta: {porcentaje_comentarios:.2f}%")