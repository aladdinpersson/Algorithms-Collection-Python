import heapq
from bitarray import bitarray

class Node(object):
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def make_frequency_dict(file="huffman.txt"):
    freq ={}
    text = ''

    with open(file) as f:
        for line in f:
            text += line

            for char in line:
                if not char in freq:
                    freq[char] = 0
                freq[char] += 1

    return freq, text

def make_heap(freq):
    heap = []
    for char in freq:
        node = Node(char, freq[char])
        heapq.heappush(heap, node)

    return heap

def build_tree(heap):
    # Create our binary tree

    while (len(heap) > 1):
        nodeL = heapq.heappop(heap)
        nodeR = heapq.heappop(heap)
        tot_freq = nodeL.freq+nodeR.freq

        heapq.heappush(heap, Node('', tot_freq, nodeL, nodeR))

    return heap


def create_mapping(root, map={}, binarytext=''):
    # Create a mapping from each character to a binary string

    if root == None:
        return

    if root.left == None and root.right == None:
        # if we are a leaf
        map[root.ch] = binarytext

    left = create_mapping(root.left, map, binarytext+'0')
    right = create_mapping(root.right, map, binarytext+'1')

    return map

def decode(binarystring, root):
    decoded_msg = ''
    curr_node = root

    i = 0

    while i <= len(binarystring):
        if curr_node.right == None and curr_node.left == None:
            decoded_msg += str(curr_node.ch)
            curr_node = root

            if i == len(binarystring): i += 1

        # If 1 walk right
        elif binarystring[i] == '1':
            curr_node = curr_node.right
            i += 1
        # If 0 walk left
        elif binarystring[i] == '0':
            curr_node = curr_node.left
            i += 1

    return decoded_msg

def main():
    freq, text = make_frequency_dict(file="Huffman.txt")
    #print(f"Our message that we wish to decompress using Huffman is: \n{text}")

    heap = make_heap(freq)
    tree = build_tree(heap)
    mapping = create_mapping(tree[0])

    print(f'Our mapping is: \n{mapping}')

    # Get encoded message
    encoded = ''

    for letter in text:
        encoded += mapping[letter]

    print(f'Our encoded message is: \n{encoded}')

    out = bitarray(encoded)

    with open('compressed_file.bin', 'wb') as f:
        out.tofile(f)

    #original_text = decode(encoded, tree[0])

if __name__ == '__main__':
    main()