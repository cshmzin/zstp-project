import json
from py2neo import Graph, Node

class Create_Graph():
    def __init__(self):
        self.path = 'data/medical2.json'
        self.link = Graph('http://localhost:7474', username='neo4j', password='csh826926')
        self.link.delete_all()

    def diseases_property(self,disease,data_json):
        disease_dict = {}
        disease_dict['name'] = disease
        disease_dict['desc'] = ''  # 描述
        disease_dict['prevent'] = ''  # 解决方法
        disease_dict['cause'] = ''  # 造成原因
        disease_dict['get_prob'] = ''  # 疾病发生率
        disease_dict['easy_get'] = ''  # 病病易发人群
        disease_dict['cure_way'] = ''  # 治疗方法
        disease_dict['cure_lasttime'] = ''  # 治疗时间
        disease_dict['cured_prob'] = ''  # 治疗成功率
        if 'desc' in data_json:
            disease_dict['desc'] = data_json['desc']
        if 'prevent' in data_json:
            disease_dict['prevent'] = data_json['prevent']
        if 'cause' in data_json:
            disease_dict['cause'] = data_json['cause']
        if 'get_prob' in data_json:
            disease_dict['get_prob'] = data_json['get_prob']
        if 'easy_get' in data_json:
            disease_dict['easy_get'] = data_json['easy_get']
        if 'cure_way' in data_json:
            disease_dict['cure_way'] = data_json['cure_way']
        if 'cure_lasttime' in data_json:
            disease_dict['cure_lasttime'] = data_json['cure_lasttime']
        if 'cured_prob' in data_json:
            disease_dict['cured_prob'] = data_json['cured_prob']
        return disease_dict


    def read_data(self):
        # 共７类节点
        drugs = [] # 药品
        foods = [] #　食物
        checks = [] # 检查
        departments = [] #科室
        producers = [] #药品大类
        diseases = [] #疾病
        symptoms = []#症状
        disease_infos = []#疾病信息

        # 构建节点实体关系
        rels_department = [] #　科室－科室关系
        rels_noteat = [] # 疾病－忌吃食物关系
        rels_doeat = [] # 疾病－宜吃食物关系
        rels_recommandeat = [] # 疾病－推荐吃食物关系
        rels_commonddrug = [] # 疾病－通用药品关系
        rels_recommanddrug = [] # 疾病－热门药品关系
        rels_check = [] # 疾病－检查关系
        rels_drug_producer = [] # 厂商－药物关系
        rels_symptom = [] #疾病症状关系
        rels_acompany = [] # 疾病并发关系
        rels_category = [] #　疾病与科室之间的关系


        for data in open(self.path):
            data_json = json.loads(data)
            #构建疾病
            disease = data_json['name']#疾病名称
            disease_pot = self.diseases_property(disease,data_json) #疾病属性
            disease_infos.append(disease_pot)
            diseases.append(disease)

            #构建症状及其关系
            if 'symptom' in data_json:
                symptoms += data_json['symptom']
                for symptom in data_json['symptom']:
                    rels_symptom.append([disease, symptom])

            #构建疾病并发关系
            if 'acompany' in data_json:
                for acompany in data_json['acompany']:
                    rels_acompany.append([disease, acompany])

            #构建科室及相关关系
            if 'cure_department' in data_json:
                cure_department = data_json['cure_department']
                if len(cure_department) == 1: #只有一个表示无上下级
                    rels_category.append([disease, cure_department[0]])
                if len(cure_department) == 2: #2个表示有上下级
                    rels_department.append([cure_department[1], cure_department[0]])
                    rels_category.append([disease, cure_department[1]])
                departments += cure_department

            #构建药品及其关系
            if 'common_drug' in data_json:
                common_drug = data_json['common_drug']
                for drug in common_drug:
                    rels_commonddrug.append([disease, drug])
                drugs += common_drug

            if 'recommand_drug' in data_json:
                recommand_drug = data_json['recommand_drug']
                drugs += recommand_drug
                for drug in recommand_drug:
                    rels_recommanddrug.append([disease, drug])

            if 'drug_detail' in data_json:
                drug_detail = data_json['drug_detail']
                producer = [i.split('(')[0] for i in drug_detail]
                rels_drug_producer += [[i.split('(')[0], i.split('(')[-1].replace(')', '')] for i in drug_detail]
                producers += producer

            #构建食物及其关系
            if 'not_eat' in data_json:
                not_eat = data_json['not_eat']
                for _not in not_eat:
                    rels_noteat.append([disease, _not])
                foods += not_eat

            if 'do_eat' in data_json:
                do_eat = data_json['do_eat']
                for _do in do_eat:
                    rels_doeat.append([disease, _do])
                foods += do_eat

            if 'recommand_eat' in data_json:
                recommand_eat = data_json['recommand_eat']
                for _recommand in recommand_eat:
                    rels_recommandeat.append([disease, _recommand])
                foods += recommand_eat

            #构建检查及其关系
            if 'check' in data_json:
                check = data_json['check']
                for _check in check:
                    rels_check.append([disease, _check])
                checks += check


        return [[set(drugs), set(foods), set(checks), set(departments), set(producers), set(symptoms), set(diseases),disease_infos],
                [rels_check, rels_recommandeat, rels_noteat, rels_doeat, rels_department, rels_commonddrug, rels_drug_producer, rels_recommanddrug,rels_symptom, rels_acompany, rels_category]]

    def create_node(self,label,nodes):
        for node_name in nodes:
            node = Node(label, name=node_name)
            self.link.create(node)
        print(f'创建节点：{label},共{len(nodes)}个')

    def create_diseases_nodes(self, disease_infos):
        for disease_dict in disease_infos:
            node = Node("Disease", name=disease_dict['name'], desc=disease_dict['desc'],
                        prevent=disease_dict['prevent'] ,cause=disease_dict['cause'],
                        easy_get=disease_dict['easy_get'],cure_lasttime=disease_dict['cure_lasttime'],
                        cure_way=disease_dict['cure_way'] , cured_prob=disease_dict['cured_prob'])
            self.link.create(node)
        print('创建疾病实体成功')

    def create_graph_nodes(self):
        Drugs, Foods, Checks, Departments, Producers, Symptoms, Diseases, disease_infos = self.read_data()[0]
        self.create_diseases_nodes(disease_infos)
        self.create_node('Drug', Drugs)
        self.create_node('Food', Foods)
        self.create_node('Check', Checks)
        self.create_node('Department', Departments)
        self.create_node('Producer', Producers)
        self.create_node('Symptom', Symptoms)

    def create_relationship(self, start_node, end_node, edges, rel_type, rel_name):
        # 去重处理
        edges = list(set([tuple(edge) for edge in edges]))
        edges = [list(edge) for edge in edges]

        for edge in edges:
            p,q = edge
            query = "match(p:%s),(q:%s) where p.name='%s'and q.name='%s' create (p)-[rel:%s{name:'%s'}]->(q)" % (start_node, end_node, p, q, rel_type, rel_name)
            self.link.run(query)

    def create_graph_rels(self):
        rels_check, rels_recommandeat, rels_noteat, rels_doeat, rels_department, rels_commonddrug, rels_drug_producer, rels_recommanddrug,rels_symptom, rels_acompany, rels_category = self.read_data()[1]
        self.create_relationship('Disease', 'Food', rels_recommandeat, 'recommand_eat', '推荐食谱')
        self.create_relationship('Disease', 'Food', rels_noteat, 'no_eat', '忌吃')
        self.create_relationship('Disease', 'Food', rels_doeat, 'do_eat', '宜吃')
        self.create_relationship('Department', 'Department', rels_department, 'belongs_to', '属于')
        self.create_relationship('Disease', 'Drug', rels_commonddrug, 'common_drug', '常用药品')
        self.create_relationship('Producer', 'Drug', rels_drug_producer, 'drugs_of', '生产药品')
        self.create_relationship('Disease', 'Drug', rels_recommanddrug, 'recommand_drug', '好评药品')
        self.create_relationship('Disease', 'Check', rels_check, 'need_check', '诊断检查')
        self.create_relationship('Disease', 'Symptom', rels_symptom, 'has_symptom', '症状')
        self.create_relationship('Disease', 'Disease', rels_acompany, 'acompany_with', '并发症')
        self.create_relationship('Disease', 'Department', rels_category, 'belongs_to', '所属科室')

    '''导出数据'''
    def export_data(self):
        Drugs, Foods, Checks, Departments, Producers, Symptoms, Diseases, disease_infos = self.read_data()[0]
        f_drug = open('export/drug.txt', 'w+')
        f_food = open('export/food.txt', 'w+')
        f_check = open('export/check.txt', 'w+')
        f_department = open('export/department.txt', 'w+')
        f_producer = open('export/producer.txt', 'w+')
        f_symptom = open('export/symptoms.txt', 'w+')
        f_disease = open('export/disease.txt', 'w+')

        f_drug.write('\n'.join(list(Drugs)))
        f_food.write('\n'.join(list(Foods)))
        f_check.write('\n'.join(list(Checks)))
        f_department.write('\n'.join(list(Departments)))
        f_producer.write('\n'.join(list(Producers)))
        f_symptom.write('\n'.join(list(Symptoms)))
        f_disease.write('\n'.join(list(Diseases)))

        f_drug.close()
        f_food.close()
        f_check.close()
        f_department.close()
        f_producer.close()
        f_symptom.close()
        f_disease.close()

if __name__ == '__main__':
    graph = Create_Graph()
    graph.export_data()
    graph.create_graph_nodes()
    graph.create_graph_rels()