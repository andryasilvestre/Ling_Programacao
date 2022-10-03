// readline lê a entrada até a quebra de linha
using System;

namespace Proj1 {
        class Proj1 {
            public static void Main(string[] args)
            {
                // string? frase = Console.ReadLine();
                // string? x = Console.ReadLine();
                // string? y = Console.ReadLine();
                // string? z = Console.ReadLine();
                
                // System.Console.WriteLine("Você digitou: ");
                // System.Console.WriteLine(frase);
                // System.Console.WriteLine(x);
                // System.Console.WriteLine(y);
                // System.Console.WriteLine(z);

                System.Console.WriteLine("Entre com um número inteiro");
                int x1 = int.Parse(Console.ReadLine());

                while (x1 > 0) {

                    if (x1 % 2 == 0) {
                        System.Console.WriteLine("Par!");
                        break;
                    }

                    else {
                        System.Console.WriteLine("Impar!");
                        break;
                        }                
                }
            }
        }

}
