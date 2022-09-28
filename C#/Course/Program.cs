using System;
using System.Globalization;

namespace Course {
    class Program {
        static void Main(string[] args) {

            bool completo = false;
            char genero = 'F';
            char letra = '\u0041'; //código unicode
            byte n1 = 126;
            int n2 = 1000;
            int n3 = 213213123;
            long n4 = 21374836248L;
            float n5 = 4.5f;
            double n6 = 4.5;
            string nome = "Maggie May";
            sbyte nx = sbyte.MinValue;
            decimal nz = decimal.MaxValue;
            double saldo = 10.434332;
            
            //casting
            double a1;
            float b1;
            a1 = 5.1;
            b1 = (float)a1; //int(a)

            int a22 = 5;
            int b33 = 2;
            double resultado1 = (double) a22 / b33; // descarta as casas decimais sem o (double) ->> fazer casting

            // bhaskara

            double a = 1.0, b = -3.0, c = -4.0;
            double delta = Math.Pow(b, 2.0) -4.0 * a * c; //mathpow utilizada p calcular potenciação
            double x1 = (-b + Math.Sqrt(delta)) / (2.0 * a);


            Console.WriteLine(completo);
            System.Console.WriteLine(letra);
            System.Console.WriteLine(genero);
            Console.WriteLine(n1);
            Console.WriteLine(n2);
            Console.WriteLine(n3);
            Console.WriteLine(n4);
            System.Console.WriteLine(n5);
            System.Console.WriteLine(n6);
            System.Console.WriteLine(nome);
            System.Console.WriteLine(nx);
            System.Console.WriteLine(nz);
            System.Console.WriteLine("\n\n");

            System.Console.WriteLine("Teste");
            System.Console.Write("Bom dia");    // write não pula linha. wrileline pula
            System.Console.WriteLine("Teste1");

            System.Console.WriteLine("-----------------\n");

            System.Console.WriteLine(saldo.ToString("F2")); // F2 - 2 casas decimais; F3 - 3 casas...
            System.Console.WriteLine(saldo.ToString("F4"));
            System.Console.WriteLine(saldo.ToString("F4", CultureInfo.InvariantCulture)); // desconsidera qqr formatacao específica de qqr país

            // nome e genero
            //placeholder
            System.Console.WriteLine("{0} é do sexo {1}.", nome, genero);

            //interpolação - mais recente e melhor, na minha opinião
            System.Console.WriteLine($"{nome} é do sexo {genero}. A ração dela custa R$ {saldo:F2}.");

            //Concatenação - mais antigo
            System.Console.WriteLine(nome + " é do sexo " + genero + ". A ração dela custa R$ " + (saldo.ToString("F2", CultureInfo.InvariantCulture)));

            System.Console.WriteLine(b1);
            System.Console.WriteLine(resultado1);
        } 
    }

}