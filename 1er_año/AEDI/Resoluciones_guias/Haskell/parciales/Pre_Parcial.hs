generarStock :: [String] ->[(String, Int)]
generarStock [] = []
generarStock (x:xs) = (x,cantidadApariciones x (x:xs)) : generarStock (eliminarTodos x xs)

cantidadApariciones :: (Eq t) => t -> [t] -> Int
cantidadApariciones y [] = 0
cantidadApariciones y (x:xs)
    |y == x = cantidadApariciones y xs + 1
    |otherwise = cantidadApariciones y xs

eliminarTodos :: (Eq t) => (t) -> [t] -> [t]
eliminarTodos _ [] = []
eliminarTodos y (x:xs)
    |y == x = eliminarTodos y xs
    |otherwise = x:eliminarTodos y xs

stockDeProducto :: [(String, Int)] -> String -> Int
stockDeProducto [] producto = 0
stockDeProducto ((x, y):zs) producto | x == producto = y
                                     | otherwise = stockDeProducto zs producto 

dineroEnStockAux :: (String, Int) -> [(String, Float)] -> Float
dineroEnStockAux (a, b) [] = 0
dineroEnStockAux (a, b) ((d, e):fs) | (a == d) = fromIntegral b * e 
                                    | otherwise = dineroEnStockAux (a, b) fs

dineroEnStock :: [(String, Int)] -> [(String, Float)] -> Float
dineroEnStock [] ((d, e):fs) = 0
dineroEnStock ((a, b):cs) ((d, e):fs) = dineroEnStockAux (a, b) ((d, e):fs) + dineroEnStock cs ((d, e):fs)

aplicarOfertaAux :: (String, Int) -> [(String, Float)] -> (String,Float)
aplicarOfertaAux (a, b) [] = (a, 0)
aplicarOfertaAux (a, b) ((d, e):fs) | ((a == d) && b > 10) = (d, e * 0.8)
                                    | ((a == d) && b <= 10) = (d, e)
                                    | otherwise = aplicarOfertaAux (a, b) fs

aplicarOferta :: [(String, Int)] -> [(String, Float)] -> [(String, Float)]
aplicarOferta [] ((d, e):fs) = []
aplicarOferta ((a, b):cs) ((d, e):fs) = (aplicarOfertaAux (a, b) ((d, e):fs)) : (aplicarOferta cs ((d, e):fs))

--------------------------------------
type Fila = [Int]
type Tablero = [Fila]
type Posicion = (Int, Int)
type Camino = [Posicion]

maximoAux :: Fila -> Int
maximoAux (x:[]) = x
maximoAux (x:y:xs) | (x > y) = maximoAux (x:xs)
                   | otherwise = maximoAux (y:xs)

maximo :: Tablero -> Int
maximo (x:[]) = maximoAux x
maximo (x:y:xs) | (maximoAux x > maximoAux y) = maximo (x:xs)
                | otherwise = maximo (y:xs)

contar :: Fila -> Int -> Int
contar [] n = 0
contar (x:xs) n |(x == n) = 1 + contar xs n
                |otherwise = contar xs n

masRepetidoFilaAux:: Fila -> Fila -> Int
masRepetidoFilaAux [x] original = x
masRepetidoFilaAux (x:y:xs) original| (contar original x) > (contar original y) = masRepetidoFilaAux (x:xs) original
                                    | otherwise = masRepetidoFilaAux (y:xs) original

masRepetidoFila :: Fila -> Int
masRepetidoFila xs = masRepetidoFilaAux xs xs

aplanar :: Tablero -> Fila
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs

masRepetido :: Tablero -> Int
masRepetido (x:xs) = masRepetidoFila (aplanar (x:xs))

recorrerColumna :: Fila -> Int -> Int
recorrerColumna (x:xs) 1 = x
recorrerColumna (x:xs) n = recorrerColumna xs (n - 1)

recorrerFila :: Tablero -> Int -> Fila
recorrerFila (x:xs) 1 = x
recorrerFila (x:xs) n = recorrerFila xs (n - 1)

valoresDeCaminoAux :: Tablero -> Posicion -> Int
valoresDeCaminoAux [x] (a, b) = recorrerColumna x b 
valoresDeCaminoAux (x:xs) (a, b) = recorrerColumna (recorrerFila (x:xs) a) b

valoresDeCamino :: Tablero -> Camino -> [Int]
valoresDeCamino (x:xs) [(a, b)] = [valoresDeCaminoAux (x:xs) (a, b)]
valoresDeCamino (x:xs) ((a, b):ys) = (valoresDeCaminoAux (x:xs) (a, b)) : (valoresDeCamino (x:xs) ys)

------------------------------------------------------------------------
divisoresPropiosAux:: Int -> Int -> [Int]
divisoresPropiosAux n 1 = [1]
divisoresPropiosAux  n x | ((mod n x) == 0) = x : (divisoresPropiosAux n (x - 1)) 
                         | otherwise = divisoresPropiosAux n (x - 1)

invertirLista :: [t] -> [t]
invertirLista [] = []
invertirLista (x:xs) = invertirLista xs ++ [x]

divisoresPropios :: Int -> [Int]
divisoresPropios 1 = [1]
divisoresPropios n = invertirLista (tail (divisoresPropiosAux n n))

sumarLista :: [Int] -> Int
sumarLista [x] = x
sumarLista (x:xs) = x + sumarLista xs

sonAmigos :: Int -> Int -> Bool
sonAmigos 1 1 = True
sonAmigos x y = ((sumarLista (divisoresPropios x)) == y) && ((sumarLista (divisoresPropios y)) == x)

esPerfecto :: Int -> Bool
esPerfecto 1 = False
esPerfecto n = (sumarLista (divisoresPropios n)) == n

losPrimerosNPerfectosAux :: Int -> Int -> [Int]
losPrimerosNPerfectosAux 0 primer_numero = []
losPrimerosNPerfectosAux n primer_numero | (esPerfecto primer_numero) = primer_numero : (losPrimerosNPerfectosAux (n-1) (primer_numero + 1))
                                         | otherwise = losPrimerosNPerfectosAux n (primer_numero + 1)

losPrimerosNPerfectos :: Int -> [Int]
losPrimerosNPerfectos 0 = []
losPrimerosNPerfectos n = losPrimerosNPerfectosAux n 1

listaAmigosAux :: [Int] -> [(Int, Int)]
listaAmigosAux (x:[]) = []
listaAmigosAux (x:y:xs) | (sonAmigos x y) = (x, y):(listaAmigosAux (x:xs))  
                        | otherwise = listaAmigosAux (x:xs)

listaAmigos :: [Int] -> [(Int, Int)]
listaAmigos (x:[]) = []
listaAmigos (x:y:xs) = listaAmigosAux (x:y:xs) ++ listaAmigos (y:xs)
