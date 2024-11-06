def data_getter(file_handle,college_name_param):
    #logic
    counts={}
    for line in file_handle:
        print(line)
        line=line[:-1:]
        line_list=line.split(',')
       # print(line_list)
        college_name=line_list[1]
        if(college_name==college_name_param):
            counts+=1
            print(counts)
            print(line)
        else:
            counts=1
            print("else",counts)
    
file_handle = open(r'C:\Users\Administrator\Desktop\UST_Training\Day_08\sample_data.csv','r')
data_getter(file_handle,'College C')

file_handle.close()
