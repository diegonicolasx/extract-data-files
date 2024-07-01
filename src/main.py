from utils import list_excel_files
from om_generation import om_generation

print("Programa para extraer datos.")
year=input("Ingrese el año: ")
portfolio=input("Ingrese el portafolio: ")
list_excel_files()
om_generation(year, portfolio)