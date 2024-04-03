#Returns the content of the Latex file as a list
def read_Latex_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.read().splitlines()
    return lines


#Transforms Latex document into a string (a tree) containing only the code of the tree without enviroments
def Latex_to_string(path):
    latex_filepath =path
    lines = read_Latex_file(latex_filepath)
    
    #Makes a string containing all the code of the tree ignoring irrelevant parts of the code
    i=0
    tree=''
    while(True):
        if lines[i]=='\\begin{forest}':
            i+=1
            while lines[i]!='\\end{forest}':
                line=lines[i].strip()
                index=0
                while index<len(line):
                    if line[index]=='[' or line[index]==']':
                        if index+1==len(line):
                            break
                        while line[index+1]==' ':
                            if index+1==len(line):
                                break
                            line=line[:index+1]+line[index+1:]
                    index+=1
                tree+=line
                i+=1
        if lines[i]=='\\end{forest}':
            break 
        i+=1
    #tree=tree.replace(' ','')
    tree=tree.replace('\n','')
    tree=tree.replace('\t','')
    tree=tree.replace('%','')
    return tree

#Returns the name of the output
def o_n(path):
    output_name='.v'
    path=path[:-4]
    for i in range(len(path)-1,-1,-1):
        if path[i]=='/':
            break
        output_name=''.join([path[i],output_name])
    return output_name

#Here we create the coq file with the code previously generated
def coq_file(coq_content,path):
    output_name=o_n(path)
    with open(output_name, 'w') as f:
        f.write(coq_content)
    coq_file_path =output_name

    # Return the file path or coq_content variable
    print("Coq file generated:", coq_file_path)