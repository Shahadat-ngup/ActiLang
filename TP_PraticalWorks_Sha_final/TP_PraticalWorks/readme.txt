UseCaseDG to PlantUML Translator
===============================

How to Use:
1. Run: `python test.py`
2. Copy the PlantUML output to https://plantuml.com/use-case-diagram

Description of the files:
1. lexer.py: Contains the token definitions for the UseCaseDG language
2. parser.py: Implements the parser and PlantUML generation functions
3. testX.py: Test files demonstrating different features of UseCaseDG

Test File Demonstrations:
------------------------

test1.py:
- Shows basic syntax with individual declarations
- Each actor and use case is declared separately
- Example:
actor User
actor Admin as A
usecase "Login" by User
usecase "Manage Users" as MU by Admin


test2.py:
- Demonstrates the concise list syntax
- Avoids repetition by declaring multiple items at once
- Example:
actor_list: Customer, Support as S, Manager as M inherits Admin
usecase_list: "Place Order", "Track Order" as TO by Customer



test3.py:
- Contains intentional syntax errors for validation testing
- Shows how the parser handles various error cases:
- Undeclared actors
- Invalid relationships
- Missing use case references
- Malformed declarations

Key Features Demonstrated:
- test1: Basic syntax and individual declarations
- test2: Compact list syntax and inheritance
- test3: Error handling and validation

The test files progress from basic to advanced usage, showing both the verbose and concise syntax options, followed by error case handling.