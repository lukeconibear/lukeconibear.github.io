# Rust

## Resources

- [Book: The Rust Programming Language](https://doc.rust-lang.org/book/title-page.html)
- [Exercises: Rustlings](https://rustlings.cool/)
- [Videos: From Python to Rust](https://youtube.com/playlist?list=PLEIv4NBmh-GsWGE9mY3sF9c5lgh5Z_jLr&si=_LiA31caoUJvowTQ)
- [Rust Language Cheat Sheet](https://cheats.rs/)
- [The stack and the heap](https://web.mit.edu/rust-lang_v1.25/arch/amd64_ubuntu1404/share/doc/rust/html/book/first-edition/the-stack-and-the-heap.html)
- [Videos: Jon Gjengset](https://www.youtube.com/@jonhoo)
- [Book: Rust for Rustaceans by Jon Gjengset](https://rust-for-rustaceans.com/)
- [Book: Effective Rust](https://www.lurklurk.org/effective-rust/)
- [Book: Rust Design patterns](https://rust-unofficial.github.io/patterns/)
- [Book: Rust Performance](https://nnethercote.github.io/perf-book/introduction.html)
- [Book: Rust API Guidelines](https://rust-lang.github.io/api-guidelines/)
- [Rust course from Google](https://google.github.io/comprehensive-rust/)

## Organisation

```bash
- Cargo.lock
- Cargo.toml
- src
  - lib.rs (normal code, unit tests, and run function)
  - main.rs (calls run function)
- tests
  - integration_test.rs (for run function from lib.rs)
```

## Python extensions

- Make Rust modules for Python bottlenecks
    - https://github.com/PyO3/pyo3
    - https://github.com/PyO3/maturin

## Arrays

- https://github.com/PyO3/rust-numpy
- https://github.com/rust-ndarray/ndarray
- Pre-allocate memory in Python before using rust calls

## Multi-threading

- https://github.com/rayon-rs/rayon
- `par_bridge().try_for_each` enables error from one of threads to be propagated back e.g., for columns
- `par_azip` is similar for arrays

## Error handling

- https://github.com/dtolnay/anyhow
- https://github.com/dtolnay/thiserror
- Pattern match range of Rust errors to Python ones, so these are returned to the Python user

## Cloud

- Read cloud files
    - https://github.com/apache/arrow-rs (`object_store`)
    - Also
        - https://github.com/CarlKCarlK/cloud-file

## Format

- https://github.com/rust-lang/rustfmt

## Lint

- https://github.com/rust-lang/rust-clippy

## Profile

- https://github.com/cmyr/cargo-instruments

## Benchmark

- https://github.com/bheisler/criterion.rs

## Logging

- ‣https://github.com/rust-lang/log

## JSON

- https://github.com/serde-rs/serde

## async

- https://github.com/tokio-rs/tokio

## Docs

- [rustdoc](https://doc.rust-lang.org/rustdoc/index.html)
- `#![warn(missing_docs)]`
- all public stuff
- create simple examples
- `#![doc = include_str!("../README.md")]`
- `cargo doc --no-deps --open`
- good example: [bed_reader - Rust (docs.rs)](https://docs.rs/bed-reader/latest/bed_reader/)

## Database

- https://github.com/rusqlite/rusqlite
- https://github.com/launchbadge/sqlx
- https://github.com/sfackler/rust-postgres

## Builder pattern for keyword arguments

- https://github.com/idanarye/rust-typed-builder
- Also
    - https://github.com/colin-kiegel/rust-derive-builder

## Plotting

- https://github.com/plotters-rs/plotters

## Concatenating strings

```rust
    let s1 = String::from("tic");
    let s2 = String::from("tac");
    let s3 = String::from("toe");

    let s = format!("{s1}-{s2}-{s3}");
```

## Using an Enum to Store Multiple Types

```rust
use std::collections::HashMap;
use std::hash::Hash;

#[derive(Debug, Eq, PartialEq, Hash)]
enum Keys {
    Int(i32),
    Text(String),
}

#[derive(Debug)]
#[allow(dead_code)]
enum SpreadsheetCell {
    Int(i32),
    Float(f64),
    Text(String),
}

fn main() {
    let mut scores = HashMap::new();

    scores.insert(Keys::Text(String::from("Blue")), 10);
    scores.insert(Keys::Text(String::from("Yellow")), 50);
    scores.insert(Keys::Int(42), 30);

    println!("{:#?}", scores);

    let row = vec![
        SpreadsheetCell::Int(3),
        SpreadsheetCell::Text(String::from("blue")),
        SpreadsheetCell::Float(10.12),
    ];

    println!("{:#?}", row);
}
```
