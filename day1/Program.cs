using System;
using System.Linq;

/* 
/ Connor Abernethy
/ 12/1/2021
/ Advent of Code 2021
*/


namespace Day1{
    class Day1{

        static int totalCount = 0;
        static void Main(string[] args)
        {
            Console.WriteLine("Part One Answer: " + SolvePartOne());
            totalCount = 0;
            Console.WriteLine("Part Two Answer: " + SolvePartTwo());
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

        static int SolvePartTwo(){
            var listOfInts = File.ReadAllLines("input.txt")
            .Select(s => Int32.Parse(s))
            .ToList();

            var prevWindow = 0;

            for (int i = 0; i < listOfInts.Count - 2; i++){
                var window = listOfInts[i] + listOfInts[i+1] + listOfInts[i+2];
                if (window > prevWindow && prevWindow != 0)
                {
                    totalCount++;
                }
                prevWindow = window;
            }
            return totalCount;
        }
    }
}