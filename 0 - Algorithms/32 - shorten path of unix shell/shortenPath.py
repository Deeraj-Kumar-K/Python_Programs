# Shorten Path of Unix Shell

# Given a valid unix shell path string,
# Return a shortend version of that path string.
# String will be non-empty.
'''
Explanation:

Path represnts a location of a file or directory.
Path can be either absolute path or relative path.

-Absolute path: It starts with root directory i.e "/"
Example of Absolute Path is "/test/new/abc"

-Relative path: It starts with the directory where the user currently is in.
Example of Relative path is "folder/videos/test"
Ex: "../../folder/test" - here, we can't remove ".." from the path.

Ex: "a/b/c"
This example shows that directory 'c' is inside of 'b' which is inside 'a'.

".." - double dot represents the parent directory.
It means that we are going back to the parent directory.
Ex: "/doo/../test" --> this will result in "/test"
First we visited the directory 'doo', then ".." made us go back,
so we were in the root directory "/". Then "/test" made us go to "test".

Ex: "doo/car/.." --> this will shorten to "doo/"

Note: If we are in root directory ie. "/", we can't go back past this.
Using ".." will not make us go back of root directory.
Ex: "/../../../" ---> this will result in "/"

"." - single dot means current directory. We are not doing anything.
So we can remove them while shortening. Ex: "doo/././././car" --> "doo/car"

Multiple slashes doen't mean anything. Ex: "doo////car" ---> "doo/car"

Input : "/doo/../test/../test/../doo//car/./yes"
Output: "/doo/car/yes"
'''

# Time complexity: O(n) , Space complexity: O(n)
#where n is the length of path

def shortenPath(path):
    #first we check if given path is absolute or relative path
    startsWithSlash = path[0] == "/" #stores boolean value
    tokens = list(filter(isImportantToken, path.split('/'))) #O(n) time, O(n) space
    
    #path = "/doo/../test/../test/../doo//car/./yes"
    #path.split('/') gives ['', 'doo', '..', 'test', '..', 'test', '..', 'doo', '', 'car', '.', 'yes']
    #we filtered out slashes '/', single dots "." and empty string ""
    #tokens = ['doo', '..', 'test', '..', 'test', '..', 'doo', 'car', 'yes']
    
    stack = [] #O(n) space
    if startsWithSlash: #if absolute path, then we need "/" at the begining, so add empty string into stack
        stack.append("")
    for token in tokens: #O(n) time
        if token == "..":
            if len(stack) == 0 or stack[-1] == "..": #firstElement or prevElement ".." means relative path
                stack.append(token) # '-1' or len(stack)-1 represents top of stack
            #elif stack[-1] == "": #if only root directory is remaining, do nothing
            #    continue
            elif stack[len(stack) - 1] != "": #combining the conditions, if top of stack is not empty string
                stack.pop() #meaning that it is not root directory but some other directory, pop from stack
        else: #else we have some directory, so append it
            stack.append(token)
            
    if len(stack) == 1 and stack[0] == "": #if only one element is remaining in stack and it is empty string,
        return "/" #then manually return the root directory coz "/".join(stack) will return "" empty string
    #if there are two or more elements in the stack, "/".join(stack) will join all those elements with "/"
    return "/".join(stack) #O(n) time

def isImportantToken(token): #O(1) time
    #if token is not empty string i.e length > 0 and not equal to ".", then it is important, so return true
    return len(token) > 0 and token != "."


# Input
path = "/doo/../test/../test/../doo//car/./yes"
print("\nPath:",path)
print("\nOutput:", shortenPath(path))
#output: "/doo/car/yes"
