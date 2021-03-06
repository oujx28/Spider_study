# coding:utf-8

import json

class SpiderParser(object):
    def get_kw_cat(self, response):
        try:
            kw_json = json.loads(response, encoding='utf-8')
            cat_info = []
            if kw_json['sign'] is not None:
                for data in kw_json['list']:
                    id = data['Id']
                    name = data['Name']
                    cat_info.append({'id':id, 'cat_name':name})
                return cat_info
        except Exception as e:
            print(e)

    def get_kw_detail(self, response):
        detail_json = json.loads(response, encoding='utf-8')
        details = []
        for data in detail_json['Chapters']:
            if data is None:
                return
            else:
                try:
                    file_path = data['Path']
                    name = data['Name']
                    file_id = str(data['Id'])
                    details.append({'file_id':file_id, 'name':name, 'file_path':file_path})
                except Exception as e:
                    print(e)
        return details