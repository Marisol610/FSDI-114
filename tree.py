class Node:
    def __init__(self, data):
        self.left =None
        self.right = None
        self.data =data

class BinaryTree:
    def __init__(self):
        self.root =None

    def add(self, new_node, current=None):
        if not current:
            current =self.root
      
        if not current.left:
            current.left = new_node

        elif not current.right:
            current.right = new_node

        return self.add(new_node, current= current.left)

    


 def binary_search(arr,ele):
     #binary and last index value
     first = 0
     last = len(arr) - 1 
     found =False   
     mid = (first +last)/2
     #Match found

     if arr[mid] == ele:
         found = True
         #Set new midpoint up or down depending on comparison
         else: 
             #set down
             if ele < arr[mid]:
         last = mid -1
         #set up
         else:
             first = mid + 1

        return found


#recursive function
        def rec_bin_search(arr,ele):
            #Base case! is when the len of the array is 0

            if len(arr) == o:
                return False
            # Recursive case
            else:
                mid = len(arr)/2
                #if match found

                if arr[mid]== ele:
                    return True

                else:
                    #call again on second half
                    if ele<arr[mid]:
                        return rec_bin_search(arr[mid], ele)
                        #or call on first half

                    else:
                        return rec_bin_search(arr[mid+1:],ele)