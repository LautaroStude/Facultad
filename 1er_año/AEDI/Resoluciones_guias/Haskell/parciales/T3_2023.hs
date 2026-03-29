type Formulas = [(String, String)]
type Presidente = String
type Votos = [Integer]
type CantTotalVotos = Integer

votosEnBlanco :: Formulas -> Votos -> CantTotalVotos -> Integer
votosEnBlanco as bs c = c - (sumaLista bs)  

sumaLista :: [Integer] -> Integer
sumaLista [] = 0
sumaLista (x:xs) = x + sumaLista xs

formulasValidas :: Formulas -> Bool
formulasValidas [] = True
formulasValidas [(a, b)] = a /= b
formulasValidas ((a, b):resto) = 
  a /= b && noEstaEn a resto && noEstaEn b resto && formulasValidas resto

noEstaEn :: String -> Formulas -> Bool
noEstaEn _ [] = True
noEstaEn nombre ((x, y):xs) = 
  nombre /= x && nombre /= y && noEstaEn nombre xs

porcentajeDeVotos :: Presidente -> Formulas -> Votos -> Float
porcentajeDeVotos n [] [] = 0
porcentajeDeVotos n cs ds = division (iesimoDigito ds (porcentajeDeVotosAux 1 n cs)) (sumaLista ds)

porcentajeDeVotosAux :: Integer -> Presidente -> Formulas -> Integer
porcentajeDeVotosAux comienzo as (x:[]) = comienzo
porcentajeDeVotosAux comienzo as ((b, c):ds) 
    | as == b = comienzo
    | otherwise = porcentajeDeVotosAux (comienzo + 1) as ds

iesimoDigito :: [Integer] -> Integer -> Integer
iesimoDigito (x:xs) 1 = x
iesimoDigito (x:xs) cuanto_moverme = iesimoDigito xs (cuanto_moverme - 1)

division :: Integer -> Integer -> Float
division a b = (fromIntegral a) / (fromIntegral b)

proximoPresidente :: Formulas -> Votos -> Presidente
proximoPresidente cs xs = iesimaTuplaFst cs (maximoPos xs 1) 

maximoPos :: [Integer] -> Integer -> Integer
maximoPos (x:[]) comienzo = comienzo
maximoPos (x:y:xs) comienzo 
    | x > y = maximoPos (x:xs) comienzo   
    | otherwise = maximoPos (y:xs) (comienzo + 1)

iesimaTuplaFst :: Formulas -> Integer -> String 
iesimaTuplaFst ((a, b):xs) 1 = a
iesimaTuplaFst ((a, b):xs) final = iesimaTuplaFst xs (final - 1)