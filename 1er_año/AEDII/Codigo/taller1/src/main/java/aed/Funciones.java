package aed;

import javax.swing.plaf.TreeUI;

class Funciones {

/***  Primera parte: Funciones en java ***/

    int cuadrado(int x) {
        return x * x;
    }

    double distancia(double x, double y) {
        return Math.sqrt((x * x)+(y * y));
    }

    boolean esPar(int n) {
        return (n % 2) == 0;
    }

    boolean esBisiesto(int n) {
        return ((((n % 4) == 0) && ((n % 100) != 0)) || ((n % 400) == 0));
    }

    int factorialIterativo(int n) {

        int res = 1;
        for (int i = 1; i <= n; i++) {
            res = res * i;
        }
        return res;
    }

    int factorialRecursivo(int n) {
        int res;

        if (n == 0) {
            res = 1;
        } else {
            res = n * factorialRecursivo(n - 1);
        }
        return res;
    }

    boolean esPrimo(int n) {

        int divisores = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                divisores += 1;
            }
        }

        return divisores == 2;
    }

    int sumatoria(int[] numeros) {
        int res = 0;
        for (int i = 0; i < numeros.length; i++) {
            res = res + numeros[i];
        }
        return res;
    }

    int busqueda(int[] numeros, int buscado) {
        int res = 0; //verificar porque si no lo encuentra como se que es el 0
        for (int i = 0; i < numeros.length; i++) {
            if (numeros[i] == buscado) {
                res = i;
            }
        }
        return res;
    }

    boolean tienePrimo(int[] numeros) {
        boolean res = false;
        for (int i = 0; i < numeros.length; i++) {
            if (esPrimo(numeros[i])) {
                res = true;
            }
        }

        return res;
    }

    boolean todosPares(int[] numeros) {
        boolean res = true;
        for (int i = 0; i < numeros.length; i++) {
            if (numeros[i] % 2 != 0 && res) {
                res = false;
            }
        }
        return res;
    }

    boolean esPrefijo(String s1, String s2) {
        boolean res = false;
        String palabra = "";
        
       
        for (int i = 0; i < s1.length() && s1.length() <= s2.length(); i++) {
            char letra = s2.charAt(i); 
            palabra = palabra + letra; 
        }
        
        if (palabra.equals(s1)){
            res = true;
        }
        return res;
    }

    boolean esSufijo(String s1, String s2) {
        boolean res = false;
        String palabra = "";
        
        for (int i = 0; i < s1.length() && s1.length() <= s2.length(); i++) {
            
            int posicion = s2.length() - s1.length() + i; 
            
            char letra = s2.charAt(posicion); 
            palabra = palabra + letra; 
        }
        
        if (palabra.equals(s1)){
            res = true;
        }
        return res;
    }

/***  Segunda parte: Debugging ***/

    boolean xor(boolean a, boolean b) {
        return (a || b) && !(a && b);
    }

    boolean iguales(int[] xs, int[] ys) {
        boolean res = true;
        if (xs.length != ys.length) {
            res = false;
        }

        for (int i = 0; i < xs.length && res; i++) {
            if (xs[i] != ys[i]) {
                res = false;
            }
        }
        return res;
    }

    boolean ordenado(int[] xs) {
        boolean res = true;
        for (int i = 0; i < xs.length - 1; i++) {
            if (xs[i] > xs [i+1]) {
                res = false;
            }
        }
        return res;
    }

    int maximo(int[] xs) {
        int res = xs[0];
        for (int i = 0; i < xs.length; i++) {
            if (xs[i] > res) {
                res = xs[i];
            }
        }
        return res;
    }

    boolean todosPositivos(int[] xs) {
        boolean res = true;
        for (int i = 0; i < xs.length && res; i++) {
            if (xs[i] <= 0) {
                res = false;
            }
        }
        return res;
    }

}
