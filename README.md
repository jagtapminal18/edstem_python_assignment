# edstem_python_assignment

**Python_File_Name**: Assignment.py

**AWS Setup**: AWS Deployment.txt

**Testcase** : Testcases.txt

**video file** : code_Review.mp4

>**Following are the step for execution:**


<ins>_1)Python code execution:_</ins>
   python3 Assignment.py
   
<ins>_2)AWS deployment and testing :_</ins>

  1)Login to AWS account.
  
  2)select to Lambda function service.
  
  3)create lambda function with the required configurations
      Runtime: Python 3.9+
      Memory: 128 MB
      Timeout: 30 seconds
      IAM Role: Basic Lambda execution role
      
  4)Implement the lambda function.
  
  5)create Textcases(Triggers) for execution and save
  
  6)Deploy the code (Deploy)
  
  7)Test the code (Test)
  
**Requirements Function should:**
   1. Accept a string parameter containing log entries
   2. Return a dictionary with two keys:
      total_errors : Total count of ERROR entries
      unique_error_messages : List of unique error messages (sorted
      alphabetically)
      
      Example Input:

      '''[2024-01-07 10:15:30] ERROR: Database connection failed
                        [2024-01-07 10:15:35] INFO: Retry attempt 1
                        [2024-01-07 10:15:40] ERROR: Authentication failed'''
      
      Expected Output:
      
            function should return:
      
            {
            'total_errors': 3,
            'unique_error_messages': [
            'Authentication failed',
            'Database connection failed'
            ]
            }
      
        
  

  
