import os  #to find location in your os
import shutil #to move your files to other locations in os
import glob #matiching a specified pathname


filename=glob.glob(r"Datasets/Combined/*")
#annote=['jpg','xml'] #creating list with filetype

image=['.jpg']
label=['.xml']

jpglocate=r'Dataset/Images_annotated'
xmllocate=r'Data set/Dataset/XML_annotated'

for file in filename:
    #print(os.path.splitext(file)[1])
    if(os.path.splitext(file)[1] in image):
        
        #shutil.copy(xmllocate,jpglocate)
        shutil.move(file,jpglocate)
    elif(os.path.splitext(file)[1] in label):
         shutil.move(file,xmllocate)
 #the end
