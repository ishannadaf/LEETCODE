"""

71. Simplify Path
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory 
in a Unix-style file system, convert it to the simplified canonical path. 
In a Unix-style file system, a period '.' refers to the current directory, 
a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') 
are treated as a single slash '/'. For this problem, any other format of periods such as '...' 
are treated as file/directory names. 

The canonical path should have the following format:
- The path starts with a single slash '/'.
- Any two directories are separated by a single slash '/'.
- The path does not end with a trailing '/'.
- The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.

Example 1:
Input: path = "/home/"
Output: "/home"
Example 2:
Input: path = "/../"
Output: "/"
Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Example 4:
Input: path = "/a/./b/../../c/"
Output: "/c"


💡 Idea

Instead of using a stack directly, we:

Split the path
Repeatedly process "..", ".", and empty parts
Keep rebuilding the list until no changes happen

👉 This simulates the logic but is inefficient

"""

def simplifyPath(path):
    parts = path.split('/')
    
    changed = True
    while changed:
        changed = False
        new_parts = []
        
        i = 0
        while i < len(parts):
            if parts[i] == "" or parts[i] == ".":
                # ignore
                changed = True
                i += 1
            elif parts[i] == "..":
                # remove previous valid directory
                if new_parts:
                    new_parts.pop()
                changed = True
                i += 1
            else:
                new_parts.append(parts[i])
                i += 1
        
        parts = new_parts

    return "/" + "/".join(parts)

print(simplifyPath("/a/./b/../../c/"))  # Output: "/c"


# Time Complexity: O(n^2) in the worst case due to repeated processing of parts
# Space Complexity: O(n) for the parts list and new_parts list
