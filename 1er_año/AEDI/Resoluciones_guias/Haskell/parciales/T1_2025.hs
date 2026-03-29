-- Ejercicio 1
cantidadNumerosAbundantes :: Integer -> Integer -> Integer
cantidadNumerosAbundantes x y 
  | x <= y && esAbundante x = 1 + (cantidadNumerosAbundantes (x + 1) y)
  | x <= y && not (esAbundante x) = (cantidadNumerosAbundantes (x + 1) y) 
  | otherwise = 0

divisoresPropiosAux:: Integer -> Integer -> [Integer]
divisoresPropiosAux n 1 = [1]
divisoresPropiosAux n x 
  | ((mod n x) == 0) = x : (divisoresPropiosAux n (x - 1)) 
  | otherwise = divisoresPropiosAux n (x - 1)

invertirLista :: [t] -> [t]
invertirLista [] = []
invertirLista (x:xs) = invertirLista xs ++ [x]

divisoresPropios :: Integer -> [Integer]
divisoresPropios 1 = [1]
divisoresPropios n = invertirLista (tail (divisoresPropiosAux n n))

sumarLista :: [Integer] -> Integer
sumarLista [x] = x
sumarLista (x:xs) = x + sumarLista xs

esAbundante :: Integer -> Bool
esAbundante n = (sumarLista (divisoresPropios n)) > n 

-- Ejercicio 2
cursadasVencidas :: [(String, Integer, Integer)] -> [String]
cursadasVencidas [] = []
cursadasVencidas ((nombre, año, cuatri):xs)
  | año < 2021 = nombre : cursadasVencidas xs
  | año == 2021 && cuatri == 1 = nombre : cursadasVencidas xs
  | otherwise = cursadasVencidas xs

-- Ejercicio 3
saturarEnUmbralHastaNegativo :: [Integer] -> Integer -> [Integer]
saturarEnUmbralHastaNegativo [] n = []
saturarEnUmbralHastaNegativo (x:xs) n
  | x < 0 = []
  | x > n = n : saturarEnUmbralHastaNegativo xs n
  | otherwise = x : saturarEnUmbralHastaNegativo xs n

-- Ejercicio 4
cantidadParesColumna :: [[Integer]] -> Integer -> Integer
cantidadParesColumna [] n = 0
cantidadParesColumna (x:xs) n = cantPares (iesimaColumna (x:xs) n) 

iesimoNumero :: [Integer] -> Integer -> Integer
iesimoNumero (x:xs) 1 = x
iesimoNumero (x:xs) n = iesimoNumero xs (n-1)

iesimaColumna :: [[Integer]] -> Integer -> [Integer]
iesimaColumna [] n = []
iesimaColumna [[x]] n = [x]
iesimaColumna (x:xs) n = iesimoNumero x n : iesimaColumna xs n

esPar :: Integer -> Bool
esPar n = mod n 2 == 0

cantPares :: [Integer] -> Integer 
cantPares [] = 0
cantPares (x:xs) 
  | esPar x = 1 + cantPares xs
  | otherwise = cantPares xs