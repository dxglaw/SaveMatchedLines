import sys
import re

def save_matched_lines(in_file, tag, out_file=None):
    '''
    Match lines in in_file with tag and write matched lines to out_file.
    Args:
        Input:
            in_file: input file
            tag: tag
            out_file: output file
    '''
    # generate output file name
    if out_file is None:
        for ii in range(len(in_file)-1, -1, -1):
            if in_file[ii] == '.':
                break
        if ii != 0:
            out_file = in_file[0:ii] + '_out' + in_file[ii::]
        else:
            out_file = in_file + '_out'
    # save matched lines to output file
    with open(in_file, 'r') as fin:
        in_contents = fin.read()
        matched = re.findall('^'+tag+'.*$', in_contents, re.M)
        with open(out_file, 'w') as fout:
            fout.write("\n".join(matched))

if __name__ == "__main__":
    num_of_args = len(sys.argv)
    if num_of_args > 1:
        in_file = sys.argv[1]
        if num_of_args > 2:
            tag = sys.argv[2]
        else:
            tag = input('Please input the tag: ')
        if num_of_args > 3:
            out_file = sys.argv[3]
        else:
            out_file = None
    else:
        in_file = 'test.csv'
        tag = 'pps'
        out_file = 'out.csv'
    save_matched_lines(in_file, tag, out_file)
