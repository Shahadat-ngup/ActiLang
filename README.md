# UseCaseDG  
*A Domain-Specific Language (DSL) for Use Case Diagrams*  
**Author**: Shahadat Hossain  

## Overview  
UseCaseDG is a custom language designed to simplify the creation of **use case diagrams**. It translates human-readable syntax into PlantUML code, enabling:  
✔ **Declarative syntax** for actors and use cases  
✔ **Relationship validation** (extends/includes/inherits)  
✔ **Structured organization** with systems and packages  

Built with Python and PLY (Lex/Yacc), it supports:  
- Actor declarations with aliases and inheritance  
- Use cases with optional actor associations  
- System boundaries and package grouping  
- Syntax error detection  

## Features  
| Feature              | Example Syntax                     | Description |
|----------------------|------------------------------------|-------------|
| **Actors**           | `actor "Customer"`<br>`actor "Admin" as ADM` | Basic actor or with alias |
| **Use Cases**        | `usecase "Place Order"`<br>`usecase "Login" as UC1 by "User"` | Standalone or actor-linked |
| **Relationships**    | `ext "Login" of "Recovery"`<br>`inc "Checkout" in "Payment"` | Extension/Inclusion links |
| **Inheritance**      | `actor "VIP" inherits "Customer"`  | Actor hierarchy |
| **System Scope**     | `system "E-Commerce" { ... }`      | Boundary container |
| **Packages**         | `package "Security" { "Login", "Logout" }` | Logical grouping |


## Note that, there is also a readme inside the main project folder that explains how to use the language.

## Installation  
```bash
git clone https://github.com/shahadat/ActiLang.git
cd ActiLang
pip install ply

 

