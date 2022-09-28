// readline lê a entrada até a quebra de linha
using System;
using System.Globalization;

namespace Proj1 {
        class Proj1 {
            public static void Main(string[] args)
            {
                string? frase = Console.ReadLine();
                string? x = Console.ReadLine();
                string? y = Console.ReadLine();
                string? z = Console.ReadLine();
                
                System.Console.WriteLine("\nVocê digitou: ");
                System.Console.WriteLine(frase);
                System.Console.WriteLine(x);
                System.Console.WriteLine(y);
                System.Console.WriteLine(z);

                // string? s = Console.ReadLine();
                string[] vet = Console.ReadLine().Split(' '); //split separa com o caractere e guarda em cada pedaço do vetor
                string a = vet[0];
                string b = vet[1];
                string c = vet[2];    

                int n1 = int.Parse(Console.ReadLine()); // faz a conversão de string para int, ja que o CR só lê strings
                char ch = char.Parse(Console.ReadLine());
                double n2 = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

                string[] pessoa = Console.ReadLine().Split(' ');
                string nome = pessoa[0];
                char sexo = char.Parse(vet[1]);
                int idade = int.Parse(vet[2]);
                

                System.Console.WriteLine(n1);
                System.Console.WriteLine(ch);
                System.Console.WriteLine(n2.ToString("F2", CultureInfo.InvariantCulture));

                System.Console.WriteLine(nome);
                System.Console.WriteLine(sexo);
                System.Console.WriteLine(idade);

                int a2 = 10;

                bool c1 = a2 < 10;
                bool c2 = a2 < 20;
                bool c3 = a2 > 10; //false
                bool c4 = a2 > 5; //True

                bool c5 = a2 <= 10;
                bool c6 = a2 >= 10;
                bool c7 = a2 == 10;
                bool c8 = a2 != 10;

                System.Console.WriteLine(c1); // falso (False)
                System.Console.WriteLine(c2); //verdadeiro (True)
                System.Console.WriteLine(c3);
                System.Console.WriteLine(c4);

                System.Console.WriteLine("-----------------");

                System.Console.WriteLine(c5);
                System.Console.WriteLine(c6);
                System.Console.WriteLine(c7);
                System.Console.WriteLine(c8);



            }

        }

}
