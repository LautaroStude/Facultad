#%%
import pandas as pd
import duckdb as dd
#%%
carpeta = "/Users/lautarostude/Facultad/2do_año/Labo_de_datos/TP1"
censo2010 = pd.read_excel(f"{carpeta}/censo2010.xlsX")
censo2022 = pd.read_excel(f"{carpeta}/censo2022.xlsX")
establecimientos = pd.read_excel(f"{carpeta}/establecimientos-asistenciales-asentados-registro-federal-refes-20220404.xlsX")
nac2010 = pd.read_csv(f"{carpeta}/nacweb10.csv", encoding="cp1252")
nac2022 = pd.read_csv(f"{carpeta}/nacweb22_0.csv", encoding="cp1252")
