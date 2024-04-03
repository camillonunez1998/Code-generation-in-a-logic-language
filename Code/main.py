import nodes as nds
import code_generator as cg
import input_output as io

#Write the path of the Latex file below
path='/Users/camilonunez/Desktop/Arbol.tex'
tree=io.Latex_to_string(path)
content=cg.semantics(cg.ontology(cg.types(cg.parameters(tree),tree),tree),tree)
io.coq_file(content,path)