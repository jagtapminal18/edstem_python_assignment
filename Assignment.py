import json
import re

#function to process Log contain
def process_log_file(input1):
    list1=[]
    errorList=[]
    errorCount=0
    output_dict={}
    try:
        if(input1 !=''):
                #Here if input log is presents then find count and error
                pattern = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] (\w+): (.+)'
                matches = re.findall(pattern, input1)
                for m in matches:
                    timestamp, level, message = m
                    if(level=='ERROR'and (message not in errorList)):
                        # print(message)
                        errorCount = errorCount+1
                        errorList.append(message)
                    elif(level=='ERROR'):
                        errorCount=errorCount+1
                output_dict={'total_errors':errorCount, 'unique_error_messages':sorted(errorList)} 

        else:
            #here if log='' then return 0 count and null entry
            output_dict={'total_errors':errorCount, 'unique_error_messages':errorList} 
            raise ValueError("Empty string")   
             
    except ValueError as e:
        print(e)

    finally:
        print("Execution Succesfully Completed Output as below")
               
    return output_dict


#function call 
# Test Case 1
input1 = '''[2024-01-07 10:15:30] ERROR: Database connection failed
[2024-01-07 10:15:35] INFO: Retry attempt 1
[2024-01-07 10:15:40] ERROR: Authentication failed'''
# Test Case 2
input2 = '''[2024-01-07 10:15:30] ERROR: Memory overflow
[2024-01-07 10:15:35] ERROR: Memory overflow'''
# Test Case 3 (Edge case)
input3 = ''

print(process_log_file(input2))
