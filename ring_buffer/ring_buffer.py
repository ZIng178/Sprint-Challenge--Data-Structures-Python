class RingBuffer:
    def __init__(self, capacity):
        self.capacity=capacity #size
        self.ringbuffer=[] #empty
        self.current_index=0 #current index

    def append(self, item):
        #compare the length of the empty and the capacity 
        # if the list is not full capacity append the item to the end 
        if len(self.ringbuffer)<self.capacity:
            self.ringbuffer.append(item)
       
       
        # if the list is full capacity, remove the oldest and insert the new item in its place 
        
        else:
            self.ringbuffer[self.current_index]=item
            self.current_index +=1
        
        if  self.current_index == self.capacity:
            self.current_index=0
    


    def get(self):
        #return the list 
        return self.ringbuffer