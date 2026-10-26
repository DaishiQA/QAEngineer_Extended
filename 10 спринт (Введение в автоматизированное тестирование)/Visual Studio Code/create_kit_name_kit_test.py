import sender_stand_request
import data

def get_kit_body(name):
    new_kit_name = data.kit_body.copy()
    new_kit_name["name"] = name
    return new_kit_name

def get_new_user_token():
    token_response = sender_stand_request.post_new_user(data.user_body)
    return token_response.json()['authToken']

def positive_assert(kit_body):
    new_kit_body = get_kit_body(kit_body)
    token = get_new_user_token()
    positive_response = sender_stand_request.post_new_client_kit(new_kit_body, token)
    assert positive_response.status_code == 201
    assert new_kit_body["name"] == positive_response.json()["name"]


def negative_assert_code_400(kit_body):
    new_kit_body = get_kit_body(kit_body)
    token = get_new_user_token()
    negative_response = sender_stand_request.post_new_client_kit(new_kit_body, token)
    assert negative_response.status_code == 400
    assert negative_response.json()["code"] == 400

def negative_assert_no_name(kit_body):
    token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Не все необходимые параметры были переданы"
    
# Тест 1. Успешное создание набора. Параметр name набора состоит из 1 буквы
def test_create_kit_1_letter_in_name_success_response():
    positive_assert("a")

# Тест 2. Успешное создание набора. Параметр name набора состоит из 511 букв
def test_create_kit_511_letters_in_name_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3. Ошибка создания набора. Параметр name набора состоит из 0 букв
def test_create_kit_0_letter_in_name_negative_response():
    negative_assert_code_400("")

# Тест 4. Ошибка создания набора. Параметр name набора состоит из 512 букв
def test_create_kit_512_letters_in_name_negative_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5. Успешное создание набора. Параметр name набора состоит из английских букв
def test_create_kit_english_letters_in_name_success_response():
    positive_assert("QWErty")

# Тест 6. Успешное создание набора. Параметр name набора состоит из русских букв
def test_create_kit_russian_letters_in_name_success_response():
    positive_assert("Мария")

# Тест 7. Успешное создание набора. Параметр name набора состоит из спецсимволов
def test_create_kit_special_symbols_in_name_success_response():
    positive_assert("\"№%@\",")

# Тест 8. Успешное создание набора. Параметр name набора содержит пробелы
def test_create_kit_space_in_name_success_response():
    positive_assert(" Человек и КО ")

# Тест 9. Успешное создание набора. Параметр name набора содержит цифры
def test_create_kit_numbers_in_name_success_response():
    positive_assert("123")

# Тест 10. Ошибка создания набора. Параметр name набора в запросе не передан
def test_create_kit_no_name_in_name_negative_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)

# Тест 11. Ошибка создания набора. Тип параметра name: число
def test_create_kit_int_in_name_negative_response():
    kit_body = data.kit_body.copy()
    kit_body["name"] = 123
    token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 400
    assert response.json()["code"] == 400