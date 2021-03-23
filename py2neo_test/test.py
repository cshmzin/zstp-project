from py2neo import Graph, Node, Relationship, NodeMatcher
from py2neo_test.get_data import Datas



class Neo4j():
    def __init__(self,datas):
        self.link = Graph('http://localhost:7474',username = 'neo4j',password = 'csh826926')
        self.link.delete_all()
        self.datas = datas
        self.Matcher = NodeMatcher(self.link)


    def create_node(self):
        for buy_name in list(set(self.datas['buy_key'])):
            node = Node('购买方',name=buy_name)
            self.link.create(node)
        for sell_name in list(set(self.datas['sell_key'])):
            node = Node('销售方',name=sell_name)
            self.link.create(node)

    def match_node(self,i):
        buy_node = self.Matcher.match('购买方').where(f"_.name='{self.datas['buy_key'][i]}'").first()
        sell_node = self.Matcher.match('销售方').where(f"_.name='{self.datas['sell_key'][i]}'").first()
        print([buy_node,sell_node])
        return [buy_node,sell_node]


    def create_relationship(self):
        for i in range(len(self.datas['buy_key'])):
            relationship = Relationship(self.match_node(i)[0],self.datas['money_key'][i],self.match_node(i)[1])
            self.link.create(relationship)


if __name__ == '__main__':
    datas = Datas()
    all_datas = datas.pd_data()
    neo4j = Neo4j(all_datas)
    neo4j.create_node()
    neo4j.create_relationship()




