class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        dirs = path.split("/")
        l = []
        for dir in dirs:
            if dir == "." or dir == "":
                pass
            elif dir == "..":
                if len(l) > 0:
                    l.pop()
            else:
                l.append(dir)
  
        result = "/".join(l)
        return "/" + result 

def main():
    print Solution().simplifyPath("/home")
    print Solution().simplifyPath("/...")
    print Solution().simplifyPath("/a/./b/../../c/")
    print Solution().simplifyPath("/home/../../..")

if __name__ == '__main__':
    main()

