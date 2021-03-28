# Data Structures and Operations

TODO (Marko & Nico & Robert, 2021-03-28): Discuss

We specify the data structures and operations using [our simplified Python].
Based on this specification, we generate the data structures and operation stubs in the respective implementations of the library (see [general design decisions]).

[our simplified Python]: simplified-python.md
[general design decisions]: general-design-decisions.md 

## Bootstrapping 

We provide a bootstrapping script that converts the "official" [RDF schema] into [our simplified Python].

Since schema changes rarely, we will use [diff] to keep our data structures and operations in sync with the "official" [RDF schema]. 

[RDF schema]: https://en.wikipedia.org/wiki/RDF_Schema
[diff]: https://en.wikipedia.org/wiki/Diff

## Operation scripting

Many operations, such as simple add/remove commands, are trivial to script and transpile into the implementation.
For such operations, we script them in [our simplified Python] directly in the meta-model.
Thus their code is automatically generated, and needs not to be written manually in the implementations.

The complex operations which cannot be scripted are marked with [include markers].

[include markers]: simplified-python.md#include-markers

## State

We define the state of the objects by using [dataclasses].
Both private and public state is defined, if possible.
This makes the debugging and reading the implementation code across the implementation languages easier, as the reader is already familiar with the names.

Private properties are marked with an underscore prefix (`_some_private_property`).

If we can not meaningfully define some properties (*e.g.*, since it uses a specialized data structure), we write [include markers] as placeholders.
The developer needs to define them manually in a separate code snippet written in the corresponding implementation language.

## Contracts

Contracts are defined along the operations with [function decorators].
Please see the document [Contracts] for more information.

[function decorators]: https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators
[Contracts]: contracts.md
