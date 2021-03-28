# Simplified Python

We use a simplified version of Python as the universal language to be transpiled into the respective implementation languages (such as C#, Java *etc.*).
This simple Python supports only a certain subset of language constructs and built-in functions.
The language is used for defining [data structures and operations], [contracts] and [scripting de/serialization].

[data structures and operations]: data-structures-and-operations.md
[contracts]: contracts.md
[scripting de/serialization]: deserialization-scripts.md

As the scripts are not used by the wide audience, but only by the developers of the library, we intentionally decide on-the-go which Python features to support.
Hence we only transpile a very limited subset of builtin functions and types.

## Disallowed Features

We allow no:

* Nested functions,
* Context managers, and
* Custom intermediate classes (*e.g.*, classes which are not directly transpiled and used by the user such as [data structures])

[data structures]: data-structures-and-operations.md

## String Formatting

To facilitate the transpilation to languages such as C++ and Golang, we decide to use [old string formatting]:

```python
>>> '%s has %03d quote types.' % ("Python", 2))
'Python has 002 quote types.'
```

[old string formatting]: https://docs.python.org/3/library/stdtypes.html#old-string-formatting

## Supported Language Constructs

### For-loops

For-loops can loop either over lists, over maps or over `for _ in range(..., ...)` where both start and end are given as integers.

## Include Markers

Since we only provide a transpilation based on a subset of Python language, we will have to include manually defined code snippets at many spots.
The developer should mark such spots with [include markers] using `NotImplementedError`.

For example:

```
raise NotImplementedError('some-marker')
```

will make the [code generators] introduce an include marker `some-marker` in the generated code.
The [filler script] will eventually replace the [include markers] with the corresponding code snippets written in the implementation language.

[code generators]: general-design-decisions.md#code-generators
[include markers]: general-design-decisions.md#include-markers
[filler script]: general-design-decisions.md#filler-script
