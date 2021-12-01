using System;
using System.Linq;

/*
*/


namespace Day1{
    class Day1{

        static int totalCount = 0;
        static void Main(string[] args)
        {
            var answer = SolvePartOne();
        }

        static int SolvePartOne(){
            var listOfInts = File.ReadAllLines("input.txt")
            .Select(s => Int32.Parse(s))
            .ToList();
            for (int i = 0; i < listOfInts.Count - 1; i++)
            {
                if (listOfInts[i+1] > listOfInts[i])
                {
                    totalCount++;
                }
            }
            return totalCount;
        }
    }
}