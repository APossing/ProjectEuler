using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace SolutionAlgorithms
{
    //O(N^2) 
    //Solves in 5.6 seconds
    public class Problem3 : IProblem
    {
        private List<BigInteger> _primeFactors;

        public Problem3()
        {
            _primeFactors = new List<BigInteger>();
        }

        public void SolveProblem(bool debuggingMode, bool smallTest)
        {
            BigInteger bigInt;
            if (smallTest)
                bigInt = new BigInteger(13195);
            else
                bigInt = new BigInteger(600851475143);

            if (debuggingMode)
                DebuggingMode(bigInt);
            else
                NonDebuggingMode(bigInt);
            PrintAnswer();
        }
        private void NonDebuggingMode(BigInteger value)                                                    //O(N^2)
        {
            BigInteger halfVal = value / 2 + 1;
            if (halfVal % 2 == 0)
                halfVal++;
            for (BigInteger i = 2; i < halfVal; i++)                                                       //O(N)
            {
                if (value % i == 0)                                                                        //O(1)
                {
                    BigInteger bigSideOfFactor = value / i;                                                //O(1)
                    if (IsPrime(bigSideOfFactor))                                                          //O(N)
                    {
                        Console.WriteLine("BiggestPrimeFactor of {1}: {0}", bigSideOfFactor, value);       //O(1)
                        return;
                    }
                }
            }
        }
        private void DebuggingMode(BigInteger value)
        {
            BigInteger halfVal = value / 2 + 1;
            if (halfVal % 2 == 0)
                halfVal++;
            for (BigInteger i = 2; i < halfVal; i++)
            {
                if (value % i == 0)
                {
                    BigInteger bigSideOfFactor = value / i;
                    Console.WriteLine("Current Factor: {0}", i);
                    if (IsPrime(bigSideOfFactor))
                    {
                        Console.WriteLine("FOUNNDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD: {0}", bigSideOfFactor);
                        return;
                    }
                }
            }
        }

        private void PrintAnswer()
        {
            Console.WriteLine("Prime Factors are :");
            foreach (var cur in _primeFactors)
            {
                Console.Write("{0}, ", cur);
            }

        }
        private bool IsPrime(BigInteger value)              //O(N)
        {
            if (value % 2 == 0)                             //O(1)
                return false;
            BigInteger halfVal = value / 2 + 1;
            for (BigInteger i = 3; i < halfVal; i += 2)     //O(N)
            {
                if (value % i == 0)                         //O(1)
                    return false;
            }

            return true;
        }
    }
}
