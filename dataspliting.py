import splitfolders
def process(path):
    
    input_folder=path
    splitfolders.ratio(input_folder,output="dataset2",seed=42,ratio=(.8,.2),group_prefix=None)
#splitfolders.fixed(input_folder,output="dataset2",seed=42,fixed=(100,100),oversample-false,group_prefix=None)
    
process("./data")
