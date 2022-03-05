# IMPORT JULIA
from julia.api import Julia
jpath = "/usr/bin/julia" # path to Julia, from current directory (your path may be slightly different)
jl = Julia(runtime=jpath, compiled_modules=False) # compiled_modules=True may work for you; it didn't for me

from julia import Main

Main.include("script.jl")
#jl_output = jl.eval("test_julia(1)")
#print(jl_output)
