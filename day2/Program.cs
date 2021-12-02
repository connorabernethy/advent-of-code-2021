using System;
using System.Linq;

/* 
/ Connor Abernethy
/ 12/2/2021
/ Advent of Code 2021
*/


namespace Day2{
    class Day2{
        static int horizontalPosition, depth = 0;
        static void Main(string[] args)
        {
            var list = File.ReadAllLines("input.txt").ToList();
            for (int i = 0; i < list.Count; i++){
                if (list[i].Contains("forward")){
                    // Get the last digit at the end of the string.
                    var forward = Int32.Parse(list[i].ElementAt(list[i].Length - 1).ToString());
                    horizontalPosition += forward;
                }
                else if (list[i].Contains("up")){
                    var up = Int32.Parse(list[i].ElementAt(list[i].Length - 1).ToString());
                    depth -= up;
                }
                else{
                    var down = Int32.Parse(list[i].ElementAt(list[i].Length - 1).ToString());
                    depth += down;
                }
            }

            Console.WriteLine("Answer: " + (depth * horizontalPosition));
        }
    }
}