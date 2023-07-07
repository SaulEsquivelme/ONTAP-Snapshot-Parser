#ONTAP Snapshot parser
import os

#Static string for directories
putty_file = r'C:\\Users\\Documents\\Python\\PuTTy_log.txt'
output_dir = r'C:\\Users\\Documents\\Python\\parser_output\\'

#Static string to discard from PuTTy log file 
putty_header = '=~=~=~=~=~=~=~=~=~=~=~='
separator = '------------------'
command = 'Cluster1::>'
new_line = '\n'
header = 'vserver'
entries = 'entries were displayed'
ext_vol = 'This is just an initialization dummy string '

outp_array = []

#Function write_csv creates the output file inside the output directory
def write_csv(outp_a):
    with open(output_dir + 'output.csv', 'a') as ofile:
        for item in outp_a:
            ostring = str(','.join(item)) + '\n'
            print(ostring)
            ofile.write(ostring)

#Function empty_output_folder wipes the content of the dedicated output directory
def empty_output_folder():
    try:
        for file in os.scandir(output_dir):
            os.remove(file.path)
    except Exception as e:
        print('Error when cleaning output directory: ' + str(e)) 

#Main
with open (putty_file, 'r') as file:
    contents = file.readlines()
for line in contents:
    if separator not in line and command not in line and new_line is not line and header not in line and entries not in line and putty_header not in line:
        line = line[:-1]
        separated_line = line.split()
        separated_line = separated_line[-2:]
        #print(separated_line)
        vol_name = separated_line[0]
        if vol_name != ext_vol:
            ext_vol = vol_name
        elif vol_name == ext_vol:
            outp_array.append(separated_line)
empty_output_folder()

write_csv(outp_array)        
