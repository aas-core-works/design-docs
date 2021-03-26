# Code Contracts

The specification of [operations] in our [meta-model] should include the [code contracts] such as pre-conditions and post-conditions.

[operations]: data-structures-and-operations.md#operations
[meta-model]: general-design-decisions.md#meta-model
[code contracts]: https://en.wikipedia.org/wiki/Design_by_contract
[SHACL]: https://www.w3.org/TR/shacl/

The contracts can be trivial (such as specifying a range of a property), as well as very complex expressions (the length of this list needs to be divisble by three and the first element needs to be larger than the sum of all the other elements).

The [code generators] transpile contracts so that they are **included in the implementation**.
This has the following benefits:
* The *implementation* of the library allows thus for **deeper testing** as contracts are checked during debuging, testing and in production.

* Additionally, the *implementation* can be analyzed with **static analyzers** and **automatic testers** (such as [crosshair] and [icontract-hypothesis]), which can only work with code with tight-enough contracts.

* The contracts are included in the **documentation of the implementation**.
  Hence the users can rely on formal unambiguous documentation.
  Moreover, the documentation in human language tends to "rot", while contracts are continuously and automatically verified in testing or in production.

[code generators]: general-design-decisions.md#code-generators
[crosshair]: https://github.com/pschanely/CrossHair
[icontract-hypothesis]: https://github.com/mristin/icontract-hypothesis

## Definition of Contracts

The contracts are written in [SHACL] and transpiled by [code generators] into the implementation stubs..

As we could **not support invariants** in most languages, we decide to define contracts as **pre-conditions** and **post-conditions** of **[operations]**.

Each contract should be given **a unique identifier**.

### Error Messages

The contracts should also include **an error message**.
The error message should support [printf format strings] so that we can include the actual offending values in the message as well.
This is important for contracts which are enforced **in production** catching **rare and hard-to-reproduce bugs**.

[printf format strings]: https://en.wikipedia.org/wiki/Printf_format_string

### Severity

Each contract is given a  **severity** which determines when it is enforced:

* `ALWAYS`, always enforced, including in production,
* `DEBUG`, enforced both in our and external tests, and
* `DEBUG_OURS`, enforced only in our tests, but excluded in external tests,
* `DEBUG_SLOW` and `DEBUG_OURS_SLOW`, enforced only in the respective tests for which we know that the amount data is small.<br>
  <br>
  This allows us to enforce contracts with exploding computational complexity.

For example, most post-conditions have the severity `DEBUG`.

## Contracts and Serialization

The contracts are a tool for improving the [correctness] of the code.
They are not meant to be used as validation of the input (*e.g.*, a JSON file to be imported).

[correctness]: https://en.wikipedia.org/wiki/Correctness_(computer_science)

In our setting, this means that the validation of the input is part of the [deserialization scripts].
 They need to check that the input is correct and conforms to the meta-model, and report the errors eventually to the user.
In contrast, the contracts give us a certain assurance that the de-serialized objects are **internally consistent** and conform to our meta-model.

In other words, the [deserialization scripts] verify the **external data**, while contracts verify the **internal data**.
For example, we can use contracts to ensure that our deserialization works.
Instead of writing tons of unit tests, we rely on the contracts to be verified during testing.
A test boils down to simply de-serializing the example JSONs.

[deserialization scripts]: deserialization-scripts.md
