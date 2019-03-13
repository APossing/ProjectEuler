using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SolutionAlgorithms
{
    public interface IProblem
    {
        void SolveProblem(bool debuggingMode, bool smallTest);
    }
}
