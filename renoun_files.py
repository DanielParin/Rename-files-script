import os
import subprocess
import multiprocessing

# directory of files to renoun (write yours).
directory = "/run/media/danipr/5058-991A"

# Word/s to delete (write yours).
string_to_delete = "[SPOTIFY-DOWNLOADER.COM] "


def renoun_fle(file_name):
    
    if file_name.startswith(string_to_delete):
        new_name = file_name[len(string_to_delete):]
        
        old_path = os.path.join(directory, file_name)
        new_path = os.path.join(directory, new_name)
        
        try:
            subprocess.run(["mv", old_path, new_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        except subprocess.CalledProcessError as e:
            print(f'Failed to rename {file_name}: {e.stderr.decode()}')
        
        print(f'Renamed: {file_name} --> {new_name}')
    
    else:
        print(f'Not renamed: {file_name}')
        

def main():
    
    archives = os.listdir(directory)
    processes = []
    
    
    for archive in archives:
        
        process = multiprocessing.Process(target=renoun_fle,args=(archive,))
        processes.append(process)
        process.start()
    
    
    for process in processes:
        process.join()
        
    print("---END OF THE SCRIPT---")
    
if __name__ == "__main__":
    main()
    