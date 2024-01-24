// See https://aka.ms/new-console-template for more information
// Console.WriteLine("Hello, World!");
using System;
using System.Collections.Generic;

class Program
{
    static List<string> FizzBuzz(int num)
    {
        List<string> arr = new List<string>();
        for (int i = 1; i <= num; i++)
        {
            if (i % 3 == 0 && i % 5 == 0)
            {
                arr.Add("FizzBuzz");
            }
            else if (i % 5 == 0)
            {
                arr.Add("Buzz");
            }
            else if (i % 3 == 0)
            {
                arr.Add("Fizz");
            }
            else
            {
                arr.Add(i.ToString());
            }
        }
        return arr;
    }

    static void Main()
    {
        List<string> result = FizzBuzz(15);
        foreach (var item in result)
        {
            Console.WriteLine(item);
        }
    }
}
