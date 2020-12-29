# logic_detector
An attempt to detect logic of the program

Steps to Install:

1. Install docker
2. Install docker-compose
3. Clone the repo
4. `sudo docker-compose up --build`

Steps to Train/Learn new Functions via UI :

1. Type `localhost:8090` in browser to access UI
2. Select model
3. Type code/upload file. The Function name will be taken as label
4. Click on Learn button

Steps to Test/Predict Functions via UI:

1. Type `localhost:8090` in browser to access UI
2. Select model
3. Type code/upload file.
4. Click on Test Button

Steps to Learn new Functions via Library function call:

1. `import model1.dataset_gen as g1`
2. `g1.add_to_dataset(function,lang)`

Steps to Test/Predict Functions via Library function call:

1. `import model1.predict as mp1`
2. `m = mp1.predict(function,language)`

To determine accuracy label wise for dynamic model:

1. `cd backend`
2. Add the labels for which accuracy has to be determined in the labels list in dataset_server.py. Available labels can be reffered from mapping.json 
3. Run `python dataset_server.py` and the results can be seen in results.txt 

Note to add a new logic detection module, 

1. create a directory modelx where x is a number. 
2. add the required python modules in it.
3. create a file called `predict.py` and add a function called `predict(function,language)` which takes 2 args and returns a python dict. `function` is the string argument which contains the function definition and language specifies the language. The return value must be a python dict which gives probabilities of various classes. The keys are the classes and values are probabilities.

Note :

1.  giving functions with special pre conditions like strings having only digits or only special characters or functions having types which are not supported by dynamic analysis model, then, will have to specify the pre conditions in dictionary passed as default arg for that parameter.

For example : In case of a function validating IP address string, the string must not contain upper case, lower case and special characters. So in that case, the function signature will be

`def IP_VAL(s:str={'upper_count':0,'lower_count':0, 'special_count':0, 'digits_count': 8}):
  pass`
  
So here my making upper case, lower case and special character count as 0 and digits count as 8, you are specifying the precondition as string having 8 digits with no upper case, lower case and special characters.

2. Default Precondition when no precondition is specified is

`{"start":0,"end":11,"len_list":8,"upper_count":3,"lower_count":3,"digits_count":3,"special_count":3 ,"wspace_count":3,"generator": lambda : random.random}`

So when function signature is like this,

`def IP_VAL(s:str):
  pass`
  
 Then, random strings of length 15 are created which have 3 upper case, 3 lower case, 3 digits and 3 special characters and 3 whitespaces. If s was list, then random list of length 8 is generated.
 
3. start and end specify the range of random numbers to be generated. Ex : if start=1, end=1000, then numbers in the range [1,1000] are generated. 

4. generator specifies a custom random data generator for an argument. It is a callable which takes no arguments. It can also be a string which has a function inside. The function must not take any arguments.

