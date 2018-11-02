using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace SolutionAlgorithms
{


    //A Pythagorean triplet is a set of three natural numbers, a < b<c, for which,
    //a2 + b2 = c2
    //For example, 32 + 42 = 9 + 16 = 25 = 52.
    //There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    //Find the product abc.


    //Solved in 0.0193025 seconds!
    //O(N^2)
    public class Problem9 : IProblem
    {
        public Problem9()
        {
        }

        public void SolveProblem(bool debuggingMode, bool smallTest)
        {
            BigInteger endValue = 1000;

            if (debuggingMode)
                DebuggingMode(endValue);
            else
                NonDebuggingMode(endValue);
        }
        private void NonDebuggingMode(BigInteger endValue)                                                    //O(N^2)
        {
            BigInteger maxAValue = endValue / 3 - 2;                //O(1)
            for (BigInteger a = 1; a < maxAValue; a++)                 //O(N)
            {
                BigInteger maxBValue = maxAValue * 2;
                for (BigInteger b = a + 1; b < maxBValue; b++)          //O(N)
                {
                    BigInteger c = endValue - b - a;
                    BigInteger firstPart = (a * a + b * b);
                    BigInteger secondPart = c * c;
                    if (firstPart == secondPart)
                    {
                        Console.WriteLine("FOUND ANSWER: {0}, {1}, {2}", a, b, c);
                        Console.WriteLine("Final answer is: {0} ", a * b * c);
                        return;
                    }
                }
            }
        }

        private void DebuggingMode(BigInteger endValue)             
        {
            BigInteger maxAValue = endValue / 3 - 2;                
            for (BigInteger a = 1; a < maxAValue; a++)                
            {
                BigInteger maxBValue = maxAValue * 2;
                for (BigInteger b = a + 1; b < maxBValue; b++)          
                {
                    BigInteger c = endValue - b - a;
                    Console.WriteLine("check: {0}, {1}, {2}", a, b, c);
                    BigInteger firstPart = (a * a + b * b);
                    BigInteger secondPart = c * c;
                    if ( firstPart == secondPart)
                    {
                        Console.WriteLine("FOUND ANSWER: {0}, {1}, {2}", a, b, c);
                        Console.WriteLine("Final answer is: {0} ", a*b*c);
                        return;
                    }
                }
            }
        }
    }
}
