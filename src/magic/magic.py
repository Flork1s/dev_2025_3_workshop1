class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """

        if n == 0:
            return 0 
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        a = 0
        b = 1
        i = 1

        while i < n:
            suma = a + b
            a = b
            b = suma
            i += 1
        return suma
        
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        fibonacciLista = []

        if n <= 0:
            return fibonacciLista
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        fibonacciLista = [0, 1]

        # Generar la secuencia
        for i in range(2, n):
            siguiente = fibonacciLista[-1] + fibonacciLista[-2]
            fibonacciLista.append(siguiente)

        return fibonacciLista

    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        i = 2

        if n <= 1:
            return False

        while i < n:
            if n % i == 0:
                return False
            i += 1
        return True
            


    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
        listaPrimos = []
        i = 2

        while i <= n:
            aux = 2
            es_primo = True

            while aux < i:
                if i % aux == 0:
                    es_primo = False
                    break 
                aux += 1

            if es_primo:
                listaPrimos.append(i)

            i += 1
        return listaPrimos

                
            
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        i = 1
        suma = 0

        if n <= 1:
            return False
        while i < n:
            if n % i == 0:
                suma += i
            i += 1
        return suma == n
            
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        triangulo = []

        for i in range(filas):
            fila = [1] * (i + 1)
            for j in range(1, i):
                fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]

            triangulo.append(fila)

        return triangulo
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        factorial = 1

        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            while n != 0:
                factorial *= n
                n -= 1
        return factorial
            
    
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        if a < 0:
            a = -a
        if b < 0:
            b = -b

        while b != 0:
            a, b = b, a % b
        return a
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        def mcd(x, y):
            while y != 0:
                x, y = y, x % y
            return abs(x)
        return abs(a*b) // mcd(a, b)

    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        if n < 0:
            n = -n
        suma = 0 
        while n > 0:
            suma += n% 10 
            n //= 10 
        return suma
    
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        if n < 0:
            n = -n
        digitos = [int(d) for d in str(n)]
        num_digitos = len(digitos)
        suma = sum(d ** num_digitos for d in digitos)
        return suma == n
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        n = len(matriz)

        if not all(len(fila) == n for fila in matriz):
            return False 
        
        suma_objetivo = sum(matriz[0])

        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False 
            
        for col in range(n):
            suma_columna  = sum (matriz[fila][col] for fila in range(n))
            if suma_columna != suma_objetivo:
                return False
        
        suma_diag1 = sum(matriz[i][i] for i in range(n))
        if suma_diag1 != suma_objetivo:
            return False
        
        suma_diag2 = sum(matriz[i][n - 1 - i] for i in range(n))
        if suma_diag2 != suma_objetivo:
            return False

        return True