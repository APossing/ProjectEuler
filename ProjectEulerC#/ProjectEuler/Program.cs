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

            //IProblem problem = new Problem3();
            //IProblem problem = new Problem9();

            problem.SolveProblem(false, false);
            stopwatch.Stop();
            Console.WriteLine(stopwatch.Elapsed);
            Console.ReadKey();
        }
    }
}
