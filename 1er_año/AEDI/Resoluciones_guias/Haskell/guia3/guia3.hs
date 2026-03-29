--Anteriores en carpeta Resoluciones_labos
--Punto 5
f :: Int -> Int
f n | n <= 7 = n^2
    | n > 7 = 2 * n - 1

g :: Int -> Int
g n | mod n 2 == 0 = div n 2
    | otherwise = 3 * n + 1

todosMenores :: (Int, Int, Int) -> Bool
todosMenores (t0, t1, t2) = f t0 > g t0 && f t1 > g t1 && f t2 > g t2

--Punto 6
type Anio = Integer
type EsBisiesto = Bool

bisiesto :: Anio -> EsBisiesto
bisiesto n | (mod n 4 /= 0) = False
           | (mod n 100 == 0 && mod n 400 /= 0) = False
           | otherwise = True

--Punto 7

valorAbsoluto :: Float -> Float
valorAbsoluto x 
    | x >= 0    = x
    | otherwise = (-x)

distanciaManhattan (x1, y1, z1) (x2, y2, z2) = 
    valorAbsoluto(x1 - x2) + valorAbsoluto(y1 - y2) + valorAbsoluto(z1 - z2)

--Punto 8
absoluto :: Int -> Int
absoluto n | n >= 0 = n
      | otherwise = -n 

sumaUltimosDigitos :: Int -> Int
sumaUltimosDigitos n = (mod (absoluto n) 10) + (mod(div (absoluto n) 10) 10)

comparar :: Int -> Int -> Int
comparar x y | (sumaUltimosDigitos x < sumaUltimosDigitos y) = 1
             | (sumaUltimosDigitos x > sumaUltimosDigitos y) = (-1)
             | (sumaUltimosDigitos x == sumaUltimosDigitos y) = 0