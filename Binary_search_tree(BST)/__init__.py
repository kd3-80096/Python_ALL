## searching and inserting in the binary search tree



class binary_search_tree:
    ## Initializing the left,right and root nodes with none values
    def __init__(self,num):
        self.left = None
        self.right = None
        self.val = num


## Method defination for insertion in BST

def insert_BST(root,num):
    ## checking if the root node is null
    if root == None:
        return binary_search_tree(num)
    ## checking for the duplicates in the root node
    else:
        if root.val == num:
            return root

        elif root.val < num:
            root.right = insert_BST(root.right,num)
        else:
            root.left = insert_BST(root.left,num)

        return root


##  Inorder traversal method defination

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)

## for searching the number in the BST

def search_BST(root,num):
    while root != None:
        if root.val < num:
            return search_BST(root.right,num)
        elif root.val > num:
            return search_BST(root.left,num)
        else:
            return True
    return  False

r = binary_search_tree(50)
r = insert_BST(r,30)
r = insert_BST(r,20)
r = insert_BST(r,40)
r = insert_BST(r,70)
r = insert_BST(r,60)
r = insert_BST(r,80)

print(search_BST(r,70))

inorder(r)



