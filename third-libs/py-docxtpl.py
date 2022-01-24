from docxtpl import DocxTemplate, RichText


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

context['foobar'] = RichText('Foobar!', color='ff0000')
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
            item["node_name"] = RichText(item["node_name"], color='00C800', size=10, )
        else:
            item["node_name"] = RichText(item["node_name"], color='F62633', size=10, )
               

context['status'] = "online"

tpl.render(context, autoescape=True)
tpl.save("tests/01.docx")