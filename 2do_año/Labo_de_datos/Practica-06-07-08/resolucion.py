#%%
import duckdb as dd
import pandas as pd

carpeta = "/Users/lautarostude/Facultad/2do_año/Labo_de_datos/Practica-06-07-08"
dpto = pd.read_csv(f"{carpeta}/departamento.csv")
casos = pd.read_csv(f"{carpeta}/casos.csv")
grupoetario = pd.read_csv(f"{carpeta}/grupoetario.csv")
provincia = pd.read_csv(f"{carpeta}/provincia.csv")
tipoevento = pd.read_csv(f"{carpeta}/tipoevento.csv")
#%% A.a
query = """
        SELECT DISTINCT descripcion
        FROM dpto
        ORDER BY descripcion ASC

        """
dataframeResultado = dd.sql(query).df()
#%% A.c
query = """
        SELECT DISTINCT id, descripcion
        FROM dpto
        ORDER BY id ASC

        """
dataframeResultado = dd.sql(query).df()
#%% A.d
query = """
        SELECT DISTINCT *
        FROM dpto

        """
dataframeResultado = dd.sql(query).df().head()
#%% A.e
query = """
        SELECT DISTINCT id AS codigo_depto, descripcion AS nombre_depto
        FROM dpto
        ORDER BY id ASC

        """
dataframeResultado = dd.sql(query).df()
#%% A.f
query = """
        SELECT DISTINCT *
        FROM dpto
        WHERE id_provincia = 54
        ORDER BY id

        """
dataframeResultado = dd.sql(query).df()
#%% A.g
query = """
        SELECT DISTINCT *
        FROM dpto
        WHERE id_provincia = 22 OR id_provincia = 78 OR id_provincia = 86
        ORDER BY id_provincia, id

        """
dataframeResultado = dd.sql(query).df()
#%% A.h
query = """
        SELECT DISTINCT *
        FROM dpto
        WHERE id_provincia >= 50 AND id_provincia <= 59
        ORDER BY id_provincia, id

        """
dataframeResultado = dd.sql(query).df()
#%% B.a
query = """
        SELECT DISTINCT *
        FROM dpto, provincia
        WHERE dpto.id_provincia = provincia.id

        """
dataframeResultado = dd.sql(query).df()
#%% B.c
query = """
        SELECT casos.*
        FROM casos, dpto, provincia
        WHERE casos.id_depto = dpto.id 
            AND dpto.id_provincia = provincia.id 
            AND provincia.descripcion = 'Chaco';
        """
              
dataframeResultado = dd.sql(query).df()
#%% B.d
query = """
        SELECT casos.*
        FROM casos, dpto, provincia
        WHERE casos.id_depto = dpto.id 
            AND dpto.id_provincia = provincia.id 
            AND provincia.descripcion = 'Buenos Aires' 
            AND casos.cantidad > 10;

        """
dataframeResultado = dd.sql(query).df()
#%% C.a
query = """
        SELECT dpto.descripcion
        FROM dpto
        LEFT JOIN casos 
        ON dpto.id = casos.id_depto
        WHERE casos.id_depto IS NULL;

        """
dataframeResultado = dd.sql(query).df()
#%% C.b
query = """
        SELECT tipoevento.descripcion
        FROM tipoevento
        LEFT JOIN casos 
        ON tipoevento.id = casos.id_tipoevento
        WHERE casos.id_tipoevento IS NULL;

        """
dataframeResultado = dd.sql(query).df()
#%% D.a
query = """
        SELECT SUM(cantidad) AS total_casos
        FROM casos;
        """
dataframeResultado = dd.sql(query).df()

#%% D.b
query = """
        SELECT tipoevento.descripcion AS tipo_evento, casos.anio, SUM(casos.cantidad) AS cantidad_total
        FROM casos
        JOIN tipoevento ON casos.id_tipoevento = tipoevento.id
        GROUP BY tipoevento.descripcion, casos.anio
        ORDER BY tipoevento.descripcion ASC, casos.anio ASC;
        """
dataframeResultado = dd.sql(query).df()

#%% D.c
query = """
        SELECT tipoevento.descripcion AS tipo_evento, casos.anio, SUM(casos.cantidad) AS cantidad_total
        FROM casos
        JOIN tipoevento ON casos.id_tipoevento = tipoevento.id
        WHERE casos.anio = 2019
        GROUP BY tipoevento.descripcion, casos.anio
        ORDER BY tipoevento.descripcion ASC, casos.anio ASC;
        """
dataframeResultado = dd.sql(query).df()

#%% D.d
query = """
        SELECT id_provincia, COUNT(id) AS total_departamentos
        FROM dpto
        GROUP BY id_provincia
        ORDER BY id_provincia ASC;
        """
dataframeResultado = dd.sql(query).df()
#%% D.e

query_totales_2019 = """
        SELECT dpto.descripcion AS depto, SUM(casos.cantidad) AS total_casos
        FROM casos
        JOIN dpto ON casos.id_depto = dpto.id
        WHERE casos.anio = 2019
        GROUP BY dpto.descripcion
        """
df_totales_2019 = dd.sql(query_totales_2019).df()

query_minimo = """
        SELECT MIN(total_casos) AS min_casos
        FROM df_totales_2019
        """
df_min_2019 = dd.sql(query_minimo).df()

query_final = """
        SELECT df_totales_2019.depto, df_totales_2019.total_casos
        FROM df_totales_2019
        JOIN df_min_2019 ON df_totales_2019.total_casos = df_min_2019.min_casos
        """
dataframeResultado = dd.sql(query_final).df()

#%% D.f

query_totales_2020 = """
        SELECT dpto.descripcion AS depto, SUM(casos.cantidad) AS total_casos
        FROM casos
        JOIN dpto ON casos.id_depto = dpto.id
        WHERE casos.anio = 2020
        GROUP BY dpto.descripcion
        """
df_totales_2020 = dd.sql(query_totales_2020).df()

query_maximo = """
        SELECT MAX(total_casos) AS max_casos
        FROM df_totales_2020
        """
df_max_2020 = dd.sql(query_maximo).df()

query_final = """
        SELECT df_totales_2020.depto, df_totales_2020.total_casos
        FROM df_totales_2020
        JOIN df_max_2020 ON df_totales_2020.total_casos = df_max_2020.max_casos
        """
dataframeResultado = dd.sql(query_final).df()

#%% D.g
query = """
        SELECT provincia.descripcion AS provincia, casos.anio, AVG(casos.cantidad) AS promedio_casos
        FROM casos
        JOIN dpto ON casos.id_depto = dpto.id
        JOIN provincia ON dpto.id_provincia = provincia.id
        GROUP BY provincia.descripcion, casos.anio;
        """
dataframeResultado = dd.sql(query).df()

#%% D.h
query_totales = """
        SELECT provincia.descripcion AS provincia, dpto.descripcion AS depto, casos.anio, SUM(casos.cantidad) AS total_casos
        FROM casos
        JOIN dpto ON casos.id_depto = dpto.id
        JOIN provincia ON dpto.id_provincia = provincia.id
        GROUP BY provincia.descripcion, dpto.descripcion, casos.anio;
        """
df_totales = dd.sql(query_totales).df()

query_maximos = """
        SELECT provincia, anio, MAX(total_casos) AS max_casos
        FROM df_totales
        GROUP BY provincia, anio;
        """
df_maximos = dd.sql(query_maximos).df()

query_final = """
        SELECT df_totales.provincia, df_totales.anio, df_totales.depto, df_totales.total_casos
        FROM df_totales
        JOIN df_maximos 
          ON df_totales.provincia = df_maximos.provincia 
         AND df_totales.anio = df_maximos.anio 
         AND df_totales.total_casos = df_maximos.max_casos;
        """
dataframeResultado = dd.sql(query_final).df()

#%% D.i

query = """
        SELECT 
            SUM(casos.cantidad) AS total, 
            MAX(casos.cantidad) AS maxima, 
            MIN(casos.cantidad) AS minima, 
            AVG(casos.cantidad) AS promedio
        FROM casos
        JOIN dpto ON casos.id_depto = dpto.id
        JOIN provincia ON dpto.id_provincia = provincia.id
        WHERE provincia.descripcion = 'Buenos Aires' AND casos.anio = 2019;
        """
dataframeResultado = dd.sql(query).df()

#%% D.j

query = """
        SELECT 
            SUM(casos.cantidad) AS total, 
            MAX(casos.cantidad) AS maxima, 
            MIN(casos.cantidad) AS minima, 
            AVG(casos.cantidad) AS promedio
        FROM casos
        JOIN dpto ON casos.id_depto = dpto.id
        JOIN provincia ON dpto.id_provincia = provincia.id
        WHERE provincia.descripcion = 'Buenos Aires' AND casos.anio = 2019 AND casos.cantidad > 1000;
        """
dataframeResultado = dd.sql(query).df()

#%% D.k

query_2019 = """
        SELECT DISTINCT id_depto 
        FROM casos 
        WHERE anio = 2019
        """
df_deptos_2019 = dd.sql(query_2019).df()


query_2020 = """
        SELECT DISTINCT id_depto 
        FROM casos 
        WHERE anio = 2020
        """
df_deptos_2020 = dd.sql(query_2020).df()

query_final = """
        SELECT provincia.descripcion AS provincia, dpto.descripcion AS departamento, AVG(casos.cantidad) AS promedio_casos
        FROM casos
        JOIN dpto ON casos.id_depto = dpto.id
        JOIN provincia ON dpto.id_provincia = provincia.id
        JOIN df_deptos_2019 ON dpto.id = df_deptos_2019.id_depto
        JOIN df_deptos_2020 ON dpto.id = df_deptos_2020.id_depto
        GROUP BY provincia.descripcion, dpto.descripcion
        ORDER BY provincia.descripcion ASC, dpto.descripcion ASC;
        """
dataframeResultado = dd.sql(query_final).df()

#%% D.l

query = """
        SELECT 
            tipoevento.descripcion AS tipo_evento,
            dpto.id AS id_depto,
            dpto.descripcion AS nombre_departamento,
            provincia.id AS id_provincia,
            provincia.descripcion AS nombre_provincia,
            SUM(CASE WHEN casos.anio = 2019 THEN casos.cantidad ELSE 0 END) AS total_casos_2019,
            SUM(CASE WHEN casos.anio = 2020 THEN casos.cantidad ELSE 0 END) AS total_casos_2020
        FROM casos
        JOIN tipoevento ON casos.id_tipoevento = tipoevento.id
        JOIN dpto ON casos.id_depto = dpto.id
        JOIN provincia ON dpto.id_provincia = provincia.id
        GROUP BY tipoevento.descripcion, dpto.id, dpto.descripcion, provincia.id, provincia.descripcion;
        """
dataframeResultado = dd.sql(query).df()

#%% E.a
query = """
        SELECT dpto.descripcion, casos.cantidad
        FROM casos
        JOIN dpto ON casos.id_depto = dpto.id
        WHERE casos.cantidad >= ALL (
            SELECT cantidad 
            FROM casos
        );
        """
dataframeResultado = dd.sql(query).df()

#%% E.b
query = """
        SELECT tipoevento.descripcion
        FROM tipoevento
        WHERE tipoevento.id = ANY (
            SELECT id_tipoevento 
            FROM casos
        );
        """
dataframeResultado = dd.sql(query).df()

#%% F.a
query = """
        SELECT tipoevento.descripcion
        FROM tipoevento
        WHERE tipoevento.id IN (
            SELECT id_tipoevento 
            FROM casos
        );
        """
dataframeResultado = dd.sql(query).df()

#%% F.b
query = """
        SELECT tipoevento.descripcion
        FROM tipoevento
        WHERE tipoevento.id NOT IN (
            SELECT id_tipoevento 
            FROM casos
        );
        """
dataframeResultado = dd.sql(query).df()

#%% G.a
query = """
        SELECT tipoevento.descripcion
        FROM tipoevento
        WHERE EXISTS (
            SELECT 1 
            FROM casos 
            WHERE casos.id_tipoevento = tipoevento.id
        );
        """
dataframeResultado = dd.sql(query).df()

#%% G.b
query = """
        SELECT tipoevento.descripcion
        FROM tipoevento
        WHERE NOT EXISTS (
            SELECT 1 
            FROM casos 
            WHERE casos.id_tipoevento = tipoevento.id
        );
        """
dataframeResultado = dd.sql(query).df()

#%% H.a
# Subconsulta correlacionada: se calcula el promedio por provincia (Total País / Cantidad de Provincias) para ese mismo año
query = """
        SELECT provincia.descripcion AS provincia, casos.anio, SUM(casos.cantidad) AS total_provincia
        FROM casos
        JOIN dpto ON casos.id_depto = dpto.id
        JOIN provincia ON dpto.id_provincia = provincia.id
        GROUP BY provincia.descripcion, casos.anio
        HAVING SUM(casos.cantidad) > (
            SELECT SUM(casos_sub.cantidad) / COUNT(DISTINCT dpto_sub.id_provincia)
            FROM casos AS casos_sub
            JOIN dpto AS dpto_sub ON casos_sub.id_depto = dpto_sub.id
            WHERE casos_sub.anio = casos.anio
        )
        ORDER BY casos.anio ASC, total_provincia DESC;
        """
dataframeResultado = dd.sql(query).df()

#%% H.b
# Subconsulta correlacionada: se busca el total de Corrientes conectando el año de la subconsulta con el año de la consulta principal
query = """
        SELECT provincia.descripcion AS provincia, casos.anio, SUM(casos.cantidad) as total_casos
        FROM casos
        JOIN dpto ON casos.id_depto = dpto.id
        JOIN provincia ON dpto.id_provincia = provincia.id
        GROUP BY provincia.descripcion, casos.anio
        HAVING SUM(casos.cantidad) > (
            SELECT SUM(casos_sub.cantidad)
            FROM casos AS casos_sub
            JOIN dpto AS dpto_sub ON casos_sub.id_depto = dpto_sub.id
            JOIN provincia AS provincia_sub ON dpto_sub.id_provincia = provincia_sub.id
            WHERE provincia_sub.descripcion = 'Corrientes' AND casos_sub.anio = casos.anio
        )
        ORDER BY casos.anio ASC, total_casos DESC;
        """
dataframeResultado = dd.sql(query).df()
