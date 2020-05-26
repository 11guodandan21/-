import pytest, requests, json

session = requests.session()

# 登录
@pytest.fixture(scope="session")
def login():
    login_url = 'http://test-api-passport.kaikeba.com/login'
    data = {"mobile": "18510780788", "verify_code": "111111", "remember": 1}
    response_object = session.post(url=login_url, data=data)
    dict_data = json.loads(response_object.text)
    s_t = dict_data['data']['sso_token']

    url = 'http://test-weblearn.kaikeba.com/token'
    data = {"sso_token": "{}".format(s_t)}
    response_object = session.post(url=url, data=data)


# 提取userId 和 accessToken
@pytest.fixture(scope="session")
def get_user_id_and_access_token(login):
    token_url = 'https://xiaoke-test.kaikeba.com/api/v1.0/small-course/passport/learn-center/token?app_id='
    response_object = session.get(url=token_url, verify=False)
    dictionary_data = json.loads(response_object.text)
    extract_user_id = dictionary_data['data']['userId']
    extract_access_token = dictionary_data['data']['accessToken']
    return extract_user_id, extract_access_token


# 提取jupyter_courseid和small_course_first_course_id和small_course_first_class_id和small_course_second_course_id
@pytest.fixture(scope="session")
def get_jupyter_id_and_small_course_id(login):
    url = 'http://test-weblearn.kaikeba.com/student/small_course/list'
    response_object = session.get(url=url)
    dict_data = json.loads(response_object.text)
    extract_small_course_first_course_id = dict_data['data']['list'][0]['id']
    extract_small_course_first_class_id = dict_data['data']['list'][0]['firstClassId']
    return extract_small_course_first_course_id, extract_small_course_first_class_id


# 提取学习中心learn_center_courser_id和learn_center_chapter_id
@pytest.fixture(scope="session")
def get_learn_center_courser_id_and_learn_center_chapter_id(login):
    url = 'http://test-weblearn.kaikeba.com/student/course/list'
    response_objecy = session.get(url=url)
    dict_data = json.loads(response_objecy.text)
    learn_center_couser_id = dict_data['data']['vip'][0]['course_id']
    learn_center_chapter_id = dict_data['data']['vip'][0]['last_info']['chapter']['chapter_id']
    # print(learn_center_couser_id,learn_center_chapter_id)
    return learn_center_couser_id, learn_center_chapter_id





