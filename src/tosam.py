import argparse


def main():
    argparser = argparse.ArgumentParser(description="To Simple-SAM converter")
    argparser.add_argument(
        "mas",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()
    # print(args)
    for line in args.mas:
        chrom, read_name, read_str, pos = line.split('\t')
        # Output as Simple-SAM
        new_pos = int(pos)+1
        cigar = str(len(read_str))+'M'
        print(read_name, chrom, str(new_pos), cigar, read_str, sep='\t')


if __name__ == '__main__':
    main()
