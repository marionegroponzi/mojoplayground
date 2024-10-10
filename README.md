# Overview

Playground to try out [Mojo](https://www.modular.com/mojo)

# Overview

Tutorial code from [here](https://docs.modular.com/max/tutorials/magic).

# Build mojo files with

- `magic run build` => builds the file `local/zero.mojo` into `local/zero`

# Run with

- `magic run hello` => runs the hello world
- `magic run dev-server` => starts a fastapi server

# Check the fastapi server with

- `http://127.0.0.1:8000` => base entry point
- `http://127.0.0.1:8000/zero` => returns zero tensor, interpreted
- `http://127.0.0.1:8000/one` => returns zero tensor, compiled (requires building it first)

