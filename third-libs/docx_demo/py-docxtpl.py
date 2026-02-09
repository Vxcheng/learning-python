from docxtpl import DocxTemplate, RichText

def parse_context(context):
  """
  docstring
  """
  hostgroup_details = [
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

  group_name_dict = dict()
  for i in range(len(hostgroup_details)):
      group_name = hostgroup_details[i]["group_name"]
      if  group_name not in group_name_dict:
        group_name_dict[group_name] = [hostgroup_details[i]]
      else:
        tmp_list = group_name_dict[group_name]
        tmp_list.append(hostgroup_details[i])
        group_name_dict[group_name] = tmp_list

  host_group_list = []
  for v in group_name_dict.values():
        host_group_list.append(v)
  context["hostgroup_details"] = host_group_list


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


hostgroup_details = [
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
        
group_name_dict = dict()
for i in range(len(hostgroup_details)):
  group_name = hostgroup_details[i]["group_name"]
  if  group_name not in group_name_dict:
    group_name_dict[group_name] = [hostgroup_details[i]]
  else:
    tmp_list = group_name_dict[group_name]
    tmp_list.append(hostgroup_details[i])
    group_name_dict[group_name] = tmp_list
    
host_group_list = []
for v in group_name_dict.values():
    host_group_list.append(v)
context["hostgroup_details2"] = host_group_list


for list in context['details2']:
    for item in list:
        if item["node_name"] == "rac037":
            item["node_name"] = RichText(item["node_name"], color='00C800', size=10, )
        else:
            item["node_name"] = RichText(item["node_name"], color='F62633', size=10, )
               
def parse_hostgroup(details):
    def append_nodeinfo(host_group):
        for item in host_group_list:
            if item['group_name'] == host_group['group_name']:
              item['node_name'] += "\n" + host_group['node_name']
              item['ip_addr'] += "\n" + host_group['ip_addr']
              return

        host_group_list.append(host_group)

    host_group_list = []
    for i in range(len(details)):
        append_nodeinfo(details[i])
    return host_group_list


context['status'] = "online"
parse_context(context)
context["list"] = context["hostgroup_details"][0]
context["detail01"] = parse_hostgroup(hostgroup_details)


# tpl = DocxTemplate("tests/my_word_template.docx")
tpl = DocxTemplate("tests/zDataInspectionTemplate_v2.docx")
tpl.render(context, autoescape=True)
tpl.save("tests/01.docx")