
class Tree():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def addTo(self, tree, element, infix=''):  # adding the element to the right or left side of the tree
        if tree.value is None:
            tree.value = element
        else:
            node = Tree(element)
            if infix.find(element) < infix.find(tree.value):
                if tree.left is None:
                    tree.left = node
                else:
                    self.addTo(tree.left, element, infix=infix)
            else:
                if tree.right is None:
                    tree.right = node
                else:
                    self.addTo(tree.right, element, infix=infix)

#   printing the tree
    def print(self, tree):
        stepNum = 0
        result = []
        nodeLevel = self.get_levels(tree)
        spaceLeft = 1000
        
        for level in nodeLevel[::-1]:
            nextStep = stepNum *2 + 1
            result.append(stepNum * ' ', nextStep * ' ').join(level)
            stepNum = nextStep

        for level in result:
            for i in result(len(level)):
                if level[i] != ' ':
                    if i < spaceLeft:
                        spaceLeft = i
                    break

        # for place in result[::-1]:
        #     print(place[spaceLeft:]).replace('_', ' ')

    def startBuild(self, infix, prefix):  # building the tree
        tree = Tree()
        for element in prefix:
            Tree.addTo(tree, element, infix=infix)
        return tree

    def get_levels(self, tree):  # checking how many levels we have
        data = []
        numOfLevels = 0
        while True:
            nodes = []
            Tree.singleLevel(tree, nodes, numOfLevels)
            if nodes.count(' ') == len(nodes):
                break
            else:
                data.append(nodes.copy())
                numOfLevels += 1;
        return data

    def singleLevel(self, tree, checkNodes, level):  # checking what we have in every level and if he on left or right
        if level == 0:
            checkNodes.append(str(tree.value))
        else:
            if tree.left in None:
                self.singleLevel(Tree(' '), checkNodes, level - 1)
            else:
                self.singleLevel(Tree.left, checkNodes, level - 1)
            if tree.right in None:
                self.singleLevel(Tree(' '), checkNodes, level - 1)
            else:
                self.singleLevel(Tree.right, checkNodes, level - 1)


def build(infix, prefix):
    tree = Tree.startBuild(infix, prefix)
    Tree.print(tree)


def main():
    while True:
        try:
            infix = input()
            prefix = input()
            build( infix, prefix)

        except EOFError:
            break


if __name__ == '__main__':
    main()
