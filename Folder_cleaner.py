import os
import sys

Folder_types = {
  "Images": ['.png','.jpg', '.jpeg', '.gif'],
  "PDF": ['.pdf'],
  "Archives": ['.zip', '.rar'],
  "Python Files": ['.py'],

}





def main(path):
  if not os.path.isdir(path):
    return "Path does not exist or is not a directory"

  for folder in Folder_types.keys():
    folder_path = os.path.join(path,folder)
    if not os.path.isdir(folder_path):
      os.mkdir(folder_path)
  others_folder_path = os.path.join(path,"Others")
  if not os.path.isdir(others_folder_path):
      os.mkdir(others_folder_path)

  files = os.listdir(path)
  for file in files:
    moved = False
    file_path = os.path.join(path,file)
    if os.path.isdir(file_path):
      continue
    base,extension = os.path.splitext(file)
    for folder,extention_list in Folder_types.items():
      if extension.lower() in extention_list:
        new_path = os.path.join(path,folder,file)
        os.rename(file_path,new_path)
        moved = True
        break
        
    if not moved:
      new_path = os.path.join(path,"Others",file)
      os.rename(file_path,new_path)  
  

  return "files sorted succesfully"






if __name__ == '__main__':
    if len(sys.argv) > 1:
      print(main(sys.argv[1]))
    else:
      path = input('Enter the Path/Location of the folder you want to filter: ')
      print(main(path))                 
