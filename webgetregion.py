import json
import os
from configfile import *
import boto3

reg = []
from boto3.session import Session
if not os.environ.get('APIKEY'):
    ACCESS_KEY=os.environ.get('APIKEY')
    SECRET_KEY=os.environ.get('SECRET')

if ACCESS_KEY != "":
    print(ACCESS_KEY)
    s = Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY)
    print(s)
else:
    s=Session()
regions = s.get_available_regions('ec2')
region=""


for item in regions:
    try:
        #print(item)
        if item=="ap-east-1" or item=="me-south-1":
            continue
        ec22 = s.resource('ec2', region_name=item)
        instances = ec22.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        a=0
        for instance in instances:
           a=a+1
           #print(instance.id, instance.instance_type)
        if a>0: reg.append(item)
    except:
        print("permission error on region: ", item)
#print(reg)


from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = False


@app.route('/', methods=['GET'])
def dropdown():
    return render_template('reg.html', regionsactive=reg)

@app.route('/risorse', methods=['GET'])
def risorse():
    ins = []
    global region
    global s

    region = request.args.get('region')
    print(region)
    ec22 = s.resource('ec2', region_name=region)
    instances = ec22.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    a = 0
    for instance in instances:
        a = a + 1
        ins.append(instance.id)
        # print(instance.id, instance.instance_type)
    return render_template('ris.html', instancesinregion=ins,regn=region)

@app.route('/info', methods=['GET'])
def instanceinfo():
    global region
    global s

    insinfo = []
    instanceid = request.args.get('instanceid')
    region = request.args.get('regn')
    print("presaregion " + region + " presainstance " + instanceid)
    ec22 = s.resource('ec2', region_name=region)
    instances = ec22.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    a = 0
    for instance in instances:
        a = a + 1
        if instance.id==instanceid:
            insinfo.append("InstanceID="+instance.id)
            insinfo.append("InstanceState="+str(instance.state))
            insinfo.append("InstanceType=" + str(instance.instance_type))
    return render_template('info.html', instancesattributes=insinfo)

if __name__ == "__main__":
    app.run(debug=False)

