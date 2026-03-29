package aed;

class Funciones {

/***  Primera parte: Funciones en java ***/

    int cuadrado(int x) {
        // COMPLETAR
        return x * x;
    }

    double distancia(double x, double y) {
        // COMPLETA
        double res = Math.sqrt(x * x + y * y);
        return res;
    }

    boolean esPar(int n) {
        // COMPLETAR
        return n % 2 == 0;
    }

    boolean esBisiesto(int n) {
        // COMPLETAR
        
        return (n % 4 == 0 && n % 100 != 0) || n % 400 == 0;
    }

    int factorialIterativo(int n) {
        // COMPLETAR
        int res = 1;
        for (int i = 1; i <= n; i++) {
            res = res * i;
        }
    return res;
    }

    int factorialRecursivo(int n) {
        // COMPLETAR
                int res = 0;
        if (n > 0) {
            res = n * factorialIterativo(n - 1);
        }
        else {
            res = 1;
        }
        return res;
    }

    boolean esPrimo(int n) {
        // COMPLETAR
        int divisores = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                divisores += 1;
            }
        }

        return divisores == 2;
    }

    int sumatoria(int[] numeros) {
        // COMPLETAR
        int res = 0;
        int longitud_lista = numeros.length;
        for (int i = 0; i < longitud_lista; i++) {
            res = res + numeros[i];
        }
        return res;
    }

    int busqueda(int[] numeros, int buscado) {
        // COMPLETAR
        int res = 0;
        int longitud_lista = numeros.length;
        for (int i = 0; i < longitud_lista; i++) {
            if (numeros[i] == buscado) {
                res = i;
            }
        }
        return res;
    }

    boolean tienePrimo(int[] numeros) {
        // COMPLETAR
        boolean res = false;
        int longitud_lista = numeros.length;
        for (int i = 0; i < longitud_lista; i++) {
            if (esPrimo(numeros[i]) && !res) {
                res = true;
            }
        }
        return res;
    }

    boolean todosPares(int[] numeros) {
        // COMPLETAR
        boolean res = true;
        int longitud_lista = numeros.length;
        for (int i = 0; i < longitud_lista; i++) {
            if (numeros[i] % 2 != 0 && res) {
                res = false;
            } 
        }
        return res;
    }

    boolean esPrefijo(String s1, String s2) {
        // COMPLETAR
        return false;
    }

    boolean esSufijo(String s1, String s2) {
        // COMPLETAR
        return false;
    }

/***  Segunda parte: Debugging ***/

    boolean xor(boolean a, boolean b) {
        return a || b && !(a && b);
    }

    boolean iguales(int[] xs, int[] ys) {
        boolean res = true;

        for (int i = 0; i < xs.length; i++) {
            if (xs[i] != ys[i]) {
                res = false;
            }
        }
        return res;
    }

    boolean ordenado(int[] xs) {
        boolean res = true;
        for (int i = 0; i < xs.length; i++) {
            if (xs[i] > xs [i+1]) {
                res = false;
            }
        }
        return res;
    }

    int maximo(int[] xs) {
        int res = 0;
        for (int i = 0; i <= xs.length; i++) {
            if (xs[i] > res) res = i;
        }
        return res;
    }

    boolean todosPositivos(int[] xs) {
        boolean res = false;
        for (int x : xs) {
            if (x > 0) {
                res = true;
            } else {
                res = false;
            }
        }
        return res;
    }

}
