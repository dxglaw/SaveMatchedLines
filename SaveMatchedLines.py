import re

def save_matched_lines(in_file, tag, out_file):
    '''
    Match lines in in_file with tag and write matched lines to out_file.
    Args:
        Input:
            in_file: input file
            tag: tag
            out_file: output file
    '''
    with open(in_file, 'r') as fin:
        in_contents = fin.read()
        matched = re.findall('^'+tag+'.*$', in_contents, re.M)
        with open(out_file, 'w') as fout:
            fout.write("\n".join(matched))

if __name__ == "__main__":
    in_file = 'test.csv'
    save_matched_lines(in_file, 'pps', 'out.csv')
