from 医疗机器人.uilt.config import like_word
from py_aho_corasick import py_aho_corasick

class QuestionClassifier:
    def __init__(self):
        # 加载特征词
        self.disease_wds= [i.strip() for i in open('export/disease.txt') if i.strip()]
        self.department_wds= [i.strip() for i in open('export/department.txt') if i.strip()]
        self.check_wds= [i.strip() for i in open('export/check.txt') if i.strip()]
        self.drug_wds= [i.strip() for i in open('export/drug.txt') if i.strip()]
        self.food_wds= [i.strip() for i in open('export/food.txt') if i.strip()]
        self.producer_wds= [i.strip() for i in open('export/producer.txt') if i.strip()]
        self.symptom_wds= [i.strip() for i in open('export/symptoms.txt') if i.strip()]
        self.region_words = set(self.department_wds + self.disease_wds + self.check_wds + self.drug_wds + self.food_wds + self.producer_wds + self.symptom_wds)
        self.deny_words = [i.strip() for i in open('export/deny.txt',encoding="utf-8") if i.strip()]
        # 构造领域actree
        self.region_tree = py_aho_corasick.Automaton(list(self.region_words))
        # 问句疑问词
        self.symptom_qwds = like_word['symptom_qwds']
        self.cause_qwds = like_word['cause_qwds']
        self.acompany_qwds = like_word['acompany_qwds']
        self.food_qwds = like_word['food_qwds']
        self.drug_qwds = like_word['drug_qwds']
        self.prevent_qwds = like_word['prevent_qwds']
        self.lasttime_qwds = like_word['lasttime_qwds']
        self.cureway_qwds = like_word['cureway_qwds']
        self.cureprob_qwds = like_word['cureprob_qwds']
        self.easyget_qwds = like_word['easyget_qwds']
        self.check_qwds = like_word['check_qwds']
        self.belong_qwds = like_word['belong_qwds']
        self.cure_qwds = like_word['cure_qwds']
        print('model init finished ......')


    '''分类主函数'''
    def classify(self, question):
        data = {}

        medical_dict = self.check_medical(question)
        if medical_dict == {}:return {}
        data['args'] = medical_dict
        #收集问句当中所涉及到的实体类型
        types = []
        for type_ in medical_dict.values():
            types += type_

        question_types = []

        # 症状
        if self.check_words(self.symptom_qwds, question) and ('disease' in types):
            question_type = 'disease_symptom'
            question_types.append(question_type)
        if self.check_words(self.symptom_qwds, question) and ('symptom' in types):
            question_type = 'symptom_disease'
            question_types.append(question_type)

        # 原因
        if self.check_words(self.cause_qwds, question) and ('disease' in types):
            question_type = 'disease_cause'
            question_types.append(question_type)
        # 并发症
        if self.check_words(self.acompany_qwds, question) and ('disease' in types):
            question_type = 'disease_acompany'
            question_types.append(question_type)

        # 推荐食品
        if self.check_words(self.food_qwds, question) and 'disease' in types:
            deny_status = self.check_words(self.deny_words, question)
            if deny_status:
                question_type = 'disease_not_food'
            else:
                question_type = 'disease_do_food'
            question_types.append(question_type)

        #已知食物找疾病
        if self.check_words(self.food_qwds+self.cure_qwds, question) and 'food' in types:
            deny_status = self.check_words(self.deny_words, question)
            if deny_status:
                question_type = 'food_not_disease'
            else:
                question_type = 'food_do_disease'
            question_types.append(question_type)

        # 推荐药品
        if self.check_words(self.drug_qwds, question) and 'disease' in types:
            question_type = 'disease_drug'
            question_types.append(question_type)

        # 药品治啥病
        if self.check_words(self.cure_qwds, question) and 'drug' in types:
            question_type = 'drug_disease'
            question_types.append(question_type)

        # 疾病接受检查项目
        if self.check_words(self.check_qwds, question) and 'disease' in types:
            question_type = 'disease_check'
            question_types.append(question_type)

        # 已知检查项目查相应疾病
        if self.check_words(self.check_qwds+self.cure_qwds, question) and 'check' in types:
            question_type = 'check_disease'
            question_types.append(question_type)

        #　症状防御
        if self.check_words(self.prevent_qwds, question) and 'disease' in types:
            question_type = 'disease_prevent'
            question_types.append(question_type)

        # 疾病医疗周期
        if self.check_words(self.lasttime_qwds, question) and 'disease' in types:
            question_type = 'disease_lasttime'
            question_types.append(question_type)

        # 疾病治疗方式
        if self.check_words(self.cureway_qwds, question) and 'disease' in types:
            question_type = 'disease_cureway'
            question_types.append(question_type)

        # 疾病治愈可能性
        if self.check_words(self.cureprob_qwds, question) and 'disease' in types:
            question_type = 'disease_cureprob'
            question_types.append(question_type)

        # 疾病易感染人群
        if self.check_words(self.easyget_qwds, question) and 'disease' in types :
            question_type = 'disease_easyget'
            question_types.append(question_type)

        # 若没有查到相关的外部查询信息，那么则将该疾病的描述信息返回
        if question_types == [] and 'disease' in types:
            question_types = ['disease_desc']

        # 若没有查到相关的外部查询信息，那么则将该疾病的描述信息返回
        if question_types == [] and 'symptom' in types:
            question_types = ['symptom_disease']

        # 将多个分类结果进行合并处理，组装成一个字典
        data['question_types'] = question_types

        return data

    '''构造词对应的类型'''
    def build_wdtype_dict(self,wds):
        wd_dict = {}
        for wd in wds:
            wd_dict[wd] = []
            if wd in self.disease_wds:
                wd_dict[wd].append('disease')
            if wd in self.department_wds:
                wd_dict[wd].append('department')
            if wd in self.check_wds:
                wd_dict[wd].append('check')
            if wd in self.drug_wds:
                wd_dict[wd].append('drug')
            if wd in self.food_wds:
                wd_dict[wd].append('food')
            if wd in self.symptom_wds:
                wd_dict[wd].append('symptom')
            if wd in self.producer_wds:
                wd_dict[wd].append('producer')
        return wd_dict

    '''问句过滤'''
    def check_medical(self, question):
        region_wds = list(set([data[1] for data in self.region_tree.get_keywords_found(question)]))
        print(region_wds)
        stop_wds = []
        for wd1 in region_wds:
            for wd2 in region_wds:
                if wd1 in wd2 and wd1 != wd2:
                    stop_wds.append(wd1)
        final_wds = [i for i in region_wds if i not in stop_wds]
        final_dict = self.build_wdtype_dict(final_wds)
        return final_dict

    '''基于特征词进行分类'''
    def check_words(self, wds, sent):
        for wd in wds:
            if wd in sent:
                return True
        return False


if __name__ == '__main__':
    handler = QuestionClassifier()
    data = handler.classify('中毒了怎么办')
    print(data)