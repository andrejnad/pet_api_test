Task:
  - Write a python class/module to:
      1. Create and return a new Pet.
      2. Verify The Pet was created with correct data.
      3. Update this Pet_name, Verify update and return record.
      4. Delete the Pet and demonstrate pet now deleted.

Installation:
  - make sure you have python 3 installed
  - download main.py and petApiCommunication.py into same folder
  - install library "requests" (pip install requests if you have pip installed)
  - install librart "certifi" (pip install certifi)

Before run:
  - open main.py
  - set api_key stored in variable "key" to your own api key (if you will not provide api key, then default (andrej) will be used)
  - set valid json request stored in variable "pet_json"
  
How to run:
  - run following command from command line: "python main.py"
  
Results:
  - all results will be printed into console:
      Step 1: Pet will be created and function will return pet under Result
      Step 2: Function will verify that data on client match data on server and will return boolean True/False under Result
      Step 3: Name will be updated, record will be verified and function will return pet under Result
      Step 4: Pet will be deleted from server, then verified and result of verification will be displayed under Result
  
Example:
  
preconditions for the example:
  - global variables in main.py:
      - url_test = "https://petstore.swagger.io/v2/pet/"
      - key = "andrej"
      - changed_name = "bruno"
      - pet_json = {"id": 896,
                    "category": {
                        "id": 148,
                        "name": "mammal"
                    },
                    "name": "pluto",
                    "photoUrls": ["url_to_photo"],
                    "tags": [{
                        "id": 421,
                        "name": "my_wife_s_dog"}],
                    "status": "alive"
                    }
                    
function returns:
  - step 1:   {'id': 896, 'category': {'id': 148, 'name': 'mammal'}, 'name': 'pluto', 'photoUrls': ['url_to_photo'], 'tags': [{'id': 421, 'name': 'my_wife_s_dog'}], 'status': 'alive'}
  - step 2:   True
  - step 3:   {'id': 896, 'category': {'id': 148, 'name': 'mammal'}, 'name': 'bruno', 'photoUrls': ['url_to_photo'], 'tags': [{'id': 421, 'name': 'my_wife_s_dog'}], 'status': 'alive'}
  - step 4:   404 Not Found

full report:


python main.py
START ================================================================================
Communication class has been initialized


STEP 1================================================================================
Creating new pet with id 896:
     200 OK
Result:
     {'id': 896, 'category': {'id': 148, 'name': 'mammal'}, 'name': 'pluto', 'photoUrls': ['url_to_photo'], 'tags': [{'id': 421, 'name': 'my_wife_s_dog'}], 'status': 'alive'}


STEP 2================================================================================
Verify if pet has correct data:
     Server data: Length: 6; Content: {'id': 896, 'category': {'id': 148, 'name': 'mammal'}, 'name': 'pluto', 'photoUrls': ['url_to_photo'], 'tags': [{'id': 421, 'name': 'my_wife_s_dog'}], 'status': 'alive'}
     Client data: Length: 6; Content: {'id': 896, 'category': {'id': 148, 'name': 'mammal'}, 'name': 'pluto', 'photoUrls': ['url_to_photo'], 'tags': [{'id': 421, 'name': 'my_wife_s_dog'}], 'status': 'alive'}
     Verification Result: True
Result:
     True


STEP 3================================================================================
Update pet:
     Status: 200 OK
     Content: {'id': 896, 'category': {'id': 148, 'name': 'mammal'}, 'name': 'bruno', 'photoUrls': ['url_to_photo'], 'tags': [{'id': 421, 'name': 'my_wife_s_dog'}], 'status': 'alive'}
Verify if pet has correct data:
     Server data: Length: 6; Content: {'id': 896, 'category': {'id': 148, 'name': 'mammal'}, 'name': 'bruno', 'photoUrls': ['url_to_photo'], 'tags': [{'id': 421, 'name': 'my_wife_s_dog'}], 'status': 'alive'}
     Client data: Length: 6; Content: {'id': 896, 'category': {'id': 148, 'name': 'mammal'}, 'name': 'bruno', 'photoUrls': ['url_to_photo'], 'tags': [{'id': 421, 'name': 'my_wife_s_dog'}], 'status': 'alive'}
     Verification Result: True
Result:
     {'id': 896, 'category': {'id': 148, 'name': 'mammal'}, 'name': 'bruno', 'photoUrls': ['url_to_photo'], 'tags': [{'id': 421, 'name': 'my_wife_s_dog'}], 'status': 'alive'}


STEP 4================================================================================
Deleting pet with id 896 :
     200 OK
Something is not OK while verifying pet with id 896 :
     404 Not Found
Result:
     404 Not Found
END ================================================================================


