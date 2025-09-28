package main

import "C"
import "fmt"

//export SayHello
func SayHello() {
	fmt.Println("Hello from Go!")
}

func main() {}
