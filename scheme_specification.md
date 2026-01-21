### Scheme Specification

This version of Scheme is not perfectly true to any official specification of the language. It is only a simplified version to reduce the work. However, the core concept and function will be kept. Most parts of this specification refer to (are copied from) https://insideempire.github.io/CS61A-Website-Archive/articles/scheme-spec/

#### Overview and Terminology

##### Expressions and Environments

Scheme works by evaluating **expressions** in **environments**. Every expression evaluates to a value. Some expressions are **self-evaluating**, which means they are both an expression and a value, and that it evaluates to itself.

A **frame** is a mapping from symbols (names) to values, as well as an optional parent frame. The current environment refers to the current frame, as well as a chain of parent frames up to the **global frame** (which has no parent). When looking up a symbol in an environment, Scheme first checks the current frame and returns the corresponding value if it exists. If it doesn't, it repeats this process on each subsequent parent frame, until either the symbol is found, or there are no more parent frames to check.

##### Atomic Expressions

There are several atomic or primitive expressions. Numbers, booleans, strings, and the empty list (nil) are all both atomic and self-evaluating. Symbols are atomic, but are not self-evaluating (they instead evaluate to a value that was previously bound to it in the environment).

##### Call Expressions

The Scheme expressions that are not atomic are called **combinations**, and consist of one or more subexpressions between parentheses. Most forms are evaluated as **call expressions**, which have three evaluation steps:

1. Evaluate the first subexpression (the operator), which must evaluate to a **procedure** (see below).
1. Evaluate the remaining subexpressions (the operands) in order.
1. Apply the procedure from step 1 to the evaluated operands (arguments) from step 2.

##### Special Forms

This part will be detailed below.

##### Symbolic Programming

Scheme's core data type is the list, built out of pairs as described below. Scheme code is actually built out of these lists. This means that the code (+ 1 2) is constructed as a list of the + symbol, the number 1, and the number 2, which is then evaluated as a call expression.

Since lists are normally evaluated as combinations, we need a special form to get the actual, unevaluated list. quote is a special form that takes a single operand expression and returns it, unevaluated. Therefore, (quote (+ 1 2)) returns the actual list of the symbol +, the number 1, and the number 2, rather than evaluating the expression to get the number 3. This also works for symbols. a is looked up in the current environment to get the corresponding value, while (quote a) evaluates to the literal symbol a.

Because quote is so commonly used in Scheme, the language has a shorthand way of writing it: just put a single quote in front of the expression you want to leave unevaluated. '(+ 1 2) and 'a are equivalent to (quote (+ 1 2)) and (quote a), respectively.

##### Miscellaneous

We only use lowercase characters.

#### Types of values

##### Numbers

We don't distinguish different number type. Instead, we use double type to present all numbers.

##### Booleans

There are two boolean values: #t and #f. Scheme booleans can be only input as their canonical #t or #f.

Any expression may be evaluated in a boolean context, but #f is the only value that is false. All other values are treated as true in a boolean context.

##### Symbols

Symbols are used as identifiers in Scheme. Valid symbols consist of some combination of alphanumeric characters. Name of built-in special forms and functions will be excluded.

##### Strings

There's no strings in our version.

##### Procedures

Procedures represent some subroutine within a Scheme program. Procedures are first-class in Scheme, meaning that they can be bound to names and passed around just like any other Scheme value. Procedures are equivalent to functions in most other languages, and the two terms are sometimes used interchangeably.

This part will be detailed below.

##### Undefines

Finally, there is also an undefined value that can be returned by some builtin procedures. This value behaves similarly to None in Python. If an expression entered into the REPL evaluates to undefined, it is not printed, just like Python.

#### Special Forms

In all of the syntax definitions below, <x> refers to a required element x that can vary, while [x] refers to an optional element x. Ellipses indicate that there can be more than one of the preceding element.

##### define

> (define \<name\> \<expression\>)

Evaluates <expression> and binds the value to <name> in the current environment. <name> must be a valid Scheme symbol.

> (define (\<name\> [param] ...) \<body\> ...)

Constructs a new lambda procedure with params as its parameters and the body expressions as its body and binds it to name in the current environment. name must be a valid Scheme symbol. Each param must be a unique valid Scheme symbol. This shortcut is equivalent to:

> (define \<name\> (lambda ([param] ...) \<body\> ...))

The return value is the symbol <name>

Example:

> scm> (define x 2)
> x
> scm> (define (f x) x)
> f

##### if

> (if \<predicate\> \<consequent\> [alternative])

Evaluates predicate. If true, the consequent is evaluated and returned. Otherwise, the alternative, if it exists, is evaluated and returned (if no alternative is present in this case, the return value is undefined).

Example:

> (define nums '(1 2 3))
> (if (null? nums) 0 (length nums))

##### cond

> (cond \<clause\> ...)

The clause corresponds to expressions of the form

> (\<test\> [expression] ...)

Alternatively, clause can be written as

> (else [expression] ...)

Starts with the first clause. Evaluates test. If true, evaluate the expressions in order, returning the last one. If there are none, return what test evaluated to instead. If test is false, proceed to the next clause. If there are no more clauses, the return value is undefined. Clauses of the form (else [expression] ...) are equivalent to (#t [expression] ...).

Example: This code returns -1 for negative numbers, 1 for positive numbers, and 0 for zeros.

> (define n -3)
> (cond
>   &nbsp;&nbsp;((< n 0) -1)
>   &nbsp;&nbsp;((> n 0) 1)
>   &nbsp;&nbsp;(else 0)
> )

##### and

> (and [test] ...)

Evaluate the tests in order, returning the first false value. If no test is false, return the last test. If no arguments are provided, return #t.

##### or 

> (or [test] ...)

Evaluate the tests in order, returning the first true value. If no test is true and there are no more tests left, return #f.

##### begin

> (begin \<expression\> ...)

Evaluates each expression in order in the current environment, returning the evaluated last one.

##### lambda

> (lambda ([param] ...) \<body\> ...)

Creates a new lambda with params as its parameters and the body expressions as its body. When the procedure created by this form is called, the call frame will extend the environment this lambda was defined in.

##### quote

> (quote \<expression\>)

Alternatively,

> '\<expression\>


Returns the literal expression without evaluating it.

##### quasiquote

> (quasiquote \<expression\>)

Alternatively,

> `\<expression\>

Returns the literal expression without evaluating it, unless a subexpression of expression is of the form:

> (unquote \<expr2\>)

in which case that expr2 is evaluated and replaces the above form in the otherwise unevaluated expression.

##### unquote
> (unquote \<expr2\>)

Alternatively,

> ,\<expr2\>

#### Built-in Procedure

##### display

> (display \<val\>)

Prints val. 

A newline will not be automatically included.

##### displayln

> (displayln \<val\>)

Like display, but includes a newline at the end.

##### eval

> (eval \<expression\>)

Evaluates expression in the current environment

##### exit

> (exit)

Exits the interpreter. In the web interpreter, this does nothing.

##### atom?
> (atom? \<arg\>)

Returns true if arg is a boolean, number, symbol, string, or nil; false otherwise.

##### boolean?

> (boolean? \<arg\>)

Returns true if arg is a boolean; false otherwise.

##### num?

> (num? \<arg\>)

Returns true if arg is a integer; false otherwise.

##### list?

> (list? \<arg\>)

Returns true if arg is a well-formed list (i.e., it doesn't contain a stream); false otherwise. If the list has a cycle, this may cause an error or infinite loop.

Example:

> scm> (list? '(1 2 3))
> #t
> scm> (list? (cons-stream 1 nil))
> #f

##### number?

> (number? \<arg\>)

Returns true if arg is a number; false otherwise.

##### null?

> (null? \<arg\>)

Returns true if arg is nil (the empty list); false otherwise.

##### pair?

> (pair? \<arg\>)

Returns true if arg is a pair; false otherwise.

##### procedure?

> (procedure? \<arg\>)

Returns true if arg is a procedure; false otherwise.

##### symbol?

> (symbol? \<arg\>)

Returns true if arg is a symbol; false otherwise.

##### append

> (append [lst] ...)

Returns the result of appending the items of all lsts in order into a single list. Returns nil if no lsts.

Example:

> scm> (append '(1 2 3) '(4 5 6))
> (1 2 3 4 5 6)
> scm> (append)
> ()
> scm> (append '(1 2 3) '(a b c) '(foo bar baz))
> (1 2 3 a b c foo bar baz)
> scm> (append '(1 2 3) 4)
> Error

#####  car
> (car <pair>)

Returns the car of pair. Errors if pair is not a pair.

##### cdr

> (cdr <pair>)

Returns the cdr of pair. Errors if pair is not a pair.

##### cons

> (cons <first> <rest>)

Returns a new pair with first as the car and rest as the cdr

##### length

> (length <arg>)

Returns the length of arg. If arg is not a list, this will cause an error.

##### list

> (list <item> ...)

Returns a list with the items in order as its elements.

##### map

> (map <proc> <lst>)

Returns a list constructed by calling proc (a one-argument procedure) on each item in lst.

##### filter

> (filter <pred> <lst>)

Returns a list consisting of only the elements of lst that return true when called on pred (a one-argument procedure).

##### +

> (+ [num] ...)

Returns the sum of all nums. Returns 0 if there are none. If any num is not a number, this will error.

##### -

> (- <num> ...)

If there is only one num, return its negation. Otherwise, return the first num minus the sum of the remaining nums. If any num is not a number, this will error.

##### *

> (* [num] ...)

Returns the product of all nums. Returns 1 if there are none. If any num is not a number, this will error.

##### /

> (/ <dividend> [divisor] ...)

If there are no divisors, return 1 divided by dividend. Otherwise, return dividend divided by the product of the divisors. This built-in does true division, not floor division. dividend and all divisors must be numbers.

Example:

> scm> (/ 4)
> 0.25
> scm> (/ 7 2)
> 3.5
> scm> (/ 16 2 2 2)
> 2

##### abs

> (abs <num>)

Returns the absolute value of num, which must be a number.


##### quotient

> (quotient <dividend> <divisor>)

Returns dividend integer divided by divisor. Both must be numbers.

Example:

> scm> (quotient 7 3)
> 2

##### remainder

> (remainder <dividend> <divisor>)

Returns the remainder that results when dividend is integer divided by divisor. Both must be numbers. Differs from modulo in behavior when negative numbers are involved.

Example:

> scm> (remainder 7 3)
> 1
> scm> (remainder -7 3)
> -1