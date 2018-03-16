######################################################################################
# Name: Animal Game
# Authors: Tradd Schmidt and Rusty Dotson
# Purpose: To try to have the computer guess the user's animal
#
######################################################################################
nl = None
wl = []


class BstNode:
    def __init__(self, data, type):
        self.data = data
        self.left = None
        self.right = None
        self.type = type


def GetNewNode(data, type):
    """
    Creates a new node with a data and a type
    :param data: What will be the data of the node
    :param type: Whether the node is a guess or a question
    :return: the node that was created
    """
    newNode = BstNode(data, type)
    return newNode


def write_file(name_of_file):
    """
    Writes the questions and guesses to a file
    :param name_of_file: the name of the file that is being written to
    :return: None
    """
    global wl
    try:
        open_file = open(name_of_file, "w")
        for i in wl:
            open_file.write(i + "\n")
        open_file.close()
    except IOError:
        print("File does not exist! Try again.")


def parse_file(words_file_name):
    """
    Parses a text file line by line and adds it to a list to be returned
    :param words_file_name: The file that will be parsed
    :return: The lines of the text file minus the first line
    """
    text = []
    try:
        open_file = open(words_file_name, 'r')
        contents = open_file.readline()
        contents = contents[:-1]
        while contents:
            text.append(contents)
            contents = open_file.readline()
            contents = contents[:-1]
        open_file.close()
    except IOError:
        print("File does not exist! Try again.")
    return text


def text_to_nodes(l):
    """
    Takes in a list of nodes in string for and creates a new list containing the nodes
    :param l: the nodes in string format
    :return: a list of nodes
    """
    nodes = []
    head = GetNewNode(l[1], "Question")
    nodes.append(head)
    a = 1
    for i in l[1:]:
        if i == "Question:":
            temp_node = GetNewNode(l[a + 1], "Question")
            nodes.append(temp_node)
        elif i == "Guess:":
            temp_node = GetNewNode(l[a + 1], "Guess")
            nodes.append(temp_node)
        else:
            pass
        a += 1
    return nodes


def nodes_to_tree():
    """
    Creates a tree using nodes
    :return: None
    """
    global nl
    if nl[0].type == "Guess":
        item = nl.pop(0)
        item.left = None
        item.right = None
    elif nl[0].type == "Question":
        item = nl.pop(0)
        item.left = nl[0]
        nodes_to_tree()
        item.right = nl[0]
        nodes_to_tree()


def game(head):
    """
    Traverses the tree based on the input of the user and updates the tree if needed
    :param head: the head of the tree
    :return: a string indicating whether the user wants to keep playing
    """
    again = True
    if head == None:
        return

    ans = input(head.data)
    if head.type == "Guess":
        if ans == "no":
            correct_animal = input("What is the correct answer?")
            new_question = input("Please provide a question to differentiate between your animal and the animal I guessed.")
            temp = head.data            # This code updates the tree
            head.data = new_question
            head.type = "Question"
            head.left = BstNode(temp, "Guess")
            head.right = BstNode(correct_animal, "Guess")
            again = input("Do you want to play again")
        elif ans == "yes":
            again = input("We guessed it! Do you want to play again?")

    elif ans == "no":
        again = game(head.left)
    elif ans == "yes":
        again = game(head.right)
    return again


def preorder(head):
    """
    Traverses the tree and appends the nodes data and type to a list that will be used to write to a file
    :param head: the head of the tree
    :return: None
    """
    global wl
    if head == None:
        return
    wl.append(head.type + ":")
    wl.append(head.data)
    preorder(head.left)
    preorder(head.right)


def main():
    global nl
    global wl
    again = True
    text = parse_file("Animal Game.txt")
    nl = text_to_nodes(text)
    head = nl[0]
    nodes_to_tree()
    while again:
        again = game(head)
        if again == "yes":
            again = True
        else:
            again = False
    preorder(head)
    write_file("Animal Game.txt")

main()
