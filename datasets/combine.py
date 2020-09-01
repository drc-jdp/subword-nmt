import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python combine <input_Folder> <outputfile> [need_to_combine_size]")
        sys.exit()
    outfile = open(sys.argv[2], 'w', encoding='utf-8')
    if len(sys.argv) == 4:
        max_count = int(sys.argv[3])
    else:
        max_count = 0
    count = 0
    for (dirpath, _, filenames) in os.walk(sys.argv[1]):
        for file in filenames:
            if count >= max_count and max_count > 0:
                break
            infile = open( os.path.join(dirpath, file), 'r', encoding='utf-8' )
            outfile.write( infile.read() )
            outfile.write( '<|endoftext|>' )
            count += 1