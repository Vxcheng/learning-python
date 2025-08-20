# -*- coding: utf-8 -*-
from docxtpl import DocxTemplate, RichText
import sys

reload(sys)
sys.setdefaultencoding('utf8')
tpl = DocxTemplate("tests/my_word_template.docx")
context = { 'company_name' : "World company" }
context['col_labels'] = ['fruit', 'vegetable', 'stone', 'thing']

context['items'] = [
        {'desc': 'Python interpreters', 'qty': 2, 'price': 'FREE'},
        {'desc': 'Django projects', 'qty': 5403, 'price': 'FREE'},
        {'desc': 'Guido', 'qty': 1, 'price': '100,000,000.00'},
    ]
context['total_price'] = '100,000,000.00'
context['category'] = 'Book'

context['foobar'] = RichText('RED', color='ff0000')
context["details"] = [
          {
            "group_name":"SRP",
            "transpro":"SRP",
            "node_name":"rac036",
            "ip_addr":"172.16.60.36"
          },
          {
            "group_name":"SRP",
            "transpro":"SRP",
            "node_name":"rac037",
            "ip_addr":"172.16.60.37"
          },
          {
            "group_name":"ISCSI",
            "transpro":"ISCSI",
            "node_name":"rac036",
            "ip_addr":"172.16.60.36"
          },
          {
            "group_name":"ISCSI",
            "transpro":"ISCSI",
            "node_name":"rac037",
            "ip_addr":"172.16.60.37"
          }
        ]

context["details2"] = [
[
    {
            "group_name":"SRP",
            "transpro":"SRP",
            "node_name":"rac036",
            "ip_addr":"172.16.60.36"
          },
          {
            "group_name":"SRP",
            "transpro":"SRP",
            "node_name":"rac037",
            "ip_addr":"172.16.60.37"
          }
],
[
     {
            "group_name":"ISCSI",
            "transpro":"ISCSI",
            "node_name":"rac036",
            "ip_addr":"172.16.60.36"
          },
          {
            "group_name":"ISCSI",
            "transpro":"ISCSI",
            "node_name":"rac037",
            "ip_addr":"172.16.60.37"
          }
]
]

for list in context['details2']:
    for item in list:
        if item["node_name"] == "rac037":
            item["node_name"] = RichText(item["node_name"], color='ff0000', )
        else:
            item["node_name"] = RichText(item["node_name"], color='ff0000',)
               
# Microsoft Yahei, Microsoft YaHei
context['status'] = "online"
context["critical"] = RichText('critical', color='F5222D',font='Microsoft YaHei',size=60, )
context["warning"] = RichText('warning', color='FAAD14',font='Microsoft YaHei', size=18)
context["prompt"] = RichText('prompt', color='13C2C2',font='Microsoft YaHei', size=20)
context["normal"] = RichText('normal', color='0A0D14',font='Microsoft YaHei', size=20)
context["colors"] = [
  "critical","warning", "prompt","normal"
]

tpl.render(context, autoescape=True)
tpl.save("tests/01.docx")