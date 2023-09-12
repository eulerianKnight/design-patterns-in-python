# Builder Design Pattern

- Some objects are simple and can be created in a single initializer call.
- Other objects require a lot of ceremony to create.
- Having an object with 10 initializer arguments is not productive.
- Instead, opt for piecewise construction.
- Builder provides an API for constructing an object step-by-step
- Builder: When piecewise object construction is complicated, provide an API for doing it succinctly.

### Builder Facets

- Sometimes we might have an object which is so complicated that we need multiple builders.
- How can we get several builders participate in one object.