# Repository Roles

PraxFlow does not require a fixed repository layout. It only needs public-contract ownership and product composition to be unambiguous.

Typical roles in a multi-repository product are:

## System / product repository

Owns product-level coordination such as subsystem boundaries, cross-repository change records, and integrated verification evidence when the project uses a dedicated system repository.

## Protocol / contract repository

Owns shared communication semantics or another public contract consumed by multiple repositories.

## PC / application repository

Owns application internals. It consumes shared public contracts instead of redefining them.

## Controller / firmware repository

Owns controller internals and consumes shared public contracts instead of redefining them.

## Module repository

Owns one independently versioned module and its internal behavior.

## Hardware repository

Owns hardware design sources and hardware-specific verification when separated from firmware/module ownership.

## Manifest / product-composition repository

Owns the set of repositories and immutable released revision combinations.

## Existing projects

These names are examples, not required names. If an existing project uses different repositories or ownership boundaries, preserve them. PraxFlow should discover and record the actual owner/consumer relationship rather than reorganizing the product.
