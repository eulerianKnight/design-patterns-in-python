# SOLID Design Principle

## 1. Single Responsibility Principle.

- Also known as "Separation of Concern",
- A Class should have a primary responsibility and should not take any other responsibility.
- A Class should have a single reason to change and the change should be related to its primary responsibility.

## 2. Open-Closed Principles

- Open for Extension, Closed for Modification.
- Once a class is tested, there should not be any modification but extension.
- Specification pattern can be used to follow this principle. Use a Base class which can be inherited(extended) for different use case.

## 3. Liskov Substitution Principle

- It states that objects of a superclass should be replaceable with objects of its subclasses without breaking the application.
- Violation of this can lead to unexpected outcomes.
- 
## 4. Interface Segregation Principle.

- Instead of an Interface with many methods it's better to have granularity, split interface in several parts.
- YAGNI - You Ain't Going to Need it.

## 5. Dependency Inversion Principle

- High Level classes or modules in code should not depend on low level classes or modules instead should depend on abstraction.
- USE ABSTRACTIONS.