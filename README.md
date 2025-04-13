# ActiLang  
*A Domain-Specific Language (DSL) for Activity Diagrams*  
**Author**: Shahadat Hossain  

## Overview  
ActiLang is a custom language designed to simplify the creation of activity diagrams. It translates human-readable syntax into PlantUML code, enabling:  
✔ **Concise syntax** for workflows  
✔ **Validation** of diagram logic  
✔ **Flexible output** compatible with PlantUML  

Built with Python and PLY (Lex/Yacc), it supports:  
- Actions, decisions, and parallel flows  
- Swimlanes (actors/partitions)  
- Error handling and syntax checks  

## Features  
| Feature       | Example Syntax          | 
|---------------|-------------------------|
| **Actions**   | `do "Process Order"`    |
| **Decisions** | `if "Payment OK?"`      |
| **Loops**     | `repeat "Retry 3x"`     |
| **Swimlanes** | `actor "Customer"`      |

## Note that, there is also a readme inside the main project folder that explains how to use the language.

## Installation  
```bash
git clone https://github.com/shahadat/ActiLang.git
cd ActiLang
pip install ply

 

