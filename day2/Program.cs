using System;
using System.Linq;

/* 
/ Connor Abernethy
/ 12/2/2021
/ Advent of Code 2021
*/


namespace Day2{
    class Day2{
        static int horizontalPosition, depth, aim = 0;
        static void Main(string[] args)
        {
            var list = File.ReadAllLines("input.txt").ToList();
            SolvePartOne(list);
            ResetPositions();
            SolvePartTwo(list);
        }

        static void SolvePartOne(List<string> list){
            for (int i = 0; i < list.Count; i++){
                if (list[i].Contains("forward")){
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
            Console.WriteLine("Part One Answer: " + (depth * horizontalPosition));
        }

        static void SolvePartTwo(List<string> list){
            for (int i = 0; i < list.Count; i++){
                if (list[i].Contains("forward")){
                    var forward = Int32.Parse(list[i].ElementAt(list[i].Length - 1).ToString());
                    horizontalPosition += forward;
                    depth += (aim * forward);
                }
                else if (list[i].Contains("up")){
                    var up = Int32.Parse(list[i].ElementAt(list[i].Length - 1).ToString());
                    aim -= up;
                }
                else{
                    var down = Int32.Parse(list[i].ElementAt(list[i].Length - 1).ToString());
                    aim += down;
                }
            }
            Console.WriteLine("Part Two Answer: " + (depth * horizontalPosition));
        }

        static void ResetPositions(){
            horizontalPosition = 0;
            depth = 0;
            aim = 0;
        }
    }
}