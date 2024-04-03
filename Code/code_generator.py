import nodes as nds

#Retruns the line of parameters
def parameters(tree):
    code='''(* Types for constructing the ontology *)\n\nParameters ('''
    #Typing the parameters
    indicator=True
    for char in tree:
        if char!='[' and char!=']':
            code+=char
            indicator=True
        elif indicator==True:
            code+=' '
            indicator=False
    code+=': Prop)'
    return code

#Taking the depth of the tree
def maxim(tree):
    compt=-1
    maxim=-1
    for char in tree:
        if char=='[':
            compt+=1
        if compt>maxim:
            maxim=compt
        if char==']':
            compt-=1
    return maxim

#(* Types for concodeucting the ontology *)
def types(code,tree):
    filiation=nds.nodes(tree)
    for parent in filiation:
        for child in filiation[parent]:
            code+='\n\t('+child+'_is_'+parent+' : '+child+' -> '+parent+')'
    code+='.'
    return(code)

#(* Ontology specification *) 
def ontology(code,tree):
    code+='\n\n\n\n(* Ontology specification *)\n'
    filiation=nds.nodes(tree)
    for parent in filiation:
        for child in filiation[parent]:
            code+='\nCoercion '+child+'_is_'+parent+' : '+child+' >-> '+parent+'.'
    return(code)

#(* Semantics corresponding to the ontology *)
def semantics(code,tree):
    code+='\n\n\n\n(* Semantics corresponding to the ontology *)\n\n'
    filiation=nds.nodes(tree)
    for parent in filiation:
        bl=True #Indicator
        for parent1 in filiation:
            if parent in filiation[parent1]:
                bl=False
        if bl==True:
            code+='Parameter is_'+parent+' : Prop.\n'
    for parent in filiation:
        for child in filiation[parent]:
            code+= 'Parameter is_'+child+' : '+parent+' -> Prop.\n'
    return code