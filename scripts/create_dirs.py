import os 
# scrabed data dir 
os.makedirs(os.path.join(os.getcwd() , 'scrabed_data')) 
os.makedirs(os.path.join(os.getcwd() , 'scrabed_data' , 'images')) 

# resized_data dir 
os.makedirs(os.path.join(os.getcwd() , 'resized_data')) 
os.makedirs(os.path.join(os.getcwd() , 'resized_data' , 'images')) 
os.makedirs(os.path.join(os.getcwd() , 'resized_data' , 'labels')) 

# data 
splits = ['train' , 'val']
os.makedirs(os.path.join(os.getcwd() , 'data'))  
for split in splits : 
    os.makedirs(os.path.join(os.getcwd() , 'data', split)) 
    os.makedirs(os.path.join(os.getcwd() ,'data',  split , 'images')) 
    os.makedirs(os.path.join(os.getcwd() ,'data',split , 'labels')) 

# aug_data 

os.makedirs(os.path.join(os.getcwd() , 'aug_data'))  
for split in splits : 
    os.makedirs(os.path.join(os.getcwd() , 'aug_data', split)) 
    os.makedirs(os.path.join(os.getcwd() ,'aug_data',  split , 'images')) 
    os.makedirs(os.path.join(os.getcwd() ,'aug_data',split , 'labels')) 

