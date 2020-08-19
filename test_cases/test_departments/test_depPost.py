import requests
import unittest
import ddt

testData = [{'name': '覆盖所有参数', 'code': 201, 'body': '{"data": [{"dep_id": "中国001", "dep_name": "北京001", "master_name": "市长007", "slogan": "北京欢迎您"}]}'},
            {'name': '覆盖覆必选参数', 'code': 201, 'body': '{"data": [{"dep_id": "美国250", "dep_name": "纽约250", "master_name": "纽约市长250", "slogan": null}]}'},
            {'name': '必选参数depid为空', 'code': 400, 'body': '{"data": [{"dep_id": null, "dep_name": "魔法学院", "哈利波特": "Test-Master", "slogan": null}]}'},
            {'name': '必选参数depname为空', 'code': 400, 'body': '{"data": [{"dep_id": "星云001", "dep_name": null, "master_name": "女超人", "slogan": null}]}'},
            {'name': '必选参数mastername为空', 'code': 400, 'body': '{"data": [{"dep_id": "星云002", "dep_name": "星球大战", "master_name": "null", "slogan": "null"}]}'},
            {'name': '必选参数depid缺失', 'code': 400, 'body': '{"data": [{"dep_name": "上海", "master_name": "上海市长"}]}'},
            {'name': '必选参数depname缺失', 'code': 400, 'body': '{"data": [{"dep_id": "北京001", "master_name": "北京市长"}]}'},
            {'name': '必选参数mastername缺失', 'code': 400, 'body': '{"data": [{"dep_id": "广州001", "dep_name": "广州"}]}'},
            {'name': '必选参数depid冗余', 'code': 400, 'body': '{"data": [{"dep_id": "广州002", "dep_name": "广州", "master_name": "广州市长", "dep_id": "广州002"}]}'},
            {'name': '必选参数depname冗余', 'code': 400, 'body': '{"data": [{"dep_id": "广州003", "dep_name": "广州", "master_name": "广州市长", "dep_name": "广州"}]}'},
            {'name': '必选参数mastername冗余', 'code': 400, 'body': '{"data": [{"dep_id": "广州004", "dep_name": "广州", "master_name": "广州市长", "master_name": "广州市长"}]}'},
            {'name': '可选参数slogan冗余', 'code': 400, 'body': '{"data": [{"dep_id": "广州005", "dep_name": "广州", "master_name": "广州市长", "slogan": "北京欢迎您", "slogan": "北京欢迎您"}]}'},
            {'name': '必选参数depid参数类型错误', 'code': 400, 'body': '{"data": [{"dep_id": true, "dep_name": "广州", "master_name": "广州市长", "dep_id": "广州002"}]}'},
            {'name': '必选参数depname参数类型错误', 'code': 400, 'body': '{"data": [{"dep_id": "广州007", "dep_name": false, "master_name": "广州市长", "dep_id": "广州002"}]}'},
            {'name': '必选参数mastername参数类型错误', 'code': 400, 'body': '{"data": [{"dep_id": "广州008", "dep_name": "广州", "master_name": true, "dep_id": "广州002"}]}'}]


@ddt.ddt
class TestDepPost(unittest.TestCase):
    url = r'http://127.0.0.1:8000/api/departments/'

    @ddt.data(*testData)
    def test_depPost(self, data):
        res = requests.post(self.url, data['body'].encode('utf-8'), headers={'Content-Type': 'application/json'})
        self.assertEqual(data['code'], res.status_code, data['name'])


if __name__ == '__main__':
    unittest.main()