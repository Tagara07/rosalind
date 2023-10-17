def read_data(data_path):
    '''
    singe sequence
    '''
    with open(data_path, 'r') as f:
        seq = f.read()
        f.close()
    return seq

def gen_txt(result):
    '''
    generate result to txt
    '''
    f = open('output.txt', 'w')
    f.write(result)
    f.close()

