relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True  
relacionesValidas ((a, b):cs)
  | a == b = False  
  | pertenece (a, b) cs = False 
  | otherwise = relacionesValidas cs
                              
pertenece :: (String, String) -> [(String, String)] -> Bool
pertenece (a, b) [] = False
pertenece (a, b) ((c, d):zs) 
    | (a == c && b == d) = True
    | otherwise = pertenece (a, b) zs

personas :: [(String, String)] -> [String]
personas [] = []
personas [(a, b)] = [a, b]
personas ((a, b):cs) = eliminarRepetidos ([a, b] ++ personas cs)

eliminarRepetidosAux :: [String] -> String -> [String]
eliminarRepetidosAux [] nombre = []
eliminarRepetidosAux (x:xs) nombre 
    | x == nombre = eliminarRepetidosAux xs nombre
    | otherwise = x : eliminarRepetidosAux xs nombre

eliminarRepetidos :: [String] -> [String]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x : (eliminarRepetidos (eliminarRepetidosAux xs x))

amigosDe :: String -> [(String, String)] -> [String]
amigosDe n [] = []
amigosDe n ((a, b):xs) 
    | n == a = b : amigosDe n xs
    | n == b = a : amigosDe n xs
    | otherwise = amigosDe n xs

longitud :: [String] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

--personaConMasAmigos :: [(String, String)] -> String
--personaConMasAmigos (x:y:[]) 
--    | ((longitud (amigosDe x)) > (longitud (amigosDe y))) = fst x
--    | otherwise = fst y 
--personaConMasAmigos (x:y:xs) 
--    | ((longitud (amigosDe x)) > (longitud (amigosDe y))) = personaConMasAmigos (x:xs)
--    | otherwise = personaConMasAmigos (y:xs)