# Roadmap

The short-term goals (say April/May 2020) are:

* Focus at first only on interfaces.
* Only generate stubs together with contracts.
* Support `Identifiable` and a minimal support for nesting.
    * `Submodel`, `SubmodelElementCollection`, `SubmodelElement` and `Property` 
* Support file objects and blobs

## Priority of Supported Languages

* C#, so that the library can be already used by, say, [aasx-server].
* Python, so that we test how it works with a slightly different paradigm.
* Java, so that enterprise people can use it.
* C++, so that embedded people can use it.
* C, so that even "niche" embedded people can use it.
* Golang, so that "server" people can use it.
* IEC611311, so that machine developers can use it.
* Erlang, so that "network" people can use it.
* Rust, for the people who use it as an alternative to C/C++.

[aasx-server]: https://github.com/admin-shell-io/aasx-server
