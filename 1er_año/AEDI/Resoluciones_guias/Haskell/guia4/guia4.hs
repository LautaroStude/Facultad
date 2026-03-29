--Punto 1
fib :: Int -> Int
fib n | (n == 0) = 0
      | (n == 1) = 1
      |  otherwise = fib (n - 1) + fib (n - 2)

--Punto 2
parteEntera :: Float -> Int
parteEntera n | n < 1 = 0
              | otherwise = parteEntera (n - 1) + 1
              -- Agrego 1 por cada n y voy restando hasta llegar a n menor a 1 (caso base)
--Punto 4
sumaImpares :: Int -> Int
sumaImpares n | n == 0 = 0
              | otherwise = sumaImpares (n - 1) + ((2 * n) - 1)  

--Punto 5
medioFact :: Int -> Int
medioFact n | n == 0 = 1
            | n == 1 = 1
            | otherwise = (medioFact (n - 2)) * n

--Punto 6
todosDigitosIguales :: Int -> Bool
todosDigitosIguales n | n < 10 = True
                      | otherwise = (mod n 10 == mod (div n 10) 10) && todosDigitosIguales (div n 10)

--Punto 8
sumaDigitos :: Int -> Int
sumaDigitos n | n == 0 = 0
              | otherwise = mod n 10 + sumaDigitos (div n 10)

--Punto 9
contarDigitos :: Int -> Int
contarDigitos 0 = 0
contarDigitos n = 1 + contarDigitos (div n 10)

invertir :: Int -> Int
invertir 0 = 0
invertir n = (mod n 10) * 10 ^ ((contarDigitos n) - 1) + invertir (div n 10)

esCapicua :: Int -> Bool
esCapicua n = n == invertir n

--Punto 10 

f1 :: Int -> Int
f1 0 = 1
f1 n = (2 ^ n) + f1 (n - 1) 

f2 :: Float -> Int -> Float
f2 q 1 = q
f2 q n = (q ^ n) + f2 q (n - 1)

f3 :: Float -> Int -> Float
f3 q 0 = 0
f3 q n = q^(2*n) + f3 q (n-1) + q^(2*n - 1)

--Hacer punto d

--Punto 11 no anda por error de tipado, preguntar que hacer si creo una funcion para cambiar el tipo

--factorial :: Int -> Int
--factorial 0 = 1
--factorial n = n * factorial (n - 1)

--numero_e :: Int -> Float
--numero_e 0 = factorial 0
--numero_e n = (1 / factorial n) + numero_e (n - 1)

--Punto 13
sumatoriaAux :: Int -> Int -> Int
sumatoriaAux n 1 = n
sumatoriaAux n m = (n ^ m) + sumatoriaAux n (m - 1)

sumatoriaDoble :: Int -> Int -> Int
sumatoriaDoble 1 m = sumatoriaAux 1 m
sumatoriaDoble n m = sumatoriaDoble (n - 1) m + sumatoriaAux n m

--Punto 14

sumaPotenciasAux :: Int -> Int -> Int -> Int
sumaPotenciasAux q n 0 = 0
sumaPotenciasAux q n m = q ^ (n + m) + sumaPotenciasAux q n (m - 1)

sumaPotencias :: Int -> Int -> Int -> Int
sumaPotencias q 0 m = 0
sumaPotencias q n m = sumaPotenciasAux q n m + sumaPotencias q (n - 1) m

--Punto 15

intAFloat :: Int -> Float
intAFloat 0 = 0.0
intAFloat n | n > 0 = 1.0 + intAFloat (n - 1) --Esto para punto 11

sumaRacionalesAux :: Int -> Int -> Float
sumaRacionalesAux n 1 = intAFloat n 
sumaRacionalesAux n m = (intAFloat n / intAFloat m) + sumaRacionalesAux n (m - 1)

sumaRacionales :: Int -> Int -> Float
sumaRacionales 1 m = sumaRacionalesAux 1 m
sumaRacionales n m = sumaRacionalesAux n m + sumaRacionales (n - 1) m 

--Punto 16

posibleDivisor :: Int -> Int -> Int
posibleDivisor n d | (mod n d == 0) = d 
                   | otherwise = posibleDivisor n (d + 1)

menorDivisor :: Int -> Int
menorDivisor n = posibleDivisor n 2

esPrimo :: Int -> Bool
esPrimo n = menorDivisor n == n

--sonCoprimosAux :: Int -> Int -> Int -> Bool
--sonCoprimosAux x y d
--  | d > x || d > y            = True  
--  | x `mod` d == 0 && y `mod` d == 0 = False 
--  | otherwise = sonCoprimosAux x y (d+1) 

--sonCoprimos :: Int -> Int -> Bool
--sonCoprimos x y = sonCoprimosAux x y 2

--Punto 17

--Punto 18
--uso contarDigitos ya previamente hecho

iesimoDigito :: Int -> Int -> Int
iesimoDigito n 0 = mod n 10
iesimoDigito n i = iesimoDigito (div n 10) (i-1) 

mayorDigitoPar :: Int -> Int
mayorDigitoPar n | (n < 10 && mod n 2 == 0) = n
                 | (n < 10 && mod n 2 /= 0) = -1 
                 | (mod (iesimoDigito n ((contarDigitos n)- 1)) 2 == 0) = iesimoDigito n ((contarDigitos n)- 1)
                 | otherwise = mayorDigitoPar (mod n (10^((contarDigitos n)- 1)))


