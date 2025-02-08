class Node:
    def __init__(self, letter = "", value = 0, left = None, right = None):
        self.letter = letter
        self.value = value
        self.left = left
        self.right = right

def make_tree(plain_text):
    nodes_list = []
    letters_set = set(plain_text)
    nodes_list = [Node(letter, plain_text.count(letter)) for letter in letters_set]
    nodes_list.sort(key=lambda el: el.value)
    while len(nodes_list) > 1:
        first = nodes_list.pop(0)
        second = nodes_list.pop(0)
        new_node = Node("", first.value + second.value, first, second)
        nodes_list.append(new_node)
        nodes_list.sort(key=lambda el: el.value)

    return nodes_list[0]

def make_codes(tree, codes, path):
    if tree.left is None and tree.right is None:
        codes[tree.letter] = path
        return

    if tree.left is not None:
        make_codes(tree.left, codes, path + '0')

    if tree.right is not None:
        make_codes(tree.right, codes, path + '1')

def compress(plain_text, codes):
    result = ''
    for letter in plain_text:
        result += codes[letter]

    return result

def decompress(compressed_txt, tree):
    result = ''
    curr_node = tree
    for bit in compressed_txt:
        if bit == '0':
            curr_node = curr_node.left
        elif bit == '1':
            curr_node = curr_node.right

        if curr_node.left is None and curr_node.right is None:
            result += curr_node.letter
            curr_node = tree
    return result

txt = 'miau'
tr = make_tree(txt)
code = dict()
make_codes(tr, code, '')

compr_txt = compress(txt, code)

print(f'Compressed plain text: {compress(txt, code)}')
print(f'Decompressed compressed text: {decompress(compr_txt, tr)}')