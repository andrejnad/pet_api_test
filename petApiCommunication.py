from json import loads as json_loads
from json import dumps as json_dumps
import requests


class PetApiCommunication(object):
    def __init__(self, url: str, api_key: str = ""):
        self.url = url
        self.api_key = api_key

    def create_and_return_a_new_pet(self, request):
        headers = {
            "api_key": self.api_key,
            "content-Type": "application/json",
            "accept": "application/json"
        }
        response = requests.post(self.url, data=json_dumps(request), headers=headers)
        print("Creating new pet with id " + str(request["id"]) + ":")
        print("     " + str(response.status_code) + " " + str(response.reason))
        return json_loads(response.text)

    def verify_pet(self, pet_id: int, expected_data: dict = None):
        url = self.url + str(pet_id)
        response = requests.get(url)
        status_code = response.status_code
        if status_code != 200:
            print("Something is not OK while verifying pet with id " + str(pet_id) + " :")
            print("     " + str(status_code) + " " + str(response.reason))
        response = json_loads(response.text)
        if expected_data is None:
            return response
        return self.__verify_if_pet_has_correct_data__(response, expected_data)

    def update_pet_and_verify(self, pet_id: int, pet_key: str, pet_value):
        pet = self.verify_pet(pet_id)
        pet[pet_key] = pet_value
        headers = {
            "api_key": self.api_key,
            "content-Type": "application/json",
            "accept": "application/json"
        }
        response = requests.put(self.url, data=json_dumps(pet), headers=headers)
        print("Update pet: ")
        print("     Status: " + str(response.status_code) + " " + str(response.reason))
        print("     Content: " + str(json_loads(response.text)))

        self.verify_pet(pet_id, pet)
        return json_loads(response.text)

    def delete_pet(self, pet_id):
        url = self.url + str(pet_id)
        headers = {
            "api_key": self.api_key,
            "accept": "application/json"
        }
        response = requests.delete(url, headers=headers)
        print("Deleting pet with id " + str(pet_id) + " :")
        print("     " + str(response.status_code) + " " + str(response.reason))
        self.verify_pet(pet_id)
        return response.status_code

    @staticmethod
    def __verify_if_pet_has_correct_data__(response, expected_data: dict):
        """
        There should be some kind of data against which function should verify if received data are correct.
        Possible solutions:
            a) Keep all added pet details in local DB and then verify pet against them
            b) Verify data just after adding new pet
            c) Provide input data to verify function (I will do this one, but I am willing to change it if needed)
                        -   there will be an input dictionary with expected data
                        -   these data will be compared against received data from server
                        -   function will return True if data match, or False if data are different
                        -   prints may be turned into logs if needed
        :return: True if data match, False if data are different
        """
        print("Verify if pet has correct data:")
        print("     Server data: Length: " + str(len(response)) + "; Content: " + str(response))
        print("     Client data: Length: " + str(len(expected_data)) + "; Content: " + str(expected_data))
        if len(response) == len(expected_data):
            if response == expected_data:
                result = True
            else:
                result = False
        else:
            result = False
        print("     Verification Result: " + str(result))
        return result

    def get_url(self):
        return self.url

    def get_api_key(self):
        return self.api_key

    def set_url(self, value: str):
        try:
            self.url = value
            return True
        except Exception as e:
            raise e

    def set_api_key(self, value: str):
        try:
            self.api_key = value
            return True
        except Exception as e:
            raise e
