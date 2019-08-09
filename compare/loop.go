package main

import "fmt"
import "time" 

func main() {
   //fmt.Println("Hello, World!")
   start := time.Now()
   // Code to measure
   duration := time.Since(start)

   for a := 0; a < 10000000000; a++ {
      //fmt.Printf("value of a: %d\n", a)
   }
   fmt.Println(duration)
}
