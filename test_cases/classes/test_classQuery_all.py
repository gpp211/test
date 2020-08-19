import ddt
import requests
import unittest

testData = [{'name': '查询所有', 'url': r'http://127.0.0.1:8000/api/departments/T01/classes/', 'params': None},
            {'name': '查询指定', 'url': r'http://127.0.0.1:8000/api/departments/T01/classes/2017T01C02/', 'params': None},
            {'name': '列表查询', 'url': r'http://127.0.0.1:8000/api/departments/T01/classes/',
             'params': {'$cls_id_list': '2017T01C03,2017T01C04'}},
            {'name': '列表查询-组合查询', 'url': r'http://127.0.0.1:8000/api/departments/T01/classes/',
             'params': {'$cls_id_list': '2017T01C03,2017T01C04', '$master_name_list': 'Master15,Master16'}},
            {'name': '条件查询', 'url': r'http://127.0.0.1:8000/api/departments/T01/classes/',
             'params': {'cls_name': '2017级Test学院C01班'}},
            {'name': '条件查询-组合查询', 'url': r'http://127.0.0.1:8000/api/departments/T01/classes/',
             'params': {'cls_name': '2017级Test学院C01班', 'master_name': 'Master', 'slogan': 'sloganSlogan'}},
            {'name': '模糊查询', 'url': r'http://127.0.0.1:8000/api/departments/T01/classes/',
             'params': {'blur': 1, 'cls_name': '2017级'}},
            {'name': '模糊查询-组合查询', 'url': r'http://127.0.0.1:8000/api/departments/T01/classes/',
             'params': {'blur': 1, 'cls_name': '2017级', 'master_name': '马'}}]


@ddt.ddt
class TestClassQueryAll(unittest.TestCase):

    @ddt.data(*testData)
    def test_classesQuery(self, data):
        url = data['url']
        if params := data['params']:
            res = requests.get(url, params)
        else:
            res = requests.get(url)
        self.assertEqual(200, res.status_code, data['name'])


if __name__ == '__main__':
    unittest.main()