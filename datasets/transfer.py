import regex as re
from functools import lru_cache

import argparse
parser = argparse.ArgumentParser(
    description='Pre-encode text files into tokenized training set.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('in_text', metavar='PATH', type=str, help='Input file, directory, or glob pattern (utf-8 text).')
parser.add_argument('out_npz', metavar='OUT.npz', type=str, help='Output file path')

@lru_cache()
def bytes_to_unicode():
    """
    Returns list of utf-8 byte and a corresponding list of unicode strings.
    The reversible bpe codes work on unicode strings.
    This means you need a large # of unicode characters in your vocab if you want to avoid UNKs.
    When you're at something like a 10B token dataset you end up needing around 5K for decent coverage.
    This is a signficant percentage of your normal, say, 32K bpe vocab.
    To avoid that, we want lookup tables between utf-8 bytes and unicode strings.
    And avoids mapping to whitespace/control characters the bpe code barfs on.
    """
    bs = list(range(ord("!"), ord("~")+1))+list(range(ord("¡"), ord("¬")+1))+list(range(ord("®"), ord("ÿ")+1))
    cs = bs[:]
    n = 0
    for b in range(2**8):
        if b not in bs:
            bs.append(b)
            cs.append(2**8+n)
            n += 1
    cs = [chr(n) for n in cs]
    return dict(zip(bs, cs))


def encode(text, outfile):
    pat = re.compile(r"""'s|'t|'re|'ve|'m|'ll|'d| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+""")
    byte_encoder = bytes_to_unicode()
    bpe_tokens = []
    for token in re.findall(pat, text):
        print(token)
        token = ''.join(byte_encoder[b] for b in token.encode('utf-8'))
        print(token)
        outfile.write(token)
           

if __name__ == "__main__":
    args = parser.parse_args()
    infile = open( args.in_text, 'r', encoding="utf-8")
    outfile = open( args.out_npz, 'w', encoding="utf-8")
    text = infile.read()
    encode( text , outfile ) 
