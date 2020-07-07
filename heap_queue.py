## heap_queue.py
## Implementation of heap classes: MinHeap and MaxHeap.
## The class creates a copy of input list, and heapify it.
## Original input list is not modified (for read-only).

## Input:   list ( int's, float's, char's)
## 2 methods to add data:
##  1. Passing a list in object declaration. Or,
##  2. Adding each element into the heap by using heappush( val).

class MinHeap:

    def __init__(self, list_input = []):
        ## Constructor of MinHeap. Takes list as input, then heapify it.
        ## Retuns None.    

        self.data   =   list_input;
        self.comparison_func    =   lambda x: x;

        self.heapify();
        
        return;
    
    def sizeof(self):
        # Returns the size of the heap (number of elements).
        return len(self.data);
    
    def heapify(self):
        # Using heappush() to populate the heap list.
        # Returns None.

        temp = self.data.copy();
        self.data = [];

        for n in temp:
            self.heappush(n);
        
        #print("HEAP: ", self.data);
        return;        

    def sorted(self):
        ## Returns a copy of sorted heap list.
        ## This function doesn't modify the heap list/structure.

        ans = [];
        temp = self.data.copy();        # Create duplicate copy of heaplist, for restoration later.

        while self.data:
            ans.append( self.heappop());
        
        self.data = temp;               # Restores back the heaplist.

        return ans;

    def heap_top(self):
        # Returns the top item of the heap.
        if self.data:    return self.data[0];
        else:            return None;
        
    def parent(self, i):
        # Returns the parent of index i.
        return (i-1)//2;

    def children(self, i):
        # Returns the children indexes of index i.
        return (i<<1) + 1, (i<<1) + 2 ;
    
    def set_comparison_func(self, func):
        # Sets the function
        self.comparison_func = func;
        return;

    def get_comparison_val(self,   data_object):
        ## Returns values used as comparison in implementing move_up and move_down functions.
        return self.comparison_func(data_object);

    def move_up(self, i_start):
        # Moves up last element to the upper heap chain.
        # This modifies the heap list data.
        # The function uses recursive calls to move the element.
        # Returns None.

        i = i_start;
        i_parent = self.parent(i);

        if i <= 0:      return;

        curr_val    =   self.get_comparison_val(    self.data[i]);
        parent_val  =   self.get_comparison_val(    self.data[i_parent]);

        if curr_val < parent_val:
            self.data[i], self.data[i_parent] = self.data[i_parent], self.data[i];
            self.move_up(i_parent);

        return;   

    def move_down(self, i_start = 0):
        # Moves down top element to the lower heap chain.
        # This modifies the heap list data.
        # The function uses recursive calls to move the element.
        # Returns None.

        i = i_start;
        max_size = len(self.data);

        if i >= max_size:     return;

        l, r    =   self.children(i);
        
        curr_val        =    self.get_comparison_val(    self.data[i]);
        left_val, right_val =   None, None;

        if r < max_size:

            left_val        =    self.get_comparison_val(    self.data[l]);
            right_val       =    self.get_comparison_val(    self.data[r]);            

            if left_val < right_val:

                if left_val < curr_val:
                    self.data[i], self.data[l] = self.data[l], self.data[i];
                    self.move_down(l);

            else:

                if right_val < curr_val:
                    self.data[i], self.data[r] = self.data[r], self.data[i];
                    self.move_down(r);
            
        elif l < max_size:

            left_val        =    self.get_comparison_val(    self.data[l]);

            if left_val < curr_val:
                self.data[i], self.data[l] = self.data[l], self.data[i];
                self.move_down(l);
        
        return;
    
    def heappop(self):
        # Returns the top element of the heap, then heapify the list.
        # If heap list is empty, returns None.

        if not self.data:           return None;
        elif len(self.data) == 1:   return self.data.pop();

        ans =   self.data[0];
        self.data[0] = self.data.pop();
        self.move_down();

        return ans;

    def heappush(self, x):
        # Adds a new element at bottom of heap list, then heapify the list.
        # Returns None.
        
        self.data.append(x);
        self.move_up(len(self.data)-1);


## MaxHeap class inherited from MinHeap class.
## The move_up and move_down methods are re-defined for MaxHeap.

class MaxHeap(MinHeap):

    def __init__(self, list_input = []):
        ## Constructor of MaxHeap. Inherit from MinHeap class.
        ## Takes list as input, then heapify it.
        ## Retuns None.  

        MinHeap.__init__(self, list_input);      
        return;
    
    def move_up(self, i_start):
        # Moves up last element to the upper heap chain.
        # This modifies the heap list data.
        # The function uses recursive calls to move the element.
        # Returns None.

        i = i_start;
        i_parent = self.parent(i);

        if i <= 0:      return;

        curr_val    =   self.get_comparison_val(    self.data[i]);
        parent_val  =   self.get_comparison_val(    self.data[i_parent]);

        if curr_val > parent_val:
            self.data[i], self.data[i_parent] = self.data[i_parent], self.data[i];
            self.move_up(i_parent);

        return;   

    def move_down(self, i_start = 0):
        # Moves down top element to the lower heap chain.
        # This modifies the heap list data.
        # The function uses recursive calls to move the element.
        # Returns None.
        
        i = i_start;
        max_size = len(self.data);

        if i >= max_size:     return;

        l, r    =   self.children(i);
        
        curr_val        =    self.get_comparison_val(    self.data[i]);

        if r < max_size:

            left_val        =    self.get_comparison_val(    self.data[l]);
            right_val        =    self.get_comparison_val(    self.data[r]);

            if left_val > right_val:

                if left_val > curr_val:
                    self.data[i], self.data[l] = self.data[l], self.data[i];
                    self.move_down(l);

            else:

                if right_val > curr_val:
                    self.data[i], self.data[r] = self.data[r], self.data[i];
                    self.move_down(r);
            
        elif l < max_size:

            left_val        =    self.get_comparison_val(    self.data[l]);

            if left_val > curr_val:
                self.data[i], self.data[l] = self.data[l], self.data[i];
                self.move_down(l);
        
        return;