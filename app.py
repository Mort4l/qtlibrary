#encoding:utf-8
from flask import Flask
from urllib import urlopen
import datetime,base64,random,re
def get_qcode_img():
    data=base64.b64encode("QT；%d；%s"%(random.randint(105000,108000),datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    data=re.findall('<img src="(.+)" id="qrcode_plugins_img" class="qrcode_plugins_img" style="background: r',urlopen("https://cli.im/api/qrcode/code?text=%s&mhid=sEuSXgq8z5khMHcrKtxSPKg"%data).read())[0]
    return data

app = Flask(__name__)
@app.route('/')
def hello_world():
    return "<img src='%s'>"%get_qcode_img()


if __name__ == '__main__':
    app.run()
