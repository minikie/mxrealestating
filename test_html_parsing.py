import requests
from bs4 import BeautifulSoup
from slimit.ast import String as astString
from slimit.parser import Parser
from slimit.visitors.nodevisitor import ASTVisitor



r = requests.get("https://m.land.naver.com/article/info/1905842490")
soup = BeautifulSoup(r.content, "html.parser")
res = dict()

#for sc in soup.findAll("script", class_="listtable_1"):
for sc in soup.findAll("script"):
    pos = sc.text.find('land.articleDetail.jsonPageData')
    if pos > 0:
        bracket_start_pos = sc.text.find('{',pos)
        bracket_end_pos = sc.text.find(';', pos)
        #print(sc.text[bracket_start_pos:bracket_end_pos])
        #js_obj_txt = sc.text[bracket_start_pos:bracket_end_pos]
        js_obj_txt = sc.text[pos:bracket_end_pos]
        # print(js_obj_txt)
        parser = Parser()
        tree = parser.parse(js_obj_txt)
        visitor = MyVisitor()
        visitor.visit(tree)
        res = visitor.res

print(res)

    #print(sc.text.find('land.articleDetail.jsonPageData'))
    #print(sc.text.replace(' ',''))
    # print(sc.text.replace(' ', '').replace('\n','').replace('\t',''))
    #print(sc.text.replace(' ', '').find('land.articleDetail.jsonPageData'))
    
    
# from slimit.parser import Parser
# from slimit.visitors import nodevisitor
# from slimit import ast
#
# parser = Parser()
# tree = parser.parse('for(var i=0; i<10; i++) {var x=5+i;}')
# for node in nodevisitor.visit(tree):
#     if isinstance(node, ast.Identifier) and node.value == 'i':
#         print(node.value)
#
# # print (tree.to_ecma()) # print awesome javascript :)
