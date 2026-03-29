import Foreign.C (CWchar)
longitud :: [t] -> Int
longitud (x:[]) = 1
longitud (x:xs) = 1 + longitud xs

ultimo :: [t] -> t
ultimo (x:[]) = x
ultimo (x:xs) = ultimo xs

principio :: [t] -> [t]
principio (x:[]) = []
principio (x:xs) = (x:principio (xs))

reverso :: [t] -> [t]
reverso [] = []
reverso xs = (ultimo xs):(reverso (principio xs)) 

-- --------------------------------------------------------

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece n [] = False 
pertenece n (x:xs) | n == x = True
                   | otherwise = pertenece n xs 

todosIguales :: (Eq t) => [t] -> Bool
todosIguales (x:[]) = True
todosIguales (x:xs) = ((x == head xs) && todosIguales xs) 
                    
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:xs) 
    | pertenece x xs = False
    | otherwise = todosDistintos xs 

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) 
    | pertenece x xs = True 
    | otherwise = hayRepetidos xs  

quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = [] 
quitar n (x:xs) 
    | n == x    = xs 
    | otherwise = x : quitar n xs

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos n (x:xs)
    | n == x    = quitarTodos n xs 
    | otherwise = x : quitarTodos n xs

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | (quitarTodos x xs == xs) = x : eliminarRepetidos xs
                         | otherwise = eliminarRepetidos xs

mismosElementosAux :: (Eq t) => [t] -> [t] -> Bool
mismosElementosAux [] [] = True
mismosElementosAux [] _ = False
mismosElementosAux (x:xs) [] = False 
mismosElementosAux (x:xs) ys 
    | pertenece x ys = mismosElementosAux xs ys
    | otherwise = False

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos xs ys = mismosElementosAux xs ys && mismosElementosAux ys xs

capicua :: (Eq t) => [t] -> Bool 
capicua xs = xs == reverso xs

-- -----------------------------------------

sumatoria :: [Int] -> Int
sumatoria (x:[]) = x
sumatoria (x:xs) = x + sumatoria xs

productoria :: [Int] -> Int
productoria (x:[]) = x
productoria (x:xs) = x * productoria xs

maximo :: [Int] -> Int
maximo [] = 0
maximo [x] = x
maximo (x:xs) | x > maximo xs = x
              | otherwise = maximo xs

sumarN :: Int -> [Int] -> [Int]
sumarN _ [] = [] 
sumarN n (x:xs) = (n + x):(sumarN n xs)

sumarPrimero :: [Int] -> [Int]
sumarPrimero [] = []
sumarPrimero xs = sumarN (head xs) (xs)

sumarElUltimo :: [Int] -> [Int]
sumarElUltimo [] = []
sumarElUltimo xs = sumarN (ultimo xs) (xs)

pares :: [Int] -> [Int]
pares [] = []
pares (x:xs) | (mod x 2 == 0) = (x):(pares xs)
             | otherwise = pares xs

multiplosDeN :: Int -> [Int] -> [Int]
multiplosDeN _ [] = []
multiplosDeN n (x:xs) | (mod x n == 0) = (x):(multiplosDeN n xs)
                      | otherwise = multiplosDeN n xs

minimo :: [Int] -> Int
minimo [] = 0
minimo [x] = x
minimo (x:xs) | (x < minimo xs) = x
              | otherwise = minimo xs 

ordenar :: [Int] -> [Int]
ordenar [] = []
ordenar xs = (minimo xs):(ordenar (quitar (minimo xs) xs))

-------------------------------------------------------

sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x:[]) = [x]
sacarBlancosRepetidos (x:y:xs) | ((x == ' ') && (x == y)) = (sacarBlancosRepetidos (y:xs))
                               | otherwise = x:(sacarBlancosRepetidos (y:xs))

contarPalabras :: [Char] -> Int
contarPalabras [] = 0
contarPalabras [x] = 0
contarPalabras (x:y:xs) | ((x == ' ') && (y /= ' ')) = 1 + contarPalabras (y:xs)
                        | otherwise = contarPalabras (y:xs)
agarrarPalabra :: [Char] -> [Char]
agarrarPalabra [] = []
agarrarPalabra (x:xs)| (x == ' ') = []
                     | otherwise = x:(agarrarPalabra xs)

saltearPalabra :: [Char] -> [Char]
saltearPalabra [] = []
saltearPalabra (x:xs) | x == ' ' = xs
                      | otherwise = saltearPalabra xs

palabras :: [Char] -> [[Char]]
palabras [] = []
palabras (x:xs) | x == ' ' = palabras xs
                | otherwise = (agarrarPalabra (x:xs)) : (palabras (saltearPalabra (x:xs)))

contarLetras :: [Char] -> Int
contarLetras [] = 0
contarLetras (x:xs) = 1 + contarLetras xs

palabrasMasLarga :: [Char] -> [Char]
palabrasMasLarga [] = []
palabrasMasLarga (x:xs) | contarLetras (agarrarPalabra (x:xs)) > contarLetras (palabrasMasLarga (saltearPalabra (x:xs))) = agarrarPalabra (x:xs)
                        | otherwise = palabrasMasLarga (saltearPalabra xs)

aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar ([]:xs) = aplanar xs 
aplanar ((y:ys):xs) = y : aplanar (ys:xs)

aplanarConEspacio :: [[Char]] -> [Char]
aplanarConEspacio [] = []
aplanarConEspacio ([]:xs) = ' ' : (aplanarConEspacio xs)
aplanarConEspacio ((y:ys):xs) = y : (aplanarConEspacio (ys:xs))

sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada [x] = [x]
sumaAcumulada (x:y:xs) = x: sumaAcumulada ((x + y):xs)

-----------------------------------------------------------
--preguntar donde poner los types
type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos [] [] = False
enLosContactos nombre [] = False
enLosContactos nombre (ys:cs) | (nombre == fst ys) = True
                              | otherwise = enLosContactos nombre cs

agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto ([], []) [] = []
agregarContacto (xs, ys) [] = [(xs, ys)]
agregarContacto (xs, ys) cs | enLosContactos xs cs = cs
                            | otherwise = ((xs, ys)) :  cs

eliminarContacto :: Nombre -> ContactosTel -> ContactosTel
eliminarContacto [] [] = []
eliminarContacto nombre [] = []
eliminarContacto nombre ((x,y):zs) | enLosContactos nombre [(x,y)] = zs
                                | otherwise = eliminarContacto nombre zs

-----------------------------------------------------------------------------

type Identificacion = Integer
type Ubicacion = Texto
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]
type Disponibilidad = Bool

existeElLocker :: Identificacion -> MapaDeLockers -> Bool
existeElLocker _ [] = False
existeElLocker id ((x, y):zs) | id == x = True
                              | otherwise = existeElLocker id zs 

ubicacionDelLocker :: Identificacion -> MapaDeLockers -> Ubicacion
ubicacionDelLocker _ [] = []
ubicacionDelLocker id ((x, (a, b)):zs)  | (id == x) = b
                                        | otherwise = ubicacionDelLocker id zs

estaDisponibleElLocker :: Identificacion -> MapaDeLockers -> Bool 
estaDisponibleElLocker _ [] = False
estaDisponibleElLocker id ((x, (a, b)):zs) | (id == x) = a
                                           | otherwise = estaDisponibleElLocker id zs
                
ocuparLocker :: Identificacion -> MapaDeLockers -> MapaDeLockers
ocuparLocker id ((x, (a, b)):zs) | (id == x) && a   = ((id, (False, b)):zs)
                                 | otherwise        = (x, (a, b)) : (ocuparLocker id zs)

----------------------------------------------------------------
sumaTotalAux :: [Int] -> Int
sumaTotalAux [] = 0
sumaTotalAux (x:xs) = x + sumaTotalAux xs

sumaTotal :: [[Int]] -> Int
sumaTotal [] = 0
sumaTotal (xs:ys) = sumaTotalAux xs + sumaTotal ys

cantidadDeAparicionesAux :: Int -> [Int] -> Int
cantidadDeAparicionesAux _ [] = 0
cantidadDeAparicionesAux n (x:xs) | (n == x) = 1 + cantidadDeAparicionesAux n xs
                                  | otherwise = cantidadDeAparicionesAux n xs

cantidadDeApariciones :: Int -> [[Int]] -> Int
cantidadDeApariciones _ [] = 0 
cantidadDeApariciones n (xs:ys) = cantidadDeAparicionesAux n xs + cantidadDeApariciones n ys

contarPalabrasMatrizAux :: [Char] -> [Char] -> Int
contarPalabrasMatrizAux xs [] = 0
contarPalabrasMatrizAux xs ys | (xs == agarrarPalabra ys) = 1 + contarPalabrasMatrizAux xs (saltearPalabra ys)
                              | otherwise = contarPalabrasMatrizAux xs (saltearPalabra ys)

contarPalabrasMatriz :: [Char] -> [[Char]] -> Int
contarPalabrasMatriz xs [] = 0
contarPalabrasMatriz xs (ys:zs) = (contarPalabrasMatrizAux xs ys) + (contarPalabrasMatriz xs zs)

multiplicarPorEscalarAux :: Int -> [Int] -> [Int]
multiplicarPorEscalarAux n [] = []
multiplicarPorEscalarAux n (x:xs) = (n * x) : (multiplicarPorEscalarAux n xs)

multiplicarPorEscalar :: Int -> [[Int]] -> [[Int]]
multiplicarPorEscalar n [] = []
multiplicarPorEscalar n (xs:ys) = (multiplicarPorEscalarAux n xs) : multiplicarPorEscalar n ys 

concatenarFilas :: [[Char]] -> [Char]
concatenarFilas [] = []
concatenarFilas ([]:ys) = concatenarFilas ys
concatenarFilas ((x:xs):ys) = x : concatenarFilas (xs:ys)
    
iesimaFila :: Int -> [[a]] -> [a] 
iesimaFila n [] = []
iesimaFila 0 (xs:ys) = xs
iesimaFila n (xs:ys) = iesimaFila (n-1) ys

elementoN :: Int -> [a] -> a
elementoN 0 (x:xs) = x
elementoN n (x:xs) = elementoN (n-1) xs

iesimaColumna :: Int -> [[a]] -> [a]
iesimaColumna _ [] = []
iesimaColumna 0 (xs:ys) = []
iesimaColumna n (xs:ys) = (elementoN n xs) : (iesimaColumna n ys)