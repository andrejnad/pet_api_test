from petApiCommunication import PetApiCommunication


def full_report():
    separator = 80*"="
    i = 0
    step = "\n\nSTEP "
    print("START " + separator)
    try:
        api = PetApiCommunication(url_test, key)
        print("Communication class has been initialized")
    except Exception as e:
        print(e)
        return

    print(step + str(i) + separator)
    i += 1
    step_1 = api.create_and_return_a_new_pet(pet_json)
    print("Result: ")
    print("     " + str(step_1))

    print(step + str(i) + separator)
    i += 1
    step_2 = api.verify_pet(pet_json["id"], pet_json)
    print("Result: ")
    print("     " + str(step_2))

    print(step + str(i) + separator)
    i += 1
    step_3 = api.update_pet_and_verify(pet_json["id"], "name", "bruno")
    print("Result: ")
    print("     " + str(step_3))

    print(step + str(i) + separator)
    i += 1
    step_4 = api.delete_pet(pet_json["id"])
    print("Result: ")
    print("     " + str(step_4))
    print("END " + separator)


url_test = "https://petstore.swagger.io/v2/pet/"
key = "andrej"
pet_json = {
    "id": 896,
    "category": {
        "id": 148,
        "name": "mammal"
    },
    "name": "pluto",
    "photoUrls": [
        "url_to_photo"
    ],
    "tags": [
        {
            "id": 421,
            "name": "my_wife_s_dog"
        }
    ],
    "status": "alive"
}

full_report()
