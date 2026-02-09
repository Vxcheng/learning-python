#!/opt/zdata/zmanager/python/bin/python
#coding=utf-8
from docxtpl import DocxTemplate, RichText
import sys
import json
import time
import traceback
import re

reload(sys)
sys.setdefaultencoding('utf8')
node_types = {1:"存储",2:"计算",3:"融合",4:"仲裁"}


def mock_context():
    with open('mock_data.json', 'r') as f:
        dict = json.loads(f.read())
        return dict["data"]

def format_date(str):
    t = time.strptime(str, "%Y-%m-%d %H:%M:%S")
    date = time.strftime("%Y-%m-%d", t)
    return date

def  remain_precision(v):
    values = re.findall(r"\d{1,}?\.\d{2}", str(v))
    if len(values) > 0:
        return '%.2f' %  v
        # return values[0]
    return str(v)

def bytes_to_human(n):
    n = int(n)
    symbols = ('K','M','G','T','P','E','Z','Y')
    prefix = {}
    for i,s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            # return '%.2f%s' % (value,s)
            value = remain_precision(value)
            return ' %s%s' % (value,s)
    return '%sB' % n

def check_exist(elem, array):
    for value in array:
        if value == elem:
            return True
    
    return False

def mb_to_human(v):
    v = int(v)
    if v == 0:
        return '%s MB' % v

    if  v%1024 == 0:
        out = v/1024
        return '%d GB' % out
        
    out = float(v)/1024
    return '%.2f GB' %  out

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
    
    return  host_group_list

def parse_context(context):
    context["report_date"] = format_date(context["report_time"])
    parse_overview(context)
    parse_report(context)

def parse_overview(context):
    parse_question_overview(context["report_overview"]["question_overview"])

    context["report_overview"]["question_overview"]["count"] = len(context["report_overview"]["question_overview"]["details"])
    context["report_overview"]["db_overview"]["db_view"]["count"] = len(context["report_overview"]["db_overview"]["db_view"]["details"])
    context["db_report"]["multipath_check"]["multipath_service_status_check"]["count"] = len(context["db_report"]["multipath_check"]["multipath_service_status_check"]["details"])
    
    details = context["report_overview"]["db_overview"]["cluster_view"]["details"]
    cluster_fields = ["clusterReadyServices", "oracleHighAvailabilityServices", "clusterSynchronizationServices", "eventManager"]
    for detail in details:
        tmp_details = detail["details"]
        for row in tmp_details:
            for k,v in row.items():
                if check_exist(k, cluster_fields ):
                    if v == "online":
                        row[k] = "在线"
                    else:
                        row[k] = "离线"

    for i in range(len(context["report_overview"]["db_overview"]["db_view"]["details"])):
        context["report_overview"]["db_overview"]["db_view"]["details"][i]["count"] = len(context["report_overview"]["db_overview"]["db_view"]["details"][i]["db_instance_items"])
        if context["report_overview"]["db_overview"]["db_view"]["details"][i]["is_archive"] == False:
            context["report_overview"]["db_overview"]["db_view"]["details"][i]["is_archive_str"] = "否"
        else:
            context["report_overview"]["db_overview"]["db_view"]["details"][i]["is_archive_str"] = "是"
        
        if context["report_overview"]["db_overview"]["db_view"]["details"][i]["is_rac"] == False:
            context["report_overview"]["db_overview"]["db_view"]["details"][i]["is_rac_str"] = "否"
        else:
            context["report_overview"]["db_overview"]["db_view"]["details"][i]["is_rac_str"] = "是"
  
    for detail in context["report_overview"]["db_overview"]["asmgroup_view"]["details"]:
        for row in detail["asmgroup_items"]:
            row["total_mb"] = mb_to_human(row["total_mb"])
            row["free_mb"] = mb_to_human(row["free_mb"])
            row["usable_file_mb"] = mb_to_human(row["usable_file_mb"])        

    for i in range(len(context["report_overview"]["server_overview"]["server_list"])):
        if context["report_overview"]["server_overview"]["server_list"][i]["is_etcd"] == False:
            context["report_overview"]["server_overview"]["server_list"][i]["is_etcd_str"] = "否"
        else:
            context["report_overview"]["server_overview"]["server_list"][i]["is_etcd_str"] = "是"
        context["report_overview"]["server_overview"]["server_list"][i]["obj_type_str"] = node_types[context["report_overview"]["server_overview"]["server_list"][i]["obj_type"]]

        details = context["report_overview"]["ibswitch_overview"]["details"]

    server_list = context["report_overview"]["server_overview"]["server_list"]
    for server in server_list:
        server["uptime"] = server["uptime"].replace("y","年")
        server["uptime"] = server["uptime"].replace("M","月")
        server["uptime"] = server["uptime"].replace("d","天")
        server["uptime"] = server["uptime"].replace("h","小时")
        server["uptime"] = server["uptime"].replace("m","分钟")
        server["uptime"] = server["uptime"].replace("s","秒")
    server_details = context["report_overview"]["server_overview"]["server_details"]
    for sd in server_details:
        sata_sases = sd["sata_sases"]["details"]
        for ss in sata_sases:
            ss["size"] = bytes_to_human(ss["size"])
        pcie_nvmes = sd["pcie_nvmes"]["details"]
        for pn in pcie_nvmes:
            pn["size"] = bytes_to_human(pn["size"])

    details = context["report_overview"]["ibswitch_overview"]["details"]
    for i in range(len(details)):
        if details[i]["state"] == "online":
            details[i]["state"] = "在线"
        else:
            details[i]["state"] = "离线"
    
    parse_storage_resources_overview(context["report_overview"]["storage_resources_overview"])

def parse_report(context):
    #db_report
    #cluster
    for cluster in context["db_report"]["cluster_check"]["details"]:
        if cluster["problem_level"]  != "normal":
            rich_serial(cluster["check_results"])

    for detail in context["db_report"]["asmgroup_check"]["details"]:
        if detail["problem_level"]  != "normal":
            rich_serial(detail["check_results"])

    for detail in context["db_report"]["asm_disk_check"]["details"]:
        if detail["problem_level"]  != "normal":
            rich_serial(detail["check_results"])

    for detail in context["db_report"]["vote_disk_check"]["details"]:
        if detail["problem_level"]  != "normal":
            rich_serial(detail["check_results"])

    details = context["db_report"]["db_parameter_check"]["details"]
    for i in range(len(details)):
        for j in range(len(details[i]["details"])):
            if details[i]["details"][j]["is_default"] == False:
                details[i]["details"][j]["is_default_str"] = "否"
            else:
                details[i]["details"][j]["is_default_str"] = "是"

    #storage_resources_report
    #volume
    for detail in context["storage_resources_report"]["volume_check"]["details"]:
        if detail["problem_level"] != "normal":
            rich_check_results(detail["check_results"])

    #server_report
    #partition_usage_check
    detail = context["server_report"]["partition_usage_check"]["partition_usage_list"]
    if detail["problem_level"] != "normal":
        rich_serial(detail["desc"])

    #cpu
    detail = context["server_report"]["cpu_check"]["cpu_check_list"]
    if detail["problem_level"] != "normal":
        rich_check_results(detail["check_results"]) 

    for detail in context["server_report"]["memory_check"]["compute_memory_check"]["memory_check_list"]:
        if detail["problem_level"] != "normal":
            rich_check_results(detail["check_results"])

    detail =  context["server_report"]["memory_check"]["storage_memory_check"]["memory_check_list"]
    if detail["problem_level"] != "normal":
        rich_check_results(detail["check_results"])   

    #disk
    for detail in context["server_report"]["disk_check"]["disk_check_list"]:
        if detail["problem_level"]  != "normal":
            rich_serial(detail["check_results"]) 

    detail =  context["server_report"]["network_card_check"]["ipoib_check_list"]
    if detail["problem_level"] != "normal":
        rich_check_results(detail["item"]["check_results"]) 

    detail = context["server_report"]["network_card_check"]["ib_check_list"]
    if detail["problem_level"]  != "normal":
        rich_serial(detail["item"]["check_results"])
        
    detail = context["server_report"]["raid_card_check"]
    if detail["problem_level"]  != "normal":
        rich_serial(detail["details"]["check_results"])      

    detail = context["server_report"]["grub_params_check"]
    if detail["problem_level"]  != "normal":
        rich_serial(detail["check_results"]) 

    detail = context["server_report"]["kdump_service_check"]
    if detail["problem_level"]  != "normal":
        rich_serial(detail["details"]["check_results"]) 

    detail = context["ibswitch_check"]["detail"]
    if detail["problem_level"]  != "normal":
        rich_serial(detail["check_results"]) 

def parse_storage_resources_overview(storage_resources):
    storage_resources["hostgroup_view"]["details"] = parse_hostgroup(storage_resources["hostgroup_view"]["details"])

    details = storage_resources["storagepool_view"]["details"]
    r = lambda rest: remain_precision( 100 - rest) if rest > 0 else rest
    for i in range(len(details)):
        details[i]["total_size"] = bytes_to_human(details[i]["total_size"])
        details[i]["free_size"] = bytes_to_human(details[i]["free_size"])
        details[i]["rest"] = float(r(details[i]["rest"] ))
    
    # volume
    details = storage_resources["volume_view"]["details"]
    dev_re = re.compile('/dev/(.*)')
    for detail in details:
        for v in detail["volumes"]:
            v["unit"] = '%sB' % (v["unit"])
            values = dev_re.findall(v["dev_path"])
            if len(values) > 0:
                v["dev_path"] = values[0]

            if v["in_use"]:
                v["in_use"] = "是"
            else:
                v["in_use"] = "否"           

            if v["lv_state"] == 'normal':
                v["lv_state"] = "正常"
            else:
                v["lv_state"] = "异常"
    
def parse_question_overview(question_overview):
    for detail in question_overview["details"]:
        tmp_desc = add_serial(detail["desc"])
        detail["desc"] = tmp_desc
        # detail["problem_level_ch"] = rich_text(detail["problem_level"], detail["problem_level_ch"] )

def add_serial(desc):
    # aaa\nbbb
    lines = desc.splitlines()
    if len(lines) >= 2:
        sord_desc = ''
        for i in range(len(lines)):
            sord_desc += '{0}）{1}\n'.format(i+1, lines[i])

        return sord_desc[:-1]
    else:
        return desc

def rich_check_results(results):
    for i in range(len(results)) :
        results[i] = rich_text("check_results", results[i])
    # return results
 
def rich_text(name, value):
    # not use rich text
    return value
    # Microsoft YaHei, 微软雅黑
    rich_dict = {
        "critical": RichText(value, color='F5222D',font='Microsoft YaHei',size=18),
        "warning": RichText(value, color='FAAD14',font='Microsoft YaHei', size=18),
        "prompt":RichText(value, color='13C2C2',font='Microsoft YaHei', size=18),
        "normal":RichText(value, color='0A0D14',font='Microsoft YaHei', size=18),

        "check_results": RichText(value, color='F5222D',font='Microsoft YaHei',size=21),
    }
    return rich_dict.get(name, "normal")

def rich_serial(results):
    if len(results) < 2:
        return

    for i in range(len(results)) :
        tmp = '{0}）{1}'.format(i+1, results[i])
        results[i] = rich_text("check_results", tmp)

if __name__ == '__main__':
    tmp = sys.argv[1]
    out = sys.argv[2]
    context = json.loads(sys.argv[3])
    context = mock_context()
    parse_context(context)

    try:
        doc = DocxTemplate(tmp)
        doc.render(context)
        doc.save(out)
        print("ok")
    except Exception as e:
        traceback.print_exc()
        print(str(e))

'''
Todo: 
1. 巡检结果的颜色处理不使用RichText，使用模板中固定颜色
2. RichText使用微软雅黑字体
'''