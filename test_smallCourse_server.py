# -*- coding: utf-8 -*-
import requests,pytest,time

timeStmp=int(time.time())

class TestSmallCourseServer:

    # 接口-获取章节学习记录
    def test_obtain_chapter_learn_record(self,get_user_id_and_access_token,get_jupyter_id_and_small_course_id):
        user_and_access_token=get_user_id_and_access_token
        userId=user_and_access_token[0]
        accessToken=user_and_access_token[1]
        jupyter_small_course_id=get_jupyter_id_and_small_course_id
        small_course_first_course_id=jupyter_small_course_id[0]
        small_course_first_class_id=jupyter_small_course_id[1]
        jupyter_small_course_id=get_jupyter_id_and_small_course_id
        url = 'https://xiaoke-test.kaikeba.com/api/v1.0/small-course/user/{}/purchased-course/{}/history/latest/records?' \
              'token={}&class_id={}'.format(
            userId, small_course_first_course_id, accessToken, small_course_first_class_id)
        response_object = requests.get(url=url, verify=False)
        dict_data=response_object.json()
        assert "success" in dict_data['msg']


    # 获取学习中心课程信息
    def test_obtain_learn_center_course_information(self,get_learn_center_courser_id_and_learn_center_chapter_id):
        call_data=get_learn_center_courser_id_and_learn_center_chapter_id
        learn_center_course_id=call_data[0]
        print()
        print(learn_center_course_id)
        url = 'http://test-weblearn.kaikeba.com/student/courseinfo?course_id={}&__timestamp={}'.format(
            learn_center_course_id,timeStmp)
        print(url)
        response_object = requests.get(url=url)
        print(response_object.text)


if __name__ == "__main__":
    pytest.main(["-s", "test_smallCourse_server.py"])



