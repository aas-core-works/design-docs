# Code Contracts

The specification of [operations] in our [meta-model] should include the [code contracts] such as pre-conditions and post-conditions.

[operations]: data-structures-and-operations.md
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

TODO (Marko & Nico & Robert, 2021-03-28): Discuss

The contracts are written in [our simplified Python] and transpiled by [code generators] into the implementation stubs.

[our simplified Python]: simplified-python.md

As we could **not support invariants** in most languages, we decide to define contracts as **pre-conditions** and **post-conditions** of **[operations]**.

The contracts are defined as [function decorators] on the opeartions:

[function decorators]: https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators

```python
@require(
    condition=lambda x, y: x < y,
    identifier="x_smaller_than_y",
    error=lambda x, y: "x (%d) must be smaller than y (%d)." % (x, y),
    severity=ALWAYS)
@ensure(
    condition=lambda x, y, result: result > x * y,
    identifier="result_greater_than_product",
    error=lambda x, y, result: 
        ("result (%d) must be greater than the product (%d)"
        "of x (%d) and y (%d)") % (result, x * y, x, y) 
)
def some_operation(x: int, y: int) -> int:
    ...
```

The contract decorators (`require` and `ensure`) as well as constants (such as `ALWAYS`) live in `aasx_core_gen.contracts` module.

### Identifier

Each contract must have an identifier unique to the operation.
In implementation languages where we can not produce an error message, we will at least display the identifier to the user.

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
