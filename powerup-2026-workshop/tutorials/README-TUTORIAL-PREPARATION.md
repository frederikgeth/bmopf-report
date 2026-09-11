# Software and preparation requirements

## Tutorial `From High-Quality Data Models to High Fidelity Network Models`

This tutorial consists of a Jupyter notebook in the Julia language. While no prior knowledge of Julia is required, we do ask that the participants install the libraries and set-up their environment beforehand.

> **New to Julia?** For a step-by-step walkthrough with copy-paste commands for Linux, Windows and macOS, see [`SETUP.md`](From-High-Quality-Data-Models-to-High-Fidelity-Network-Models/SETUP.md). The notes below are a quick reference.

### Getting Julia 
This tutorial requires requires **Julia ≥ 1.10**. If you don't have Julia yet, install it with [juliaup](https://github.com/JuliaLang/juliaup), or via the
[Microsoft Store](https://apps.microsoft.com/detail/9NJNWW8PVKMN) (or
`winget install julia -s msstore`) on Windows, or via
`curl -fsSL https://install.julialang.org | sh` on macOS/Linux.

Alternatively, you can get an installer from
[julialang.org/downloads](https://julialang.org/downloads/).

### Working with Jupyter notebooks in Julia

This can be done via the `IJulia` package. Please check its [manual](https://ijulia.org/stable/).


### Packages required for the notebook

`BMOPFTools` is not yet in the General registry (Julia's default package
catalogue), so you have to install it from this Git URL:

```julia
using Pkg
Pkg.add(url = "https://github.com/frederikgeth/BMOPFTools.jl")
```

All the other packages (`JuMP`, `Ipopt` and `Plots`) are in the General registry so they can simply be added through their name:
```julia
using Pkg
Pkg.add("Ipopt")
```

Make sure these are installed in the same environment as the notebook.

## Demo `Multiconductor AC power flow in the browser with tellegen`

No installation. Bring a laptop with a current browser and download the two files in
[`Multiconductor-Power-Flow-in-the-Browser-with-tellegen`](Multiconductor-Power-Flow-in-the-Browser-with-tellegen/);
the README there lists the steps.
