import shutil
import os


path = os.getcwd()
print("Path:",path)


files = os.listdir()

for f in files:
    if os.path.isdir(f):
        #print(f)

        videos = os.listdir(f)
        
        for v in videos:
            video, file = v.split('.')
            if file == 'mp4':
                #print(v)

                v_path = os.path.join(path,f,v)
                new_v_path = os.path.join(path,v)

                print(v_path)
                print(new_v_path)

                shutil.move(v_path,new_v_path)
                print(v + "moved")

    print("\n")
