import gc

gc.collect()
print(gc.get_stats)

### how do the python manage the memory 

# Object_specific allocator : each data type of {dict,list,set} has it won optimed allocator
# private Heap : it is the area in the memory allocates the python objects live
# Garbage collector(GC): free memory when objects are no longer in use