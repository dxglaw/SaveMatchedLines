import sys
import re

def save_matched_lines(in_file, tag, out_file=None, remove_tag=False):
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
    with open(in_file, 'r', encoding='utf-8') as fin:
        in_contents = fin.read()
        # handle special characters in the tag
        specail_ch = ['^', '$', '*', '+', '?']
        for ch in specail_ch:
            if ch in tag:
                tag = tag.replace(ch, '\\'+ch)
        # match the tag
        matched = re.findall('^'+tag+'.*$', in_contents, re.M)
        out_contents = "\n".join(matched)
        if remove_tag:
            out_contents = out_contents.replace(tag, '')
        # write to the output file
        with open(out_file, 'w', encoding='utf-8') as fout:
            fout.write(out_contents)

if __name__ == "__main__":
    # default input
    in_file = 'test.csv'
    tag = 'pps,'
    out_file = 'out.csv'
    remove_tag = False
    # args
    num_of_args = len(sys.argv)
    if num_of_args > 1:
        in_file = sys.argv[1]
        if num_of_args > 2:
            tag = sys.argv[2]
        else:
            tag = input('Please input the tag (add a trailing space not to output tag): ')
            # if the trailing character is space, do not inlude tag in the output file.
            if tag[-1] == ' ':
                remove_tag = True
                tag = tag[:-1]
        if num_of_args > 3:
            out_file = sys.argv[3]
        else:
            out_file = None
    save_matched_lines(in_file, tag, out_file, remove_tag)
