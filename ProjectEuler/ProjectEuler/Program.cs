using System;
using System.Diagnostics;
using SolutionAlgorithms;

namespace ProjectEuler
{
    class Program
    {
        static void Main(string[] args)
        {
            Stopwatch stopwatch = Stopwatch.StartNew();
            Problem3 prob3 = new Problem3();
            prob3.SolveProblem(false, false);
            stopwatch.Stop();
            Console.WriteLine(stopwatch.Elapsed);
            Console.ReadKey();
        }
    }
}
